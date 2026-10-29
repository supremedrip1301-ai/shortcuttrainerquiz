'''
login_screen.py - choose an existing player (Listbox + Scrollbar) or create a new one
(Entry for the name, Radiobuttons for the avatar colour, optional PIN).
Players are saved in saves/players.csv.
'''

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

import config
from core import storage
from core.models import Player
from ui.base_screen import Screen
from ui.widgets import HoverButton, make_entry


class LoginScreen(Screen):
    '''Player selection and creation (inherits from Screen).'''

    def build(self):
        '''Create the two panels: existing players and new player (method overriding).'''
        self.players = {}
        self.make_label(self, config.APP_TITLE, config.FONT_LARGE).pack(pady=(40, 0))
        self.make_label(self, "Who is playing today?", config.FONT_MEDIUM, "subtext").pack(pady=(4, 24))
        row = tk.Frame(self, bg=self.colors["bg"])
        row.pack()
        self.build_player_list(row)
        self.build_new_player(row)

    def build_player_list(self, parent):
        '''Left card: Listbox of saved players with a Scrollbar and a Continue button.'''
        card = self.make_card(parent, 22, 18)
        card.pack(side="left", padx=14, anchor="n")
        self.make_label(card, "Existing players", config.FONT_MEDIUM, bg="panel").pack(anchor="w")
        box = tk.Frame(card, bg=self.colors["panel"])
        box.pack(pady=10)
        scrollbar = ttk.Scrollbar(box, orient="vertical")
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(box, width=28, height=10, font=config.FONT_NORMAL,
                                  bg=self.colors["entry_bg"], fg=self.colors["text"],
                                  selectbackground=self.colors["accent"], selectforeground="white",
                                  relief="flat", highlightthickness=0, yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left")
        scrollbar.config(command=self.listbox.yview)
        self.listbox.bind("<Double-Button-1>", lambda event: self.continue_player())
        self.listbox.bind("<<ListboxSelect>>", self.show_player_info)
        self.info_label = self.make_label(card, "Select your name and press Continue.",
                                          config.FONT_SMALL, "subtext", "panel")
        self.info_label.pack(anchor="w")
        HoverButton(card, "Continue  →", self.continue_player, self.colors).pack(fill="x", pady=(10, 0))

    def build_new_player(self, parent):
        '''Right card: name Entry, avatar colour Radiobuttons, optional PIN, New Player button.'''
        card = self.make_card(parent, 22, 18)
        card.pack(side="left", padx=14, anchor="n")
        self.make_label(card, "New player", config.FONT_MEDIUM, bg="panel").pack(anchor="w")
        self.make_label(card, "Your name", config.FONT_NORMAL, "subtext", "panel").pack(anchor="w", pady=(10, 2))
        self.name_var = tk.StringVar()
        self.name_entry = make_entry(card, self.colors, 26, textvariable=self.name_var)
        self.name_entry.pack(anchor="w", ipady=4)
        self.name_entry.bind("<KeyRelease>", lambda event: self.draw_preview())
        self.name_entry.bind("<Return>", lambda event: self.new_player())
        self.make_label(card, "Avatar colour", config.FONT_NORMAL, "subtext", "panel").pack(anchor="w", pady=(12, 2))
        colors_row = tk.Frame(card, bg=self.colors["panel"])
        colors_row.pack(anchor="w")
        self.avatar_var = tk.StringVar(value=config.AVATAR_COLORS[0])
        for color in config.AVATAR_COLORS:
            # a Radiobutton without the round indicator looks like a coloured square button
            tk.Radiobutton(colors_row, variable=self.avatar_var, value=color, indicatoron=0,
                           width=2, bg=color, selectcolor=color, activebackground=color,
                           relief="flat", offrelief="flat", bd=3, cursor="hand2",
                           command=self.draw_preview).pack(side="left", padx=3)
        self.preview = tk.Canvas(card, width=70, height=70, bg=self.colors["panel"], highlightthickness=0)
        self.preview.pack(pady=10)
        self.make_label(card, "PIN (optional, 4 digits)", config.FONT_NORMAL, "subtext", "panel").pack(anchor="w")
        self.pin_entry = make_entry(card, self.colors, 10, show="*")
        self.pin_entry.pack(anchor="w", ipady=4)
        HoverButton(card, "New Player  ✓", self.new_player, self.colors, kind="success").pack(fill="x", pady=(14, 0))
        self.draw_preview()

    def on_show(self, **data):
        '''Remove the menubar and reload the list of players (method overriding).'''
        self.app.root.config(menu="")
        self.players = storage.load_players()
        self.listbox.delete(0, "end")
        for name in sorted(self.players.keys(), key=lambda n: n.lower()):
            self.listbox.insert("end", name)
        if len(self.players) == 0:
            self.info_label.config(text="No players yet. Create one on the right!")
        self.name_entry.focus_set()

    def draw_preview(self):
        '''Draw the avatar preview: a coloured circle with the first letter of the name.'''
        self.preview.delete("all")
        name = self.name_var.get().strip()
        if name == "":
            letter = "?"
        else:
            letter = name[0].upper()
        self.preview.create_oval(5, 5, 65, 65, fill=self.avatar_var.get(), outline="")
        self.preview.create_text(35, 35, text=letter, fill="white", font=config.FONT_LARGE)

    def show_player_info(self, event=None):
        '''Show level and streak of the selected player.'''
        selection = self.listbox.curselection()
        if len(selection) == 0:
            return
        player = self.players[self.listbox.get(selection[0])]
        self.info_label.config(text="Level %d  |  %d XP  |  streak %d day(s)"
                               % (player.get_level(), player.get_xp(), player.streak))

    def continue_player(self):
        '''Log in with the selected player (asks for the PIN if one was set).'''
        selection = self.listbox.curselection()
        if len(selection) == 0:
            messagebox.showwarning("No player selected", "Please select your name in the list first.")
            return
        player = self.players[self.listbox.get(selection[0])]
        if player.has_pin():
            pin = simpledialog.askstring("PIN", "Enter the PIN for " + player.name + ":",
                                         show="*", parent=self)
            if pin is None:
                return
            if not player.check_pin(pin):
                messagebox.showerror("Wrong PIN", "Sorry, that PIN is not correct.")
                return
        self.login(player)

    def new_player(self):
        '''Check the typed name and PIN, create the player and log in.'''
        name = self.name_var.get().strip()
        pin = self.pin_entry.get().strip()
        if name == "":
            messagebox.showwarning("Name missing", "Please type your name.")
            return
        if len(name) > 20:
            messagebox.showwarning("Name too long", "Please use at most 20 characters.")
            return
        if name.lower() in [n.lower() for n in self.players]:
            messagebox.showwarning("Name used", "This name already exists. Select it in the list.")
            return
        if pin != "" and (len(pin) != 4 or not pin.isdigit()):
            messagebox.showwarning("PIN", "The PIN must be exactly 4 digits (or empty).")
            return
        player = Player(name, self.avatar_var.get(), 0, pin)
        self.app.set_player(player)
        self.app.save_player()
        self.name_var.set("")
        self.pin_entry.delete(0, "end")
        self.login(player)

    def login(self, player):
        '''Remember the player and open the home screen.'''
        self.app.set_player(player)
        self.app.show_screen("home")
