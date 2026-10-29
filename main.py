'''
main.py - entry point of the Shortcut Trainer Quiz app.

Run it with:   python main.py

It creates the main window (tk.Tk), builds the App controller and starts mainloop().
The App class keeps a dictionary of screens and switches between them with
show_screen(name, **data). Only one screen is visible at a time:
    the old screen is hidden with pack_forget() and the new one is shown with pack().
'''

import queue
import tkinter as tk
import traceback
from tkinter import messagebox, ttk

import config
from core import quiz_engine, storage
from data.shortcuts import get_all_software_names
from ui import help_window
from ui.achievements_screen import AchievementsScreen
from ui.home_screen import HomeScreen
from ui.leaderboard_screen import LeaderboardScreen
from ui.learn_screen import LearnScreen
from ui.login_screen import LoginScreen
from ui.quiz_screen import QuizScreen
from ui.quiz_setup_screen import QuizSetupScreen
from ui.results_screen import ResultsScreen
from ui.settings_screen import SettingsScreen
from ui.splash_screen import SplashScreen
from ui.stats_screen import StatsScreen
from ui.widgets import Toast


class App:
    '''The controller: creates the screens, switches between them and keeps the shared state.'''

    # screen name -> screen class (every class inherits from ui.base_screen.Screen)
    SCREEN_CLASSES = {
        "splash": SplashScreen,
        "login": LoginScreen,
        "home": HomeScreen,
        "learn": LearnScreen,
        "quiz_setup": QuizSetupScreen,
        "quiz": QuizScreen,
        "results": ResultsScreen,
        "stats": StatsScreen,
        "leaderboard": LeaderboardScreen,
        "achievements": AchievementsScreen,
        "settings": SettingsScreen,
    }

    # screens that can be shown again directly after the theme changes
    REBUILD_SAFE = ("home", "settings", "learn", "stats", "leaderboard", "achievements",
                    "quiz_setup")

    def __init__(self, root):
        '''Load the settings, prepare the shared objects and show the splash screen.'''
        self.root = root
        self.settings = storage.load_settings()
        self.colors = config.THEMES.get(self.settings["theme"], config.DARK_THEME)
        self.player = None                      # the Player object after login
        self.key_queue = queue.Queue()          # key messages from the Tkinter key reader
        self.screens = {}                       # dictionary: name -> Screen object
        self.current_name = ""
        self.last_quiz = None                   # settings of the last quiz (for "Play Again")
        self.is_fullscreen = False
        self.style = ttk.Style(root)
        # NOTE (advanced): this shows a friendly message instead of a traceback if any
        # button command fails unexpectedly; the app keeps running.
        root.report_callback_exception = self.report_error
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)
        self.apply_theme_colors()
        root.bind("<F11>", self.toggle_fullscreen)
        self.show_screen("splash")

    # ---------------------------------------------------------------- screens

    def get_screen(self, name):
        '''Return the screen object; it is created the first time it is needed.'''
        if name not in self.screens:
            screen_class = self.SCREEN_CLASSES[name]
            self.screens[name] = screen_class(self.container, self)
        return self.screens[name]

    def show_screen(self, name, **data):
        '''Hide the current screen and show another one. **data is passed to on_show().'''
        if name not in self.SCREEN_CLASSES:
            messagebox.showinfo("Not available", "This part of the app is not available yet.")
            return
        if self.current_name == "quiz" and name != "results":
            if self.screens["quiz"].is_running():
                if not messagebox.askyesno("Leave quiz", "Leave the quiz? This quiz will not be saved."):
                    return
        if self.current_name in self.screens:
            old_screen = self.screens[self.current_name]
            old_screen.on_hide()
            old_screen.pack_forget()            # hide the old frame (it is not destroyed)
        screen = self.get_screen(name)
        self.current_name = name
        screen.pack(fill="both", expand=True)   # show the new frame
        screen.on_show(**data)

    def rebuild_screens(self):
        '''Destroy all screens, so they are built again with the new colours.'''
        self.root.config(menu="")
        for screen in self.screens.values():
            screen.on_hide()
            screen.destroy()
        self.screens = {}
        self.current_name = ""

    # ---------------------------------------------------------------- theme and window

    def apply_theme_colors(self):
        '''Give the ttk widgets (Treeview, Combobox, Progressbar ...) the theme colours.'''
        c = self.colors
        style = self.style
        style.theme_use("clam")
        style.configure(".", background=c["bg"], foreground=c["text"], fieldbackground=c["entry_bg"],
                        font=config.FONT_NORMAL, bordercolor=c["key_border"])
        style.configure("Treeview", background=c["panel"], fieldbackground=c["panel"],
                        foreground=c["text"], rowheight=26, borderwidth=0)
        style.configure("Treeview.Heading", background=c["panel_alt"], foreground=c["text"],
                        font=config.FONT_BOLD, relief="flat")
        style.map("Treeview", background=[("selected", c["accent"])], foreground=[("selected", "white")])
        style.configure("TCombobox", fieldbackground=c["entry_bg"], background=c["panel_alt"],
                        foreground=c["text"], arrowcolor=c["text"], lightcolor=c["entry_bg"],
                        darkcolor=c["entry_bg"], padding=3)
        style.map("TCombobox", fieldbackground=[("readonly", c["entry_bg"])],
                  foreground=[("readonly", c["text"])], selectbackground=[("readonly", c["entry_bg"])],
                  selectforeground=[("readonly", c["text"])])
        style.configure("TSpinbox", fieldbackground=c["entry_bg"], foreground=c["text"],
                        background=c["panel_alt"], arrowcolor=c["text"])
        style.configure("Horizontal.TProgressbar", troughcolor=c["panel_alt"], background=c["accent"],
                        lightcolor=c["accent"], darkcolor=c["accent"], bordercolor=c["panel_alt"])
        style.configure("Horizontal.TScale", background=c["panel"], troughcolor=c["panel_alt"])
        style.configure("Vertical.TScrollbar", background=c["panel_alt"], troughcolor=c["bg"],
                        arrowcolor=c["text"], bordercolor=c["bg"])
        style.configure("TNotebook", background=c["bg"], borderwidth=0)
        style.configure("TNotebook.Tab", background=c["panel_alt"], foreground=c["text"], padding=(16, 6))
        style.map("TNotebook.Tab", background=[("selected", c["accent"])], foreground=[("selected", "white")])
        # the drop-down list of a Combobox is a normal Listbox, it is styled with option_add
        self.root.option_add("*TCombobox*Listbox.background", c["panel"])
        self.root.option_add("*TCombobox*Listbox.foreground", c["text"])
        self.root.configure(bg=c["bg"])
        self.container.configure(bg=c["bg"])

    def set_theme(self, theme_name):
        '''Switch between the dark and the light theme and rebuild the screens.'''
        if self.current_name == "quiz":
            messagebox.showinfo("Theme", "Please finish the quiz first, then change the theme.")
            return
        self.settings["theme"] = theme_name
        self.save_settings()
        self.colors = config.THEMES[theme_name]
        self.apply_theme_colors()
        current = self.current_name
        self.rebuild_screens()
        if current in self.REBUILD_SAFE and current in self.SCREEN_CLASSES:
            self.show_screen(current)
        else:
            self.show_screen("home")

    def toggle_fullscreen(self, event=None):
        '''F11: switch full-screen mode on or off.'''
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)

    def show_toast(self, title, message, color=None):
        '''Show a small popup at the bottom-right corner for 2.5 seconds.'''
        if color is None:
            color = self.colors["accent"]
        Toast(self.root, title, message, color)

    def report_error(self, error_type, error_value, error_traceback):
        '''Show unexpected errors in simple language (details are printed in the console).'''
        traceback.print_exception(error_type, error_value, error_traceback)
        messagebox.showerror("Something went wrong",
                             "Sorry, something unexpected happened:\n" + str(error_value) +
                             "\n\nThe app will keep running.")

    # ---------------------------------------------------------------- player and settings

    def set_player(self, player):
        '''Remember the player who logged in.'''
        self.player = player

    def save_player(self):
        '''Save the current player to players.csv (shows an error if the file is locked).'''
        try:
            storage.save_player(self.player)
        except OSError as error:
            messagebox.showerror("Save error", "Could not save the player:\n" + str(error))

    def save_settings(self):
        '''Save the settings dictionary to settings.csv.'''
        try:
            storage.save_settings(self.settings)
        except OSError as error:
            messagebox.showerror("Save error", "Could not save the settings:\n" + str(error))

    def sound_on(self):
        '''True when feedback sounds are switched on.'''
        return self.settings["sound"] == "on"

    # ---------------------------------------------------------------- starting quizzes

    def start_quiz(self, questions, mode, software_list, seconds=None, lives=False, practice=False):
        '''Create a QuizSession and open the quiz screen.'''
        if len(questions) == 0:
            messagebox.showinfo("No questions", "There are no questions for this selection.")
            return
        if seconds is None:
            seconds = int(self.settings["seconds"])
        session = quiz_engine.QuizSession(questions, mode, software_list, seconds, lives)
        self.show_screen("quiz", session=session, practice=practice)

    def start_from_settings(self, quiz_settings):
        '''Start a quiz from a settings dictionary (used by Quiz Setup and "Play Again").'''
        self.last_quiz = quiz_settings
        mode = quiz_settings["mode"]
        if mode == "daily":
            self.start_daily_challenge()
        elif mode == "revise":
            self.start_revise()
        elif mode == "speed":
            session = quiz_engine.SpeedRunSession(quiz_settings["software_list"], quiz_settings["difficulty"])
            self.show_screen("quiz", session=session, practice=False)
        else:
            questions = quiz_engine.generate_questions(quiz_settings["software_list"], quiz_settings["count"],
                                                       quiz_settings["difficulty"], mode)
            self.start_quiz(questions, mode, quiz_settings["software_list"],
                            quiz_settings["seconds"], quiz_settings["lives"])

    def start_quick_quiz(self):
        '''10 mixed MCQ questions from all software.'''
        software_list = get_all_software_names()
        self.last_quiz = {"mode": "mixed", "software_list": software_list, "difficulty": "all",
                          "count": 10, "seconds": int(self.settings["seconds"]), "lives": False}
        self.start_from_settings(self.last_quiz)

    def start_daily_challenge(self):
        '''Today's 10 fixed questions. Only the first try of the day counts for the leaderboard.'''
        practice = storage.daily_done_today(self.player.name)
        if practice:
            if not messagebox.askyesno("Daily Challenge", "You already finished today's challenge.\n"
                                       "Play it again as practice? (It will not count again.)"):
                return
        self.last_quiz = {"mode": "daily"}
        questions = quiz_engine.generate_daily_questions()
        self.start_quiz(questions, "daily", get_all_software_names(), practice=practice)

    def start_revise(self):
        '''Questions from the shortcuts this player got wrong most often.'''
        weak = storage.load_mistakes(self.player.name)
        if len(weak) == 0:
            messagebox.showinfo("Revise", "You have no weak shortcuts yet.\nPlay some quizzes first!")
            return
        self.last_quiz = {"mode": "revise"}
        questions = quiz_engine.generate_revise_questions(weak, int(self.settings["questions"]))
        software_list = sorted(set([q.shortcut.software for q in questions]))
        self.start_quiz(questions, "revise", software_list)

    def replay_last_quiz(self):
        '''"Play Again" on the results screen.'''
        if self.last_quiz is None:
            self.show_screen("quiz_setup")
        else:
            self.start_from_settings(self.last_quiz)

    # ---------------------------------------------------------------- help and closing

    def open_help(self, topic):
        '''Open a help window: "how", "format" or "about".'''
        help_window.open_help(self.root, self.colors, topic)

    def on_close(self):
        '''Ask before closing (so an accidental Alt+F4 does not close the app at once).'''
        if not messagebox.askyesno("Quit", "Do you really want to quit?"):
            return
        if self.current_name in self.screens:
            self.screens[self.current_name].on_hide()
        self.root.destroy()


def center_window(root, width, height):
    '''Put the window in the middle of the screen using a "WxH+X+Y" geometry string.'''
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # on small screens (or with 150% Windows scaling) the window is made smaller to fit
    width = min(width, screen_width - 40)
    height = min(height, screen_height - 90)
    x = (screen_width - width) // 2
    y = max(0, (screen_height - height) // 2 - 30)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))


def main():
    '''Create the main window, the App controller and start the event loop.'''
    # creating tkinter window
    root = tk.Tk()
    root.title(config.APP_TITLE)
    center_window(root, config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    root.minsize(min(config.MIN_WIDTH, root.winfo_screenwidth() - 40),
                 min(config.MIN_HEIGHT, root.winfo_screenheight() - 90))
    if root.winfo_screenheight() < 800:
        root.state("zoomed")              # small screen: start maximized to use all the space
    app = App(root)
    # ask "Do you really want to quit?" when the window is closed
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    # Entering the event main loop
    root.mainloop()


if __name__ == "__main__":
    main()
