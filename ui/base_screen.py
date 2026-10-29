'''
base_screen.py - the parent class of every screen (PPT 1.5: inheritance).

Every screen of the app is a class that inherits from Screen:
    class HomeScreen(Screen), class QuizScreen(Screen), ...   -> hierarchical inheritance
Every screen overrides build() and on_show()                 -> method overriding
'''

import tkinter as tk

import config
from ui.widgets import HoverButton


class Screen(tk.Frame):
    '''Base class for all screens. A screen is a tk.Frame that fills the main window.'''

    def __init__(self, parent, app):
        '''Create the frame, remember the App controller and build the widgets.'''
        super().__init__(parent, bg=app.colors["bg"])
        self.app = app                  # the App controller (main.py)
        self.colors = app.colors        # the current theme dictionary
        self.build()

    def build(self):
        '''Create all widgets of the screen. Every child class overrides this.'''
        pass

    def on_show(self, **data):
        '''Called every time the screen becomes visible. **data carries extra values.'''
        pass

    def on_hide(self):
        '''Called when the screen is hidden (stop timers, animations, ...).'''
        pass

    # ---------------------------------------------------------------- small helpers

    def make_header(self, title, subtitle=""):
        '''Create the top bar with a "Home" button, a title and an optional subtitle.'''
        bar = tk.Frame(self, bg=self.colors["panel"])
        bar.pack(side="top", fill="x")
        back = HoverButton(bar, "←  Home", lambda: self.app.show_screen("home"),
                           self.colors, kind="secondary")
        back.pack(side="left", padx=12, pady=10)
        title_label = tk.Label(bar, text=title, font=config.FONT_MEDIUM,
                               bg=self.colors["panel"], fg=self.colors["text"])
        title_label.pack(side="left", padx=10)
        if subtitle != "":
            tk.Label(bar, text=subtitle, font=config.FONT_NORMAL, bg=self.colors["panel"],
                     fg=self.colors["subtext"]).pack(side="left", padx=4)
        return bar

    def make_label(self, parent, text, font=config.FONT_NORMAL, color="text", bg="bg", **options):
        '''Create a tk.Label with theme colours (color and bg are keys of the theme).'''
        return tk.Label(parent, text=text, font=font, fg=self.colors[color],
                        bg=self.colors[bg], **options)

    def make_card(self, parent, padx=16, pady=12):
        '''Create a panel-coloured frame (a "card") with inner padding.'''
        return tk.Frame(parent, bg=self.colors["panel"], padx=padx, pady=pady)
