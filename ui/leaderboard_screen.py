'''
leaderboard_screen.py - top scores of all players in a Treeview.
The rows are sorted with sorted(rows, key=lambda row: row["score"], reverse=True)
(see core/stats.py), can be filtered by mode and software, and the current
player's rows are highlighted.
'''

import tkinter as tk
from tkinter import ttk

import config
from core import stats
from core.quiz_engine import QUIZ_MODES
from data.shortcuts import get_all_software_names, get_display_name
from ui.base_screen import Screen

MAX_ROWS = 50


class LeaderboardScreen(Screen):
    '''Leaderboard with filters (inherits from Screen).'''

    def build(self):
        '''Create the filters and the Treeview (method overriding).'''
        self.make_header("Leaderboard", "best scores of all players on this computer")
        filters = tk.Frame(self, bg=self.colors["bg"])
        filters.pack(fill="x", padx=16, pady=(12, 6))
        self.make_label(filters, "Mode:").pack(side="left")
        modes = ["All"] + list(QUIZ_MODES.values()) + ["Daily Practice"]
        self.mode_box = ttk.Combobox(filters, values=modes, state="readonly", width=22, font=config.FONT_NORMAL)
        self.mode_box.set("All")
        self.mode_box.pack(side="left", padx=(4, 16))
        self.mode_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())
        self.make_label(filters, "Software:").pack(side="left")
        self.name_to_key = {"All": "All"}
        for software_key in get_all_software_names():
            self.name_to_key[get_display_name(software_key)] = software_key
        self.software_box = ttk.Combobox(filters, values=list(self.name_to_key.keys()), state="readonly",
                                         width=22, font=config.FONT_NORMAL)
        self.software_box.set("All")
        self.software_box.pack(side="left", padx=4)
        self.software_box.bind("<<ComboboxSelected>>", lambda event: self.refresh())
        self.info_label = self.make_label(filters, "", config.FONT_SMALL, "subtext")
        self.info_label.pack(side="right")
        self.build_table()

    def build_table(self):
        '''Treeview: Rank, Player, Mode, Software, Score, Accuracy, Grade, Date.'''
        box = tk.Frame(self, bg=self.colors["bg"])
        box.pack(fill="both", expand=True, padx=16, pady=(0, 14))
        columns = ("rank", "player", "mode", "software", "score", "accuracy", "grade", "date")
        headings = ("Rank", "Player", "Mode", "Software", "Score", "Accuracy", "Grade", "Date")
        widths = (60, 140, 170, 230, 80, 90, 60, 150)
        self.table = ttk.Treeview(box, columns=columns, show="headings")
        for column, heading, width in zip(columns, headings, widths):
            self.table.heading(column, text=heading)
            self.table.column(column, width=width, anchor="w")
        self.table.tag_configure("me", background=self.colors["panel_alt"], foreground=self.colors["accent"])
        self.table.tag_configure("top", foreground=self.colors["warning"])
        scrollbar = ttk.Scrollbar(box, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def on_show(self, **data):
        '''Reload the scores every time the screen opens (method overriding).'''
        self.refresh()

    def software_text(self, software_list):
        '''Short text for the software column ("VS Code" or "5 software").'''
        keys = software_list.split("|")
        if len(keys) > 2:
            return str(len(keys)) + " software"
        return ", ".join(map(get_display_name, keys))      # map() with a function

    def refresh(self):
        '''Fill the table with the filtered, sorted rows.'''
        self.table.delete(*self.table.get_children())
        software = self.name_to_key[self.software_box.get()]
        rows = stats.get_leaderboard_rows(self.mode_box.get(), software)
        my_name = self.app.player.name
        for rank, row in enumerate(rows[:MAX_ROWS], start=1):
            tags = []
            if row["player"] == my_name:
                tags.append("me")
            elif rank <= 3:
                tags.append("top")
            self.table.insert("", "end", tags=tags, values=(
                "#" + str(rank), row["player"], row["mode"], self.software_text(row["software_list"]),
                row["score"], str(row["accuracy"]) + "%", row["grade"], row["date_time"][:16]))
        if len(rows) == 0:
            self.info_label.config(text="No scores yet - play a quiz!")
        else:
            self.info_label.config(text="Your rows are highlighted. Showing %d of %d."
                                   % (min(len(rows), MAX_ROWS), len(rows)))
