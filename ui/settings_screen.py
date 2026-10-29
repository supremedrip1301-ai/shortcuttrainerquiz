'''
settings_screen.py - theme, sound, quiz defaults and "Reset my progress".
Every change is saved to saves/settings.csv and applied at once.
'''

import tkinter as tk
from tkinter import messagebox, ttk

import config
from core import sound, storage
from ui.base_screen import Screen
from ui.widgets import HoverButton, make_checkbutton, make_radiobutton


class SettingsScreen(Screen):
    '''App settings (inherits from Screen).'''

    def build(self):
        '''Create two columns of setting cards (method overriding).'''
        self.make_header("Settings", "changes are saved at once")
        body = tk.Frame(self, bg=self.colors["bg"])
        body.pack(fill="both", expand=True, padx=16, pady=12)
        left = tk.Frame(body, bg=self.colors["bg"])
        left.pack(side="left", fill="both", expand=True, padx=(0, 8))
        right = tk.Frame(body, bg=self.colors["bg"])
        right.pack(side="left", fill="both", expand=True, padx=(8, 0))
        self.build_appearance(left)
        self.build_quiz_defaults(left)
        self.build_danger_zone(right)

    def section(self, parent, title):
        '''Create a card with a title and return it.'''
        card = self.make_card(parent)
        card.pack(fill="x", pady=(0, 12))
        self.make_label(card, title, config.FONT_MEDIUM, bg="panel").pack(anchor="w", pady=(0, 6))
        return card

    def build_appearance(self, parent):
        '''Theme Radiobuttons and the sound Checkbutton.'''
        card = self.section(parent, "Appearance & sound")
        self.theme_var = tk.StringVar(value=self.app.settings["theme"])
        make_radiobutton(card, "Dark theme", self.theme_var, "dark", self.colors,
                         command=self.change_theme).pack(anchor="w")
        make_radiobutton(card, "Light theme", self.theme_var, "light", self.colors,
                         command=self.change_theme).pack(anchor="w")
        self.sound_var = tk.BooleanVar(value=self.app.settings["sound"] == "on")
        row = tk.Frame(card, bg=self.colors["panel"])
        row.pack(fill="x", pady=(8, 0))
        make_checkbutton(row, "Play feedback sounds", self.sound_var, self.colors,
                         command=self.change_sound).pack(side="left")
        HoverButton(row, "Test sound", lambda: sound.play_correct(True), self.colors,
                    kind="secondary").pack(side="right")

    def build_quiz_defaults(self, parent):
        '''Default seconds per question (Scale) and default number of questions (Spinbox).'''
        card = self.section(parent, "Quiz defaults")
        self.make_label(card, "Seconds per question", bg="panel").pack(anchor="w")
        self.seconds_var = tk.IntVar(value=int(self.app.settings["seconds"]))
        tk.Scale(card, from_=config.MIN_SECONDS, to=config.MAX_SECONDS, orient="horizontal",
                 variable=self.seconds_var, length=260, bg=self.colors["panel"], fg=self.colors["text"],
                 troughcolor=self.colors["panel_alt"], highlightthickness=0, bd=0,
                 activebackground=self.colors["accent"],
                 command=lambda value: self.change_defaults()).pack(anchor="w")
        self.make_label(card, "Number of questions", bg="panel").pack(anchor="w", pady=(8, 0))
        self.questions_var = tk.StringVar(value=self.app.settings["questions"])
        spinbox = ttk.Spinbox(card, from_=config.MIN_QUESTIONS, to=config.MAX_QUESTIONS, width=8,
                              textvariable=self.questions_var, font=config.FONT_NORMAL,
                              command=self.change_defaults)
        spinbox.pack(anchor="w")
        spinbox.bind("<FocusOut>", lambda event: self.change_defaults())
        spinbox.bind("<Return>", lambda event: self.change_defaults())

    def build_danger_zone(self, parent):
        '''Reset button and the location of the save files.'''
        card = self.section(parent, "My data")
        self.make_label(card, "Save files are in:\n" + config.SAVES_DIR, config.FONT_SMALL, "subtext", "panel",
                        justify="left", wraplength=420).pack(anchor="w")
        HoverButton(card, "Reset my progress", self.reset_progress, self.colors,
                    kind="danger").pack(anchor="w", pady=(10, 0))

    # ---------------------------------------------------------------- saving the changes

    def on_show(self, **data):
        '''Show the current values (method overriding).'''
        self.theme_var.set(self.app.settings["theme"])

    def change_theme(self):
        '''Apply the chosen theme (all screens are rebuilt).'''
        if self.theme_var.get() != self.app.settings["theme"]:
            self.app.set_theme(self.theme_var.get())

    def change_sound(self):
        '''Sound on / off.'''
        if self.sound_var.get():
            self.app.settings["sound"] = "on"
        else:
            self.app.settings["sound"] = "off"
        self.app.save_settings()

    def change_defaults(self):
        '''Save the default seconds and number of questions (only valid numbers).'''
        try:
            questions = int(self.questions_var.get())
        except ValueError:
            questions = 0
        if config.MIN_QUESTIONS <= questions <= config.MAX_QUESTIONS:
            self.app.settings["questions"] = str(questions)
        else:
            self.questions_var.set(self.app.settings["questions"])
        self.app.settings["seconds"] = str(self.seconds_var.get())
        self.app.save_settings()

    def reset_progress(self):
        '''Delete XP, history, mistakes and badges of the current player (after asking).'''
        player = self.app.player
        if not messagebox.askyesno("Reset progress", "Really delete ALL progress of " + player.name + "?\n"
                                   "XP, history, weak shortcuts and badges will be lost."):
            return
        try:
            fresh = storage.reset_player_progress(player)
        except OSError as error:
            messagebox.showerror("Reset failed", "Could not reset the progress:\n" + str(error))
            return
        self.app.set_player(fresh)
        messagebox.showinfo("Reset progress", "Your progress was reset. Good luck from level 1!")
