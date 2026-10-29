'''
stats_screen.py - the player's statistics.

history.csv is read with pandas (like the slide: penguins = pd.read_csv("penguins.csv")),
numbers are calculated with NumPy (core/stats.py), and two Matplotlib charts are shown:
a line chart of the accuracy in the last 20 quizzes and a bar chart per software.
'''

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import config
from core import stats, storage
from core.quiz_engine import find_shortcut
from data.shortcuts import get_display_name
from ui.base_screen import Screen
from ui.widgets import HoverButton, style_chart


class StatsScreen(Screen):
    '''Statistics, charts and weakest shortcuts (inherits from Screen).'''

    def build(self):
        '''Create the header and an empty content frame (method overriding).'''
        self.make_header("Statistics", "your progress over time")
        self.content = tk.Frame(self, bg=self.colors["bg"])
        self.content.pack(fill="both", expand=True, padx=16, pady=10)
        self.figure = None
        self.chart_widget = None

    def on_show(self, **data):
        '''Rebuild the content every time, so it always shows the newest data (method overriding).'''
        self.clear_content()
        player = self.app.player
        summary = stats.get_player_summary(player.name)
        if summary["quizzes"] == 0:
            self.show_empty_state()
            return
        self.build_tiles(summary)
        middle = tk.Frame(self.content, bg=self.colors["bg"])
        middle.pack(fill="both", expand=True, pady=(10, 0))
        self.build_charts(middle, player.name)
        self.build_weak_table(middle, player.name)

    def on_hide(self):
        '''Free the chart when the screen is left (method overriding).'''
        self.clear_content()

    def clear_content(self):
        '''Remove all widgets of the content frame and the Matplotlib figure.'''
        if self.figure is not None:
            self.figure.clear()
            self.figure = None
        for child in self.content.winfo_children():
            child.destroy()

    def show_empty_state(self):
        '''Friendly message when the player has not finished any quiz yet.'''
        box = self.make_card(self.content, 40, 40)
        box.pack(expand=True)
        self.make_label(box, "★", config.FONT_HUGE, "accent", "panel").pack()
        self.make_label(box, "No statistics yet", config.FONT_LARGE, bg="panel").pack(pady=6)
        self.make_label(box, "Finish your first quiz and your progress will appear here.",
                        config.FONT_NORMAL, "subtext", "panel").pack()
        HoverButton(box, "⚡ Start a Quick Quiz", self.app.start_quick_quiz, self.colors).pack(pady=(16, 0))

    def build_tiles(self, summary):
        '''A row of number tiles: quizzes, average accuracy, best score, favourite, time.'''
        row = tk.Frame(self.content, bg=self.colors["bg"])
        row.pack(fill="x")
        minutes = summary["total_time"] // 60
        tiles = [("Quizzes played", str(summary["quizzes"])),
                 ("Average accuracy", str(summary["avg_accuracy"]) + "%"),
                 ("Best score", str(summary["best_score"])),
                 ("Favourite software", summary["favourite"]),
                 ("Time played", str(minutes) + " min")]
        for number, (title, value) in enumerate(tiles):
            row.columnconfigure(number, weight=1, uniform="tiles")
            tile = self.make_card(row, 12, 8)
            tile.grid(row=0, column=number, padx=4, sticky="nsew")
            self.make_label(tile, value, config.FONT_MEDIUM, "accent", "panel").pack()
            self.make_label(tile, title, config.FONT_SMALL, "subtext", "panel").pack()

    def build_charts(self, parent, player_name):
        '''Line chart (slide style: title, xlabel, ylabel, grid) and a bar chart per software.

        NOTE (advanced): FigureCanvasTkAgg shows the Matplotlib figure inside the Tkinter
        window; plt.show() would open a second window and block the app.'''
        frame = tk.Frame(parent, bg=self.colors["panel"])
        frame.pack(side="left", fill="both", expand=True)
        self.figure = Figure(figsize=(6.4, 3.4), dpi=100)
        line_axes = self.figure.add_subplot(1, 2, 1)
        bar_axes = self.figure.add_subplot(1, 2, 2)
        x_values, y_values = stats.get_accuracy_trend(player_name, 20)
        line_axes.plot(x_values, y_values, marker='o', color=self.colors["accent"])
        line_axes.set_title("Accuracy - last 20 quizzes", fontsize=10)
        line_axes.set_xlabel("Quiz number", fontsize=8)
        line_axes.set_ylabel("Accuracy (%)", fontsize=8)
        line_axes.set_ylim(0, 105)
        line_axes.set_xticks(x_values)              # whole quiz numbers only (1, 2, 3 ...)
        line_axes.grid(alpha=0.3)
        per_software = stats.get_accuracy_per_software(player_name)
        names = list(per_software.keys())
        values = list(per_software.values())
        positions = list(range(len(names)))
        bar_axes.bar(positions, values, label="Accuracy %", width=.5, color=self.colors["success"])
        bar_axes.set_xticks(positions)
        bar_axes.set_xticklabels(names, rotation=60, ha="right", fontsize=7)
        bar_axes.set_ylim(0, 125)
        bar_axes.legend(fontsize=7, loc="upper right")
        bar_axes.set_ylabel("Accuracy (%)", fontsize=8)
        bar_axes.set_title("Accuracy per software", fontsize=10)
        style_chart(self.figure, [line_axes, bar_axes], self.colors)
        self.figure.tight_layout()
        try:
            canvas = FigureCanvasTkAgg(self.figure, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
        except Exception as error:
            self.make_label(frame, "Chart could not be drawn: " + str(error), color="danger", bg="panel").pack()

    def build_weak_table(self, parent, player_name):
        '''Treeview with the 10 weakest shortcuts (most wrong answers).'''
        frame = self.make_card(parent, 10, 8)
        frame.pack(side="right", fill="y", padx=(10, 0))
        self.make_label(frame, "Your 10 weakest shortcuts", config.FONT_BOLD, bg="panel").pack(anchor="w")
        table = ttk.Treeview(frame, columns=("software", "keys", "count"), show="headings", height=10)
        for column, heading, width in (("software", "Software", 105), ("keys", "Shortcut", 95),
                                       ("count", "Wrong", 50)):
            table.heading(column, text=heading)
            table.column(column, width=width, anchor="w")
        table.pack(fill="y", expand=True, pady=6)
        weak = storage.load_mistakes(player_name)[:10]
        for row in weak:
            table.insert("", "end", values=(get_display_name(row["software"]), row["keys"], row["wrong_count"]))
        if len(weak) == 0:
            self.make_label(frame, "No weak shortcuts - great!", config.FONT_SMALL, "success", "panel").pack()
        else:
            self.tip_label = self.make_label(frame, "Click a row to see the action.", config.FONT_SMALL,
                                             "subtext", "panel", wraplength=280, justify="left")
            self.tip_label.pack(anchor="w")
            table.bind("<<TreeviewSelect>>", lambda event: self.show_action(table, weak))
            HoverButton(frame, "Revise these now", self.app.start_revise, self.colors, kind="danger").pack(fill="x")

    def show_action(self, table, weak):
        '''Show what the selected weak shortcut does.'''
        selection = table.selection()
        if len(selection) == 0:
            return
        row = weak[table.index(selection[0])]
        shortcut = find_shortcut(row["software"], row["keys"])
        if shortcut is not None:
            self.tip_label.config(text=row["keys"] + " = " + shortcut.action)
