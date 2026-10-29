'''
models.py - the main classes (PPT 1.5: classes and objects) of the project.

Shortcut    : one keyboard shortcut (public attributes only)
Question    : one quiz question made from a Shortcut
Player      : a player profile (public, _protected and __private attributes)
Achievement : one badge that a player can unlock
'''

import datetime

from core import key_utils


class Shortcut:
    '''One keyboard shortcut of one software. All attributes are public.'''

    def __init__(self, software, keys, action, category, difficulty, mode):
        '''Store the six details of a shortcut (like the Person class of the slides).'''
        self.software = software        # public attribute, e.g. "vs_code"
        self.keys = keys                # e.g. "Ctrl+Shift+P"
        self.action = action            # e.g. "Show the Command Palette"
        self.category = category        # e.g. "General"
        self.difficulty = difficulty    # "easy", "medium" or "hard"
        self.mode = mode                # "press" or "mcq"

    def can_be_pressed(self):
        '''Return True if this shortcut may be pressed inside our window.'''
        return self.mode == "press"

    def display(self):
        '''Print the shortcut (same idea as Employee.display() in the slides).'''
        print("Software: %s \nKeys: %s \nAction: %s" % (self.software, self.keys, self.action))


def make_shortcut(software, data):
    '''Create a Shortcut object from one dictionary of a data file.'''
    return Shortcut(software, data["keys"], data["action"], data["category"],
                    data["difficulty"], data["mode"])


class Question:
    '''One quiz question. kind is "action" (guess the action), "shortcut" (guess the combo) or "press".'''

    def __init__(self, shortcut, kind, options=None, correct_index=0):
        '''Create a question for the given Shortcut object.'''
        self.shortcut = shortcut
        self.kind = kind
        if options is None:          # a list must not be used as a default argument directly
            options = []
        self.options = options       # list of 4 strings for MCQ questions
        self.correct_index = correct_index
        # these are filled while the user plays
        self.user_answer = ""
        self.answered = False
        self.is_correct = False
        self.skipped = False
        self.used_hint = False
        self.points = 0

    def get_prompt_text(self):
        '''Return the question sentence that is shown on the quiz screen.'''
        if self.kind == "action":
            return "What does this shortcut do?"
        elif self.kind == "shortcut":
            return "Which shortcut does this:  " + self.shortcut.action + " ?"
        else:
            return "Press the keys for:  " + self.shortcut.action

    def get_correct_answer_text(self):
        '''Return the correct answer as text (action or key combo).'''
        if self.kind == "action":
            return self.shortcut.action
        return self.shortcut.keys

    def check_option(self, index):
        '''Check an MCQ answer (index 0-3). Saves and returns True/False.'''
        self.answered = True
        self.user_answer = self.options[index]
        self.is_correct = (index == self.correct_index)
        return self.is_correct

    def check_combo(self, combo_text):
        '''Check a pressed key combo for a "press" question. Saves and returns True/False.'''
        self.answered = True
        self.user_answer = combo_text
        self.is_correct = key_utils.combos_match(combo_text, self.shortcut.keys)
        return self.is_correct

    def mark_skipped(self, reason="Skipped"):
        '''Mark this question as skipped (or timed out).'''
        self.answered = True
        self.skipped = True
        self.is_correct = False
        self.user_answer = reason


