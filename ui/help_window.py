'''
help_window.py - Toplevel windows (PPT 3.5: TopLevel, ScrolledText) for
"How to Play", "Shortcut Format Guide" and "About".
'''

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import config

HOW_TO_PLAY = [
    ("Welcome!", "Shortcut Trainer Quiz teaches keyboard shortcuts of Windows and 20 popular "
     "programs. Pick software on the home screen or in Custom Quiz, choose a mode and start."),
    ("Guess the Action", "You see a shortcut as key caps, e.g. [Ctrl] + [Shift] + [N]. Choose what "
     "it does from 4 answers. You can also press the keys 1-4."),
    ("Guess the Shortcut", "You see an action, e.g. 'Create a new folder'. Choose the right key "
     "combination from 4 answers."),
    ("Press the Keys", "You see an action and you really press the shortcut on your keyboard. "
     "The app detects it with Tkinter key events and lights up the keys on the on-screen keyboard. "
     "For chords like 'Ctrl+K, Ctrl+C' press the first combo, release, then press the second one "
     "within 1.5 seconds."),
    ("Speed Run", "60 seconds, mixed questions. Answer as many as you can!"),
    ("Daily Challenge", "10 questions that are the same for everybody today. Only your first try "
     "of the day counts on the leaderboard."),
    ("Revise Weak Shortcuts", "Questions made from the shortcuts you got wrong most often. Every "
     "correct answer lowers the 'weak' counter, every wrong answer raises it."),
    ("Points", "Correct answer = 10 points + the seconds left on the timer. A hint costs 3 points. "
     "Every 5 correct answers in a row give +20 bonus points. Wrong or skipped = 0. "
     "You earn XP = points / 2, and every 100 XP is a new level."),
    ("Lives mode", "With 'Lives mode' you have 3 hearts. A wrong answer, a skip or a time-out "
     "costs one heart. When all hearts are gone, the quiz ends."),
    ("Useful keys", "F11 = full screen.  Keys 1-4 choose an MCQ answer.  "
     "Right-click on the home screen for a quick menu."),
]

FORMAT_GUIDE = [
    ("Modifier keys", "Ctrl, Alt, Shift and Win (the Windows logo key) are held down while you "
     "press the main key. In this app they are always written in the order Ctrl, Alt, Shift, Win. "
     "So the Windows shortcut 'Win+Ctrl+D' is written 'Ctrl+Win+D'."),
    ("The plus sign", "'Ctrl+Shift+N' means: hold Ctrl and Shift, then press N."),
    ("Chords (two steps)", "'Ctrl+K, Ctrl+C' (with a comma) means: press Ctrl+K, let go, then press "
     "Ctrl+C. Gmail uses chords like 'G, I' (press G, then I)."),
    ("Special key names", "Esc, Tab, Enter, Space, Backspace, Delete, Insert, Home, End, PageUp, "
     "PageDown, Up, Down, Left, Right, F1-F12, PrtScn, CapsLock and Numpad 0-9."),
    ("The = / + key", "The key next to Backspace is written '='. 'Ctrl+=' is the usual 'Ctrl+Plus' "
     "(zoom in). When you press the keys, Ctrl+Plus and Ctrl+Numpad + are also accepted."),
    ("Symbols", "Symbols are written with the keys you really press on a US keyboard: "
     "'#' = Shift+3, '?' = Shift+/, '>' = Shift+. and '*' = Shift+8."),
    ("Why some shortcuts are MCQ only", "Windows itself catches shortcuts with the Win key, "
     "Alt+Tab, Alt+F4, Ctrl+Alt+Delete, Ctrl+Shift+Esc, PrtScn and a few more. If you pressed them, "
     "Windows would react (lock the PC, switch windows...) and our app would never see them. "
     "Numpad shortcuts are also MCQ only, because many laptops have no number pad."),
]

ABOUT = [
    ("Shortcut Trainer Quiz", "Version " + config.APP_VERSION + "  -  a desktop app to learn and "
     "practise keyboard shortcuts."),
    ("Project details", "Student Name: ________\nCourse: MCA, Semester 1\n"
     "Subject: Python Programming (26CAH-606)"),
    ("Technologies used", "Python 3, Tkinter + ttk (GUI and key detection), "
     "Matplotlib (charts), NumPy and pandas (statistics), csv, random, datetime, threading, queue."),
    ("Note", "Software names are only shown as text and self-drawn coloured badges. No logos are used."),
]


class HelpWindow(tk.Toplevel):
    '''A Toplevel window with a scrollable help text (inherits from tk.Toplevel).'''

    def __init__(self, root, colors, title, sections):
        '''Create the window and fill it with (heading, text) sections.'''
        super().__init__(root)
        self.title(title)
        self.geometry("640x520")
        self.configure(bg=colors["bg"])
        self.transient(root)                   # stays on top of the main window
        text = ScrolledText(self, wrap="word", font=config.FONT_NORMAL, bg=colors["panel"],
                            fg=colors["text"], relief="flat", padx=18, pady=14)
        text.pack(fill="both", expand=True, padx=12, pady=(12, 6))
        text.tag_configure("heading", font=config.FONT_MEDIUM, foreground=colors["accent"])
        for heading, body in sections:
            text.insert("end", heading + "\n", "heading")
            text.insert("end", body + "\n\n")
        text.config(state="disabled")          # read-only
        tk.Button(self, text="Close", command=self.destroy, bg=colors["accent"], fg="white",
                  relief="flat", font=config.FONT_BOLD, padx=20).pack(pady=(0, 12))
        self.bind("<Escape>", lambda event: self.destroy())
        self.focus_set()


def open_help(root, colors, topic):
    '''Open the help window for a topic: "how", "format" or "about".'''
    if topic == "how":
        HelpWindow(root, colors, "How to Play", HOW_TO_PLAY)
    elif topic == "format":
        HelpWindow(root, colors, "Shortcut Format Guide", FORMAT_GUIDE)
    else:
        HelpWindow(root, colors, "About", ABOUT)
