'''
learn_screen.py - Learn mode with two tabs (ttk.Notebook):

1. Cheat Sheet : a searchable Treeview of all shortcuts (search Entry + filter Comboboxes)
2. Flashcards  : a big card shows the action; click or press Space to flip and see the keys

export_cheat_sheet() writes a neat .txt file (also used by File > Export Cheat Sheet).
'''

import datetime
import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import config
from core import key_utils
from data.shortcuts import SOFTWARE_INFO, combine_shortcuts, get_all_software_names, get_display_name, get_shortcuts
from ui.base_screen import Screen
from ui.widgets import HoverButton, make_entry

ALL_SOFTWARE_TEXT = "All software"
ALL_CATEGORIES_TEXT = "All categories"


def export_cheat_sheet(parent, software_keys=None):
    '''Ask for a file name and write a text cheat sheet with one section per software.'''
    if software_keys is None:
        software_keys = get_all_software_names()
    path = filedialog.asksaveasfilename(parent=parent, title="Save cheat sheet",
                                        defaultextension=".txt", initialfile="shortcut_cheat_sheet.txt",
                                        filetypes=[("Text file", "*.txt"), ("All files", "*.*")])
    if not path:
        return                          # the user pressed Cancel
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(config.APP_TITLE.upper() + " - CHEAT SHEET\n")
            f.write("Created on " + str(datetime.date.today()) + "\n")
            for software_key in software_keys:
                f.write("\n" + "=" * 72 + "\n")
                f.write(get_display_name(software_key).upper() + "\n")
                f.write("=" * 72 + "\n")
                current_category = ""
                for shortcut in get_shortcuts(software_key):
                    if shortcut.category != current_category:
                        current_category = shortcut.category
                        f.write("\n  [" + current_category + "]\n")
                    f.write("  %-26s %s\n" % (shortcut.keys, shortcut.action))
        messagebox.showinfo("Cheat sheet saved", "The cheat sheet was saved to:\n" + path)
    except OSError as error:
        messagebox.showerror("Export failed", "Could not write the file:\n" + str(error))


