'''
config.py - all fixed settings (constants) of the Shortcut Trainer Quiz app.

Colours, fonts, window size, timer defaults and the paths of the save files are
kept here in one place, so every other file can simply do "import config".
'''

import os

# Global variable (PPT 1.4: local and global variables).
# APP_VERSION is created outside every function, so it is a GLOBAL variable and
# every function of every file can read it as config.APP_VERSION.
APP_VERSION = "1.0"
APP_TITLE = "Shortcut Trainer Quiz"

# ---------------- window size ----------------
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
MIN_WIDTH = 960
MIN_HEIGHT = 600

# ---------------- colour themes (dictionaries) ----------------
DARK_THEME = {
    "name": "dark",
    "bg": "#14161f",          # main window background
    "panel": "#1d2030",       # cards / panels
    "panel_alt": "#262a3d",   # lighter panel (hover, rows)
    "text": "#eef0f8",        # normal text
    "subtext": "#9aa1bd",     # grey helper text
    "accent": "#6c63ff",      # main purple-blue colour
    "accent_hover": "#8a83ff",
    "success": "#2ecc71",     # correct answer (green)
    "warning": "#f5b041",     # yellow
    "danger": "#e74c3c",      # wrong answer (red)
    "key_bg": "#2c3148",      # key cap background
    "key_text": "#ffffff",
    "key_border": "#4b5275",
    "held": "#3498db",        # keys currently held (blue)
    "entry_bg": "#262a3d",
    "chart_bg": "#1d2030",
}

LIGHT_THEME = {
    "name": "light",
    "bg": "#f2f4fa",
    "panel": "#ffffff",
    "panel_alt": "#e6e9f4",
    "text": "#1d2030",
    "subtext": "#5d6585",
    "accent": "#5a52e0",
    "accent_hover": "#7a73f0",
    "success": "#27ae60",
    "warning": "#e09b1f",
    "danger": "#d64333",
    "key_bg": "#ffffff",
    "key_text": "#1d2030",
    "key_border": "#b7bdd6",
    "held": "#2e86de",
    "entry_bg": "#ffffff",
    "chart_bg": "#ffffff",
}

THEMES = {"dark": DARK_THEME, "light": LIGHT_THEME}

# Colours a player can choose for the avatar (tuple = fixed list, cannot change).
AVATAR_COLORS = ("#6c63ff", "#e74c3c", "#2ecc71", "#f39c12", "#1abc9c", "#e84393", "#0984e3")

# ---------------- fonts: tuples (family, size, weight) like the slides ----------------
FONT_FAMILY = "Segoe UI"
FONT_SMALL = (FONT_FAMILY, 9)
FONT_NORMAL = (FONT_FAMILY, 11)
FONT_BOLD = (FONT_FAMILY, 11, "bold")
FONT_MEDIUM = (FONT_FAMILY, 14, "bold")
FONT_LARGE = (FONT_FAMILY, 22, "bold")
FONT_HUGE = (FONT_FAMILY, 40, "bold")
FONT_KEY = ("Consolas", 14, "bold")
FONT_MONO = ("Consolas", 10)

# ---------------- quiz defaults ----------------
DIFFICULTY_LEVELS = ("all", "easy", "medium", "hard")   # tuple: fixed values
DEFAULT_QUESTIONS = 10
MIN_QUESTIONS = 5
MAX_QUESTIONS = 50
DEFAULT_SECONDS = 20
MIN_SECONDS = 5
MAX_SECONDS = 60
SPEED_RUN_SECONDS = 60
DAILY_QUESTIONS = 10
LIVES = 3
CHORD_TIMEOUT = 1.5          # seconds to wait for the 2nd step of a chord like "Ctrl+K, Ctrl+C"
NEXT_QUESTION_DELAY = 1200   # milliseconds before the next question appears

# points (used by core.quiz_engine.calculate_points)
POINTS_CORRECT = 10
POINTS_STREAK_BONUS = 20     # given every 5 correct answers in a row
HINT_PENALTY = 3

# ---------------- files and folders ----------------
# os.path is used so the paths work no matter from which folder the app is started.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVES_DIR = os.path.join(BASE_DIR, "saves")
PLAYERS_FILE = "players.csv"
HISTORY_FILE = "history.csv"
MISTAKES_FILE = "mistakes.csv"
SETTINGS_FILE = "settings.csv"
ACHIEVEMENTS_FILE = "achievements.csv"
SOFTWARE_RESULTS_FILE = "software_results.csv"

# default settings (dictionary) - used when settings.csv does not exist yet
DEFAULT_SETTINGS = {
    "theme": "dark",
    "sound": "on",
    "seconds": str(DEFAULT_SECONDS),
    "questions": str(DEFAULT_QUESTIONS),
}