class Player:
    '''A player profile. Shows public, _protected and __private attributes (PPT 1.5).'''

    def __init__(self, name, avatar="#6c63ff", xp=0, pin="", streak=0, last_played="",
                 quizzes=0, best_streak=0, fixed_count=0, created=""):
        '''Create a player. Numbers may come from a CSV file as text, so int() is used.'''
        self.name = name                    # public attribute
        self.avatar = avatar                # public attribute (colour)
        self._xp = int(xp)                  # protected attribute (use add_xp / get_xp)
        self.__pin = str(pin)               # private attribute (name mangling: _Player__pin)
        self.streak = int(streak)           # days played in a row
        self.last_played = last_played      # "YYYY-MM-DD" text
        self.quizzes = int(quizzes)
        self.best_streak = int(best_streak)  # best "correct in a row" ever
        self.fixed_count = int(fixed_count)  # weak shortcuts fixed in revise mode
        if created == "":
            created = str(datetime.date.today())
        self.created = created

    def add_xp(self, *points):
        '''Add any number of XP values (*args, PPT 1.4). Returns True if the level went up.'''
        old_level = self.get_level()
        for p in points:
            self._xp = self._xp + int(p)
        return self.get_level() > old_level

    def get_xp(self):
        '''Return the total XP (reading the protected attribute through a method).'''
        return self._xp

    def get_level(self):
        '''Level = xp // 100 + 1, so every 100 XP gives one new level.'''
        return self._xp // 100 + 1

    def xp_in_current_level(self):
        '''Return how many XP the player has inside the current level (0-99).'''
        return self._xp % 100

    def has_pin(self):
        '''Return True if the player has set a PIN.'''
        return self.__pin != ""

    def check_pin(self, pin):
        '''Compare a typed PIN with the private PIN. The PIN itself is never returned.'''
        return self.__pin == str(pin)

    def get_pin_for_saving(self):
        '''Only storage.py uses this to write the PIN into players.csv.'''
        return self.__pin

    def update_streak(self, today=None):
        '''Update the daily streak using datetime.date (played yesterday -> streak + 1).'''
        if today is None:
            today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        if self.last_played == str(today):
            pass                                  # already played today, nothing changes
        elif self.last_played == str(yesterday):
            self.streak = self.streak + 1
        else:
            self.streak = 1
        self.last_played = str(today)

    def display(self):
        '''Print the player (same style as Employee.display() in the slides).'''
        print("Name: %s \nLevel: %d \nXP: %d" % (self.name, self.get_level(), self._xp))

    def to_dict(self):
        '''Return the player as a dictionary (one row of players.csv).'''
        return {"name": self.name, "avatar": self.avatar, "xp": self._xp,
                "pin": self.__pin, "streak": self.streak, "last_played": self.last_played,
                "quizzes": self.quizzes, "best_streak": self.best_streak,
                "fixed_count": self.fixed_count, "created": self.created}


class Achievement:
    '''One badge. "unlocked" and "date" are filled from achievements.csv.'''

    def __init__(self, badge_id, title, description, color, symbol):
        '''Create a locked achievement.'''
        self.badge_id = badge_id
        self.title = title
        self.description = description
        self.color = color
        self.symbol = symbol
        self.unlocked = False
        self.date = ""

    def unlock(self, date_text=""):
        '''Mark the badge as unlocked on the given date (today by default).'''
        if date_text == "":
            date_text = str(datetime.date.today())
        self.unlocked = True
        self.date = date_text


# List of all badges: (id, title, description, colour, symbol). Tuples because they never change.
ACHIEVEMENT_DEFINITIONS = [
    ("first_steps", "First Steps", "Finish your first quiz", "#2ecc71", "1"),
    ("on_fire", "On Fire", "Get 10 correct answers in a row", "#e67e22", "10"),
    ("perfectionist", "Perfectionist", "Score 100% in a quiz of 20+ questions", "#f1c40f", "100"),
    ("speed_demon", "Speed Demon", "Get 25 correct answers in one Speed Run", "#e74c3c", "25"),
    ("windows_wizard", "Windows Wizard", "90%+ in a Windows quiz (10+ questions)", "#0984e3", "W"),
    ("photoshop_pro", "Photoshop Pro", "90%+ in a Photoshop quiz (10+ questions)", "#31a8ff", "Ps"),
    ("blender_master", "Blender Master", "90%+ in a Blender quiz (10+ questions)", "#ea7600", "B"),
    ("coder", "Code Ninja", "90%+ in a VS Code quiz (10+ questions)", "#007acc", "</>"),
    ("office_hero", "Office Hero", "90%+ in a Word, Excel or PowerPoint quiz (10+ q.)", "#217346", "O"),
    ("polyglot", "Polyglot", "Play 10 different software", "#9b59b6", "10+"),
    ("daily_habit", "Daily Habit", "Play on 7 days in a row", "#16a085", "7d"),
    ("comeback", "Comeback", "Fix 20 weak shortcuts (answer them right again)", "#c0392b", "R"),
    ("key_master", "Key Master", "10 correct in one Press the Keys quiz", "#3498db", "K"),
    ("early_bird", "Daily Challenger", "Finish your first Daily Challenge", "#fd79a8", "D"),
    ("marathon", "Quiz Marathon", "Finish 25 quizzes", "#8e44ad", "25q"),
    ("level_5", "Rising Star", "Reach level 5", "#fdcb6e", "L5"),
    ("no_hints", "Pure Skill", "Grade A in 10+ questions without any hint", "#00b894", "A"),
    ("survivor", "Survivor", "Finish a Lives quiz (10+ q.) without losing a heart", "#d63031", "3"),
]


def create_all_achievements():
    '''Return a new list of Achievement objects (all locked) built from the definitions.'''
    badges = []
    for badge_id, title, description, color, symbol in ACHIEVEMENT_DEFINITIONS:
        badges.append(Achievement(badge_id, title, description, color, symbol))
    return badges
