'''
achievements_screen.py - all badges in a grid. Unlocked badges are coloured and show
the date; locked badges are grey. The badge icons are drawn on a Canvas (create_oval).
'''

import tkinter as tk
from tkinter import ttk

import config
from core import storage
from core.models import create_all_achievements
from ui.base_screen import Screen
from ui.widgets import ScrollableFrame, draw_badge

BADGES_PER_ROW = 3


class AchievementsScreen(Screen):
    '''Badge collection (inherits from Screen).'''

    def build(self):
        '''Create the header, the progress line and a scrollable grid (method overriding).'''
        self.make_header("Achievements", "collect all badges")
        top = tk.Frame(self, bg=self.colors["bg"])
        top.pack(fill="x", padx=16, pady=(12, 4))
        self.count_label = self.make_label(top, "", config.FONT_MEDIUM)
        self.count_label.pack(side="left")
        self.progress = ttk.Progressbar(top, orient="horizontal", length=300)
        self.progress.pack(side="left", padx=16)
        self.scroll = ScrollableFrame(self, self.colors)
        self.scroll.pack(fill="both", expand=True, padx=16, pady=(4, 12))

    def on_show(self, **data):
        '''Draw every badge with the current unlock state (method overriding).'''
        for child in self.scroll.inner.winfo_children():
            child.destroy()
        unlocked = storage.load_achievements(self.app.player.name)
        badges = create_all_achievements()
        for badge in badges:
            if badge.badge_id in unlocked:
                badge.unlock(unlocked[badge.badge_id])
        done = len([b for b in badges if b.unlocked])
        self.count_label.config(text="%d / %d badges unlocked" % (done, len(badges)))
        self.progress["maximum"] = len(badges)
        self.progress["value"] = done
        grid = self.scroll.inner
        for column in range(BADGES_PER_ROW):
            grid.columnconfigure(column, weight=1, uniform="badges")
        # unlocked badges first: sorted() with a lambda (True sorts after False, so reverse=True)
        badges = sorted(badges, key=lambda b: b.unlocked, reverse=True)
        for number, badge in enumerate(badges):
            card = self.make_badge_card(grid, badge)
            card.grid(row=number // BADGES_PER_ROW, column=number % BADGES_PER_ROW, padx=6, pady=6, sticky="nsew")
        self.scroll.scroll_to_top()

    def make_badge_card(self, parent, badge):
        '''One card: round badge (coloured or grey), title, description and date.'''
        card = tk.Frame(parent, bg=self.colors["panel"], padx=10, pady=10)
        icon = tk.Canvas(card, width=64, height=64, bg=self.colors["panel"], highlightthickness=0)
        icon.pack(side="left")
        if badge.unlocked:
            draw_badge(icon, 32, 32, 58, badge.symbol, badge.color)
            title_color = "text"
            status = "Unlocked on " + badge.date
            status_color = "success"
        else:
            draw_badge(icon, 32, 32, 58, badge.symbol, self.colors["panel_alt"], self.colors["subtext"])
            title_color = "subtext"
            status = "Locked"
            status_color = "subtext"
        text = tk.Frame(card, bg=self.colors["panel"])
        text.pack(side="left", padx=10, fill="x")
        self.make_label(text, badge.title, config.FONT_BOLD, title_color, "panel").pack(anchor="w")
        self.make_label(text, badge.description, config.FONT_SMALL, "subtext", "panel",
                        wraplength=220, justify="left").pack(anchor="w")
        self.make_label(text, status, config.FONT_SMALL, status_color, "panel").pack(anchor="w")
        return card