class LearnScreen(Screen):
    '''Cheat sheet table and flashcards (inherits from Screen).'''

    def build(self):
        '''Create the header and the two notebook tabs (method overriding).'''
        self.make_header("Learn", "search the cheat sheet or practise with flashcards")
        self.all_shortcuts = combine_shortcuts(*get_all_software_names())
        self.name_to_key = {}            # display name -> software key
        for software_key in get_all_software_names():
            self.name_to_key[get_display_name(software_key)] = software_key
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=16, pady=12)
        sheet_tab = tk.Frame(self.notebook, bg=self.colors["bg"])
        card_tab = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.notebook.add(sheet_tab, text="Cheat Sheet")
        self.notebook.add(card_tab, text="Flashcards")
        self.build_cheat_sheet(sheet_tab)
        self.build_flashcards(card_tab)
        self.notebook.bind("<<NotebookTabChanged>>", lambda event: self.card_canvas.focus_set())

    # ---------------------------------------------------------------- cheat sheet tab

    def build_cheat_sheet(self, parent):
        '''Filters on top, a Treeview with a Scrollbar below.'''
        filters = tk.Frame(parent, bg=self.colors["bg"])
        filters.pack(fill="x", pady=(10, 8))
        self.make_label(filters, "Search:").pack(side="left")
        self.search_entry = make_entry(filters, self.colors, 24)
        self.search_entry.pack(side="left", padx=(4, 12), ipady=3)
        self.search_entry.bind("<KeyRelease>", lambda event: self.refresh_table())   # filter while typing
        names = [ALL_SOFTWARE_TEXT] + list(self.name_to_key.keys())
        self.software_box = ttk.Combobox(filters, values=names, state="readonly", width=22, font=config.FONT_NORMAL)
        self.software_box.set(ALL_SOFTWARE_TEXT)
        self.software_box.pack(side="left", padx=4)
        self.software_box.bind("<<ComboboxSelected>>", self.on_software_change)
        self.category_box = ttk.Combobox(filters, values=[ALL_CATEGORIES_TEXT], state="readonly", width=20, font=config.FONT_NORMAL)
        self.category_box.set(ALL_CATEGORIES_TEXT)
        self.category_box.pack(side="left", padx=4)
        self.category_box.bind("<<ComboboxSelected>>", lambda event: self.refresh_table())
        self.difficulty_box = ttk.Combobox(filters, values=["all", "easy", "medium", "hard"],
                                           state="readonly", width=8, font=config.FONT_NORMAL)
        self.difficulty_box.set("all")
        self.difficulty_box.pack(side="left", padx=4)
        self.difficulty_box.bind("<<ComboboxSelected>>", lambda event: self.refresh_table())
        HoverButton(filters, "Export cheat sheet", self.export_current, self.colors).pack(side="right")
        self.count_label = self.make_label(filters, "", config.FONT_SMALL, "subtext")
        self.count_label.pack(side="right", padx=10)
        self.build_table(parent)

    def build_table(self, parent):
        '''Create the Treeview (columns: Software, Shortcut, Action, Category, Difficulty).'''
        box = tk.Frame(parent, bg=self.colors["bg"])
        box.pack(fill="both", expand=True)
        columns = ("software", "keys", "action", "category", "difficulty")
        self.table = ttk.Treeview(box, columns=columns, show="headings")
        headings = ("Software", "Shortcut", "Action", "Category", "Difficulty")
        widths = (150, 170, 380, 150, 90)
        for column, heading, width in zip(columns, headings, widths):
            self.table.heading(column, text=heading)
            self.table.column(column, width=width, anchor="w")
        scrollbar = ttk.Scrollbar(box, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def on_software_change(self, event=None):
        '''A new software was chosen: fill the category list for it.'''
        categories = []
        for shortcut in self.get_filtered_by_software():
            if shortcut.category not in categories:
                categories.append(shortcut.category)
        self.category_box["values"] = [ALL_CATEGORIES_TEXT] + sorted(categories)
        self.category_box.set(ALL_CATEGORIES_TEXT)
        self.refresh_table()

    def get_filtered_by_software(self):
        '''Return the shortcuts of the chosen software (or all).'''
        name = self.software_box.get()
        if name == ALL_SOFTWARE_TEXT:
            return self.all_shortcuts
        return get_shortcuts(self.name_to_key[name])

    def refresh_table(self):
        '''Show only the rows that match the search text and the filters.'''
        text = self.search_entry.get().strip().lower()
        category = self.category_box.get()
        difficulty = self.difficulty_box.get()
        self.table.delete(*self.table.get_children())
        count = 0
        for s in self.get_filtered_by_software():
            if category != ALL_CATEGORIES_TEXT and s.category != category:
                continue
            if difficulty != "all" and s.difficulty != difficulty:
                continue
            searchable = (s.keys + " " + s.action + " " + s.category).lower()
            if text != "" and text not in searchable:
                continue
            self.table.insert("", "end", values=(get_display_name(s.software), s.keys, s.action,
                                                 s.category, s.difficulty))
            count = count + 1
        self.count_label.config(text=str(count) + " shortcuts shown")

    def export_current(self):
        '''Export the chosen software (or all software) to a text file.'''
        name = self.software_box.get()
        if name == ALL_SOFTWARE_TEXT:
            export_cheat_sheet(self)
        else:
            export_cheat_sheet(self, [self.name_to_key[name]])

    # ---------------------------------------------------------------- flashcards tab

    def build_flashcards(self, parent):
        '''A software chooser, the card Canvas and Previous / Flip / Next buttons.'''
        top = tk.Frame(parent, bg=self.colors["bg"])
        top.pack(fill="x", pady=10)
        self.make_label(top, "Cards from:").pack(side="left")
        names = [ALL_SOFTWARE_TEXT] + list(self.name_to_key.keys())
        self.card_software_box = ttk.Combobox(top, values=names, state="readonly", width=24, font=config.FONT_NORMAL)
        self.card_software_box.set(names[1])
        self.card_software_box.pack(side="left", padx=6)
        self.card_software_box.bind("<<ComboboxSelected>>", lambda event: self.load_cards())
        HoverButton(top, "⇄ Shuffle", self.shuffle_cards, self.colors, kind="secondary").pack(side="left", padx=6)
        self.card_count = self.make_label(top, "", config.FONT_NORMAL, "subtext")
        self.card_count.pack(side="right")
        self.card_canvas = tk.Canvas(parent, height=300, bg=self.colors["bg"], highlightthickness=0,
                                     cursor="hand2")
        self.card_canvas.pack(fill="x", padx=60, pady=10)
        self.card_canvas.bind("<Button-1>", lambda event: self.flip_card())
        self.card_canvas.bind("<space>", lambda event: self.flip_card())
        self.card_canvas.bind("<Right>", lambda event: self.move_card(1))
        self.card_canvas.bind("<Left>", lambda event: self.move_card(-1))
        self.card_canvas.bind("<Configure>", lambda event: self.draw_card())
        buttons = tk.Frame(parent, bg=self.colors["bg"])
        buttons.pack()
        HoverButton(buttons, "← Previous", lambda: self.move_card(-1), self.colors, kind="secondary").pack(side="left", padx=6)
        HoverButton(buttons, "Flip (Space)", self.flip_card, self.colors).pack(side="left", padx=6)
        HoverButton(buttons, "Next →", lambda: self.move_card(1), self.colors, kind="secondary").pack(side="left", padx=6)
        self.cards = []
        self.card_index = 0
        self.card_flipped = False
        self.load_cards()

    def load_cards(self):
        '''Load the flashcards for the chosen software.'''
        name = self.card_software_box.get()
        if name == ALL_SOFTWARE_TEXT:
            self.cards = list(self.all_shortcuts)
        else:
            self.cards = get_shortcuts(self.name_to_key[name])
        self.card_index = 0
        self.card_flipped = False
        self.draw_card()

    def shuffle_cards(self):
        '''Mix the cards in a random order (random.shuffle, PPT 1.2).'''
        random.shuffle(self.cards)
        self.card_index = 0
        self.card_flipped = False
        self.draw_card()
        self.card_canvas.focus_set()

    def move_card(self, step):
        '''Go to the next (+1) or previous (-1) card.'''
        if len(self.cards) == 0:
            return
        self.card_index = (self.card_index + step) % len(self.cards)
        self.card_flipped = False
        self.draw_card()
        self.card_canvas.focus_set()

    def flip_card(self):
        '''Turn the card around.'''
        self.card_flipped = not self.card_flipped
        self.draw_card()
        self.card_canvas.focus_set()

    def draw_card(self):
        '''Draw the front (action) or the back (keys) of the current card.'''
        c = self.card_canvas
        c.delete("all")
        if len(self.cards) == 0:
            return
        width = c.winfo_width()
        shortcut = self.cards[self.card_index]
        info = SOFTWARE_INFO.get(shortcut.software, {"color": self.colors["accent"]})
        if self.card_flipped:
            fill = self.colors["accent"]
            text_color = "white"
        else:
            fill = self.colors["panel"]
            text_color = self.colors["text"]
        c.create_rectangle(8, 14, width - 2, 296, fill=self.colors["key_border"], outline="")
        c.create_rectangle(2, 6, width - 8, 288, fill=fill, outline=info["color"], width=4)
        c.create_text(24, 30, text=get_display_name(shortcut.software) + "  |  " + shortcut.category,
                      anchor="w", fill=text_color, font=config.FONT_NORMAL)
        if self.card_flipped:
            c.create_text(width / 2, 130, text=key_utils.format_combo_for_display(shortcut.keys),
                          fill="white", font=("Consolas", 30, "bold"), width=width - 60)
            c.create_text(width / 2, 210, text=shortcut.action, fill="white", font=config.FONT_MEDIUM,
                          width=width - 60)
        else:
            c.create_text(width / 2, 140, text=shortcut.action, fill=text_color, font=config.FONT_LARGE,
                          width=width - 80)
            c.create_text(width / 2, 255, text="Click or press Space to see the shortcut",
                          fill=self.colors["subtext"], font=config.FONT_SMALL)
        self.card_count.config(text="Card %d / %d" % (self.card_index + 1, len(self.cards)))

    # ---------------------------------------------------------------- showing

    def on_show(self, **data):
        '''Fill the table the first time and put the cursor in the search box.'''
        if len(self.table.get_children()) == 0:
            self.refresh_table()
        self.search_entry.focus_set()
