'''
home_screen.py - the dashboard after login.

* the menubar is built exactly like the "Menu Demonstration" example (PPT 3.4)
* the right-click popup menu is built exactly like the popup example (PPT 3.4)
* a greeting card with level, XP bar, streak, quizzes and accuracy
* a scrollable grid of software cards grouped by section; a click opens Quiz Setup
'''

import datetime
import tkinter as tk
from tkinter import Menu, ttk

import config
from core import stats, storage
from data.shortcuts import ALL_SOFTWARE, SOFTWARE_INFO, count_all_shortcuts, get_software_by_section
from ui.base_screen import Screen
from ui.learn_screen import export_cheat_sheet
from ui.widgets import HoverButton, ScrollableFrame, draw_badge, draw_flame

CARDS_PER_ROW = 4


class HomeScreen(Screen):
    '''The main dashboard (inherits from Screen).'''

    def build(self):
        '''Create menubar, popup menu, greeting card, quick buttons and software cards.'''
        self.best_labels = {}            # software key -> Label that shows the best accuracy
        self.create_menubar()
        self.create_popup_menu()
        self.build_greeting()
        self.build_quick_buttons()
        self.scroll = ScrollableFrame(self, self.colors)
        self.scroll.pack(fill="both", expand=True, padx=16, pady=(4, 10))
        self.build_software_cards(self.scroll.inner)
        self.bind_popup(self)

    # ---------------------------------------------------------------- menus (PPT 3.4)

    def create_menubar(self):
        '''Build the menubar in the same way as the PPT 3.4 "Menu Demonstration" code.'''
        root = self.app.root

        # Creating Menubar
        menubar = Menu(root)

        # Adding File Menu and commands
        file = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='File', menu = file)
        file.add_command(label ='New Quiz', command = lambda: self.app.show_screen("quiz_setup"))
        file.add_command(label ='Switch Player', command = lambda: self.app.show_screen("login"))
        file.add_command(label ='Export Cheat Sheet', command = lambda: export_cheat_sheet(root))
        file.add_separator()
        file.add_command(label ='Exit', command = self.app.on_close)

        # Adding View Menu and commands
        view = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='View', menu = view)
        view.add_command(label ='Dark Theme', command = lambda: self.app.set_theme("dark"))
        view.add_command(label ='Light Theme', command = lambda: self.app.set_theme("light"))
        view.add_separator()
        view.add_command(label ='Fullscreen  (F11)', command = self.app.toggle_fullscreen)

        # Adding Practice Menu and commands
        practice = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Practice', menu = practice)
        practice.add_command(label ='Daily Challenge', command = self.app.start_daily_challenge)
        practice.add_command(label ='Revise Weak Shortcuts', command = self.app.start_revise)

        # Adding Help Menu
        help_ = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='How to Play', command = lambda: self.app.open_help("how"))
        help_.add_command(label ='Shortcut Format Guide', command = lambda: self.app.open_help("format"))
        help_.add_separator()
        help_.add_command(label ='About', command = lambda: self.app.open_help("about"))

        # display Menu
        root.config(menu = menubar)
        self.menubar = menubar

    def create_popup_menu(self):
        '''Build the right-click menu in the same way as the PPT 3.4 popup example.'''
        #Add Menu
        self.popup = Menu(self, tearoff=0)

        #Adding Menu Items
        self.popup.add_command(label="Start Quick Quiz", command=self.app.start_quick_quiz)
        self.popup.add_command(label="Learn Mode", command=lambda: self.app.show_screen("learn"))
        self.popup.add_separator()
        self.popup.add_command(label="Statistics", command=lambda: self.app.show_screen("stats"))
        self.popup.add_command(label="Settings", command=lambda: self.app.show_screen("settings"))

    def menu_popup(self, event):
        '''Show the popup menu where the mouse was right-clicked.'''
        # display the popup menu
        try:
            self.popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            #Release the grab
            self.popup.grab_release()

    def bind_popup(self, widget):
        '''Bind <Button-3> (right click) to the widget and to all widgets inside it.'''
        widget.bind("<Button-3>", self.menu_popup)
        for child in widget.winfo_children():
            self.bind_popup(child)            # recursion: children of children too

    # ---------------------------------------------------------------- greeting card

    def build_greeting(self):
        '''Top card: avatar, greeting, level + XP bar and four small statistic tiles.'''
        card = self.make_card(self, 18, 12)
        card.pack(fill="x", padx=16, pady=(14, 8))
        self.avatar = tk.Canvas(card, width=64, height=64, bg=self.colors["panel"], highlightthickness=0)
        self.avatar.pack(side="left")
        text_box = tk.Frame(card, bg=self.colors["panel"])
        text_box.pack(side="left", padx=14)
        self.greeting = self.make_label(text_box, "", config.FONT_LARGE, bg="panel")
        self.greeting.pack(anchor="w")
        self.level_label = self.make_label(text_box, "", config.FONT_NORMAL, "subtext", "panel")
        self.level_label.pack(anchor="w")
        self.xp_bar = ttk.Progressbar(text_box, orient="horizontal", length=260, maximum=100)
        self.xp_bar.pack(anchor="w", pady=4)
        tiles = tk.Frame(card, bg=self.colors["panel"])
        tiles.pack(side="right")
        self.streak_canvas = tk.Canvas(tiles, width=28, height=34, bg=self.colors["panel"], highlightthickness=0)
        self.streak_canvas.grid(row=0, column=0, rowspan=2, padx=(0, 4))
        self.tile_values = {}
        titles = ("Day streak", "Quizzes", "Accuracy", "Shortcuts")
        for number, title in enumerate(titles):
            value = self.make_label(tiles, "0", config.FONT_MEDIUM, "text", "panel")
            value.grid(row=0, column=number + 1, padx=16)
            self.make_label(tiles, title, config.FONT_SMALL, "subtext", "panel").grid(row=1, column=number + 1)
            self.tile_values[title] = value

    def build_quick_buttons(self):
        '''A row of big buttons for the main features.'''
        row = tk.Frame(self, bg=self.colors["bg"])
        row.pack(fill="x", padx=16, pady=(0, 6))
        buttons = [
            ("⚡ Quick Quiz", self.app.start_quick_quiz, "primary"),
            ("☀ Daily", self.app.start_daily_challenge, "success"),
            ("✚ Custom", lambda: self.app.show_screen("quiz_setup"), "secondary"),
            ("✎ Learn", lambda: self.app.show_screen("learn"), "secondary"),
            ("Statistics", lambda: self.app.show_screen("stats"), "secondary"),
            ("Leaderboard", lambda: self.app.show_screen("leaderboard"), "secondary"),
            ("★ Badges", lambda: self.app.show_screen("achievements"), "secondary"),
            ("⚙ Settings", lambda: self.app.show_screen("settings"), "secondary"),
        ]
        for number, (text, command, kind) in enumerate(buttons):
            # grid with uniform columns: all buttons get the same width
            row.columnconfigure(number, weight=1, uniform="quick")
            button = HoverButton(row, text, command, self.colors, kind=kind, font=(config.FONT_FAMILY, 10, "bold"))
            button.grid(row=0, column=number, padx=3, sticky="ew")

    # ---------------------------------------------------------------- software cards

    def build_software_cards(self, parent):
        '''Create one section heading and a grid of cards for every section.'''
        groups = get_software_by_section()
        for section, software_keys in groups.items():
            if len(software_keys) == 0:
                continue
            self.make_label(parent, section, config.FONT_MEDIUM).pack(anchor="w", pady=(10, 4))
            grid = tk.Frame(parent, bg=self.colors["bg"])
            grid.pack(fill="x")
            for column in range(CARDS_PER_ROW):
                grid.columnconfigure(column, weight=1, uniform="cards")
            for number, software_key in enumerate(software_keys):
                card = self.make_software_card(grid, software_key)
                card.grid(row=number // CARDS_PER_ROW, column=number % CARDS_PER_ROW,
                          padx=5, pady=5, sticky="nsew")

    def make_software_card(self, parent, software_key):
        '''Create one card: self-drawn badge with initials, name, number of shortcuts, best score.'''
        info = SOFTWARE_INFO[software_key]
        card = tk.Frame(parent, bg=self.colors["panel"], padx=10, pady=10, cursor="hand2")
        badge = tk.Canvas(card, width=52, height=52, bg=self.colors["panel"], highlightthickness=0)
        badge.pack(side="left")
        draw_badge(badge, 26, 26, 48, info["initials"], info["color"])
        text_box = tk.Frame(card, bg=self.colors["panel"])
        text_box.pack(side="left", padx=10, fill="x")
        self.make_label(text_box, info["name"], config.FONT_BOLD, bg="panel").pack(anchor="w")
        count_text = str(len(ALL_SOFTWARE[software_key])) + " shortcuts"
        self.make_label(text_box, count_text, config.FONT_SMALL, "subtext", "panel").pack(anchor="w")
        best = self.make_label(text_box, "Not played yet", config.FONT_SMALL, "subtext", "panel")
        best.pack(anchor="w")
        self.best_labels[software_key] = best
        # hover colour and click for the card and everything inside it
        widgets = [card, badge, text_box] + text_box.winfo_children()
        for widget in widgets:
            widget.bind("<Enter>", lambda event, w=widgets: self.set_card_color(w, self.colors["panel_alt"]))
            widget.bind("<Leave>", lambda event, w=widgets: self.set_card_color(w, self.colors["panel"]))
            widget.bind("<Button-1>", lambda event, key=software_key: self.open_setup(key))
        return card

    def set_card_color(self, widgets, color):
        '''Change the background of all widgets of one card (hover effect).'''
        for widget in widgets:
            widget.config(bg=color)

    def open_setup(self, software_key):
        '''Open Quiz Setup with this software already selected.'''
        self.app.show_screen("quiz_setup", software=software_key)

    # ---------------------------------------------------------------- showing

    def on_show(self, **data):
        '''Attach the menubar again and refresh the player's numbers (method overriding).'''
        self.app.root.config(menu=self.menubar)
        player = self.app.player
        if player is None:
            return
        self.draw_avatar(player)
        self.greeting.config(text=self.get_greeting() + ", " + player.name + "!")
        self.level_label.config(text="Level %d   |   %d / 100 XP to the next level   |   total %d XP"
                                % (player.get_level(), player.xp_in_current_level(), player.get_xp()))
        self.xp_bar["value"] = player.xp_in_current_level()
        self.tile_values["Day streak"].config(text=str(player.streak))
        self.tile_values["Quizzes"].config(text=str(len(storage.load_history(player.name))))
        self.tile_values["Accuracy"].config(text=str(stats.get_overall_accuracy(player.name)) + "%")
        self.tile_values["Shortcuts"].config(text=str(count_all_shortcuts()))
        self.streak_canvas.delete("all")
        draw_flame(self.streak_canvas, 2, 4, 24, player.streak > 0)
        self.update_best_scores(player)

    def draw_avatar(self, player):
        '''Draw the player's avatar: coloured circle with the first letter.'''
        self.avatar.delete("all")
        self.avatar.create_oval(4, 4, 60, 60, fill=player.avatar, outline="")
        self.avatar.create_text(32, 32, text=player.name[0].upper(), fill="white", font=config.FONT_LARGE)

    def get_greeting(self):
        '''Return "Good morning / afternoon / evening" depending on the clock.'''
        hour = datetime.datetime.now().hour
        if hour < 12:
            return "Good morning"
        elif hour < 17:
            return "Good afternoon"
        else:
            return "Good evening"

    def update_best_scores(self, player):
        '''Write the best accuracy of the player on every software card.'''
        best = stats.get_best_accuracy_per_software(player.name)
        for software_key, label in self.best_labels.items():
            if software_key in best:
                label.config(text="Best: " + str(best[software_key]) + "%", fg=self.colors["success"])
            else:
                label.config(text="Not played yet", fg=self.colors["subtext"])

    def destroy(self):
        '''Method overriding: also destroy the menubar, which belongs to the root window.'''
        try:
            self.menubar.destroy()
        except tk.TclError:
            pass
        super().destroy()
