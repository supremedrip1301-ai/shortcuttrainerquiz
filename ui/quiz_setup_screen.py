'''
quiz_setup_screen.py - choose software (Checkbuttons), quiz mode (Radiobuttons),
difficulty (Combobox), number of questions (Spinbox), seconds per question (Scale)
and lives mode (Checkbutton), then start the quiz.
'''

import tkinter as tk
from tkinter import messagebox, ttk

import config
from core import quiz_engine
from data.shortcuts import SOFTWARE_INFO, get_software_by_section
from ui.base_screen import Screen
from ui.widgets import HoverButton, ScrollableFrame, make_checkbutton, make_radiobutton

# (mode key, title, short description) - tuples because they never change
MODE_CHOICES = (
    ("action", "Guess the Action", "See the keys, pick what they do"),
    ("shortcut", "Guess the Shortcut", "See the action, pick the right keys"),
    ("mixed", "Mixed MCQ", "Both kinds of questions mixed"),
    ("press", "Press the Keys", "Really press the shortcut on the keyboard"),
    ("speed", "Speed Run", "60 seconds, as many as you can"),
    ("daily", "Daily Challenge", "Today's 10 questions (all software)"),
    ("revise", "Revise Weak Shortcuts", "Your most-missed shortcuts"),
)


class QuizSetupScreen(Screen):
    '''Custom quiz settings (inherits from Screen).'''

    def build(self):
        '''Create the software list on the left and the options on the right (method overriding).'''
        self.make_header("Custom Quiz", "choose software, mode and options")
        body = tk.Frame(self, bg=self.colors["bg"])
        body.pack(fill="both", expand=True, padx=16, pady=12)
        self.build_software_list(body)
        self.build_options(body)

    def build_software_list(self, parent):
        '''Left card: one Checkbutton per software, grouped by section, with Select All / Clear.'''
        card = self.make_card(parent)
        card.pack(side="left", fill="both", expand=True, padx=(0, 12))
        top = tk.Frame(card, bg=self.colors["panel"])
        top.pack(fill="x")
        self.make_label(top, "1. Choose software", config.FONT_MEDIUM, bg="panel").pack(side="left")
        HoverButton(top, "Clear", self.clear_all, self.colors, kind="secondary").pack(side="right")
        HoverButton(top, "Select All", self.select_all, self.colors, kind="secondary").pack(side="right", padx=6)
        scroll = ScrollableFrame(card, self.colors, bg_key="panel")
        scroll.pack(fill="both", expand=True, pady=(8, 0))
        self.software_vars = {}               # dictionary: software key -> BooleanVar
        for section, software_keys in get_software_by_section().items():
            if len(software_keys) == 0:
                continue
            self.make_label(scroll.inner, section, config.FONT_BOLD, "accent", "panel").pack(anchor="w", pady=(8, 0))
            for software_key in software_keys:
                var = tk.BooleanVar(value=False)
                make_checkbutton(scroll.inner, SOFTWARE_INFO[software_key]["name"], var, self.colors,
                                 command=self.update_available).pack(anchor="w", padx=12)
                self.software_vars[software_key] = var

    def build_options(self, parent):
        '''Right card: mode Radiobuttons and the other options.'''
        card = self.make_card(parent)
        card.pack(side="right", fill="y")
        HoverButton(card, "▶  Start Quiz", self.start, self.colors, kind="success",
                    font=config.FONT_MEDIUM).pack(side="bottom", fill="x", pady=(4, 0))
        self.make_label(card, "2. Quiz mode", config.FONT_MEDIUM, bg="panel").pack(anchor="w")
        self.mode_var = tk.StringVar(value="mixed")
        for mode, title, description in MODE_CHOICES:
            make_radiobutton(card, title + "  -  " + description, self.mode_var, mode, self.colors,
                             command=self.update_available).pack(anchor="w")
        self.make_label(card, "3. Options", config.FONT_MEDIUM, bg="panel").pack(anchor="w", pady=(10, 4))
        grid = tk.Frame(card, bg=self.colors["panel"])
        grid.pack(anchor="w")
        self.build_option_widgets(grid)
        self.available_label = self.make_label(card, "", config.FONT_NORMAL, "subtext", "panel")
        self.available_label.pack(anchor="w", pady=(8, 4))

    def build_option_widgets(self, grid):
        '''Difficulty Combobox, questions Spinbox, seconds Scale and lives Checkbutton.'''
        self.make_label(grid, "Difficulty", bg="panel").grid(row=0, column=0, sticky="w", pady=3)
        self.difficulty_box = ttk.Combobox(grid, values=["All", "Easy", "Medium", "Hard"],
                                           state="readonly", width=10, font=config.FONT_NORMAL)
        self.difficulty_box.set("All")
        self.difficulty_box.grid(row=0, column=1, sticky="w", padx=8)
        self.difficulty_box.bind("<<ComboboxSelected>>", lambda event: self.update_available())
        self.make_label(grid, "Questions", bg="panel").grid(row=1, column=0, sticky="w", pady=3)
        self.count_var = tk.StringVar(value=self.app.settings["questions"])
        ttk.Spinbox(grid, from_=config.MIN_QUESTIONS, to=config.MAX_QUESTIONS, textvariable=self.count_var,
                    width=8, font=config.FONT_NORMAL).grid(row=1, column=1, sticky="w", padx=8)
        self.make_label(grid, "Seconds / question", bg="panel").grid(row=2, column=0, sticky="w", pady=3)
        self.seconds_var = tk.IntVar(value=int(self.app.settings["seconds"]))
        tk.Scale(grid, from_=config.MIN_SECONDS, to=config.MAX_SECONDS, orient="horizontal",
                 variable=self.seconds_var, length=170, bg=self.colors["panel"], fg=self.colors["text"],
                 troughcolor=self.colors["panel_alt"], highlightthickness=0, bd=0,
                 activebackground=self.colors["accent"]).grid(row=2, column=1, sticky="w", padx=8)
        self.lives_var = tk.BooleanVar(value=False)
        make_checkbutton(grid, "Lives mode (3 hearts)", self.lives_var, self.colors).grid(
            row=3, column=0, columnspan=2, sticky="w", pady=3)

    # ---------------------------------------------------------------- helpers

    def select_all(self):
        '''Tick every software.'''
        for var in self.software_vars.values():
            var.set(True)
        self.update_available()

    def clear_all(self):
        '''Untick every software.'''
        for var in self.software_vars.values():
            var.set(False)
        self.update_available()

    def get_selected(self):
        '''Return a list with the keys of the ticked software.'''
        selected = []
        for software_key, var in self.software_vars.items():
            if var.get():
                selected.append(software_key)
        return selected

    def get_difficulty(self):
        '''Return the chosen difficulty in lower case ("all", "easy", ...).'''
        return self.difficulty_box.get().lower()

    def update_available(self):
        '''Show how many questions are possible with the current choices.'''
        mode = self.mode_var.get()
        if mode in ("daily", "revise"):
            self.available_label.config(text="This mode chooses its own questions.")
            return
        available = quiz_engine.count_available(self.get_selected(), self.get_difficulty(), mode)
        self.available_label.config(text=str(available) + " different questions available")

    def on_show(self, software=None, mode=None, **data):
        '''Pre-select a software (when a home card was clicked) or a mode (method overriding).'''
        self.count_var.set(self.app.settings["questions"])          # defaults from Settings
        self.seconds_var.set(int(self.app.settings["seconds"]))
        if software is not None:
            self.clear_all()
            self.software_vars[software].set(True)
        if mode is not None:
            self.mode_var.set(mode)
        self.update_available()

    # ---------------------------------------------------------------- start

    def read_count(self):
        '''Read the Spinbox value safely. Returns None (and warns) if it is not valid.'''
        try:
            count = int(self.count_var.get())
        except ValueError:
            count = 0
        if count < config.MIN_QUESTIONS or count > config.MAX_QUESTIONS:
            messagebox.showwarning("Questions", "Please choose between %d and %d questions."
                                   % (config.MIN_QUESTIONS, config.MAX_QUESTIONS))
            return None
        return count

    def check_press_mode(self, selected, count):
        '''Press mode needs shortcuts that can be pressed. Returns (mode, count) or (None, 0).'''
        available = quiz_engine.count_available(selected, self.get_difficulty(), "press")
        if available == 0:
            if messagebox.askyesno("Press the Keys", "None of these shortcuts can be pressed inside the app "
                                   "(Windows itself uses them).\nPlay 'Guess the Shortcut' (MCQ) instead?"):
                return "shortcut", count
            return None, 0
        if available < count:
            if messagebox.askyesno("Press the Keys", "Only %d of these shortcuts can be pressed inside the app.\n"
                                   "Yes = play %d Press questions.\nNo = play MCQ with %d questions instead."
                                   % (available, available, count)):
                return "press", available
            return "shortcut", count
        return "press", count

    def start(self):
        '''Check the choices and ask the App to start the quiz.'''
        mode = self.mode_var.get()
        selected = self.get_selected()
        if mode not in ("daily", "revise") and len(selected) == 0:
            messagebox.showwarning("No software", "Please tick at least one software.")
            return
        count = self.read_count()
        if count is None:
            return
        if mode == "press":
            mode, count = self.check_press_mode(selected, count)
            if mode is None:
                return
        quiz_settings = {"mode": mode, "software_list": selected, "difficulty": self.get_difficulty(),
                         "count": count, "seconds": self.seconds_var.get(), "lives": self.lives_var.get()}
        self.app.start_from_settings(quiz_settings)
