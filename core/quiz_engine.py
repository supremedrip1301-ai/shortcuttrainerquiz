'''
quiz_engine.py - question generation, scoring, grading and the quiz session classes.

Inheritance used here (PPT 1.5):
    QuizSession                      (normal quiz, one timer per question)
      └── TimedQuizSession           (single + multilevel: one timer for the whole quiz)
            └── SpeedRunSession      (multilevel: 60 seconds, endless questions)
'''

import datetime
import random
import time

import config
from core import key_utils
from core.models import Question
from data.shortcuts import combine_shortcuts, get_all_software_names, get_shortcuts

# Quiz modes: internal name -> text shown to the user (dictionary).
QUIZ_MODES = {
    "action": "Guess the Action",
    "shortcut": "Guess the Shortcut",
    "mixed": "Mixed MCQ",
    "press": "Press the Keys",
    "speed": "Speed Run",
    "daily": "Daily Challenge",
    "revise": "Revise Weak Shortcuts",
    "review": "Review Mistakes",
}

OPTIONS_PER_QUESTION = 4


# ---------------------------------------------------------------- grading and scoring

def get_grade(accuracy):
    '''Return the grade for an accuracy percentage (multi-way if-elif-else, PPT 1.3).'''
    score = accuracy
    if score >= 100.0:
        grade = 'A+'
    elif score >= 90.0:
        grade = 'A'
    elif score >= 80.0:
        grade = 'B'
    elif score >= 70.0:
        grade = 'C'
    elif score >= 60.0:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def calculate_points(is_correct, seconds_left=0, streak=0, used_hint=False):
    '''Return the points for one answer.

    correct = 10 + remaining seconds (time bonus), hint = -3,
    every 5 correct answers in a row = +20 streak bonus, wrong or skipped = 0.'''
    if not is_correct:
        points = 0
    elif used_hint:
        points = config.POINTS_CORRECT - config.HINT_PENALTY + int(seconds_left)
    else:
        points = config.POINTS_CORRECT + int(seconds_left)
    if is_correct and streak > 0 and streak % 5 == 0:
        points = points + config.POINTS_STREAK_BONUS
    return points


def calculate_result(questions):
    '''Count the answers of a finished quiz. Returns 5 values (PPT 1.4: return multiple values).'''
    correct = 0
    wrong = 0
    skipped = 0
    for q in questions:
        if q.is_correct:
            correct = correct + 1
        elif q.skipped:
            skipped = skipped + 1
        else:
            wrong = wrong + 1
    total = len(questions)
    if total > 0:
        accuracy = round(correct * 100 / total, 1)
    else:
        accuracy = 0.0
    grade = get_grade(accuracy)
    return correct, wrong, skipped, accuracy, grade


def get_wrong_answers(questions):
    '''Return a list of the questions that were wrong or skipped (PPT 1.4: return a list).'''
    wrong_list = []
    for q in questions:
        if not q.is_correct:
            wrong_list.append(q)
    return wrong_list


# ---------------------------------------------------------------- building questions

def similarity(first, second, kind):
    '''Return a small number that says how similar two shortcuts are (bigger = more similar).

    Similar wrong options make the MCQ harder and more useful.'''
    points = 0
    if first.category == second.category:
        points = points + 1
    if kind == "shortcut":
        first_keys = key_utils.combo_to_key_list(first.keys)
        second_keys = key_utils.combo_to_key_list(second.keys)
        if len(first_keys) == len(second_keys):
            points = points + 1
        # same modifiers (e.g. both use Ctrl+Shift) -> looks similar
        first_mods = set([k for k in first_keys[0] if key_utils.is_modifier(k)])
        second_mods = set([k for k in second_keys[0] if key_utils.is_modifier(k)])
        if first_mods == second_mods:
            points = points + 2
    return points


def option_text(shortcut, kind):
    '''Return the text of an answer option: the action, or the key combo.'''
    if kind == "action":
        return shortcut.action
    return shortcut.keys


def get_wrong_options(correct, same_software, all_shortcuts, kind, count=3):
    '''Return a list of `count` wrong option texts, preferably from the same software.'''
    correct_text = option_text(correct, kind)
    used = [correct_text.lower()]
    candidates = list(same_software)
    random.shuffle(candidates)
    # sorted() with lambda: the most similar shortcuts come first (shuffle keeps ties random)
    candidates = sorted(candidates, key=lambda s: similarity(correct, s, kind), reverse=True)
    others = list(all_shortcuts)
    random.shuffle(others)
    wrong = []
    for shortcut in candidates[:8] + others:
        text = option_text(shortcut, kind)
        if text.lower() in used:
            continue
        if kind != "action" and key_utils.combos_match(text, correct_text):
            continue                     # an "equal" combo would be a second correct answer
        wrong.append(text)
        used.append(text.lower())
        if len(wrong) == count:
            break
    return wrong


def make_question(shortcut, kind, all_shortcuts):
    '''Create one Question. MCQ kinds get 4 shuffled options with exactly one correct.'''
    if kind == "press":
        return Question(shortcut, "press")
    same_software = [s for s in all_shortcuts
                     if s.software == shortcut.software and s.keys != shortcut.keys]
    options = get_wrong_options(shortcut, same_software, all_shortcuts, kind, OPTIONS_PER_QUESTION - 1)
    correct_text = option_text(shortcut, kind)
    options.append(correct_text)
    random.shuffle(options)
    return Question(shortcut, kind, options, options.index(correct_text))


def choose_kind(mode):
    '''Return the question kind for a quiz mode. "mixed" picks action or shortcut at random.'''
    if mode in ("action", "shortcut", "press"):
        return mode
    return random.choice(["action", "shortcut"])


def get_pool(software_list, difficulty="all", mode="mixed"):
    '''Return the list of Shortcut objects that may be asked for these settings.'''
    pool = combine_shortcuts(*software_list, difficulty=difficulty)
    if mode == "press":
        pool = list(filter(lambda s: s.can_be_pressed(), pool))
    return pool


def count_available(software_list, difficulty="all", mode="mixed"):
    '''Return how many different questions are possible for these settings.'''
    return len(get_pool(software_list, difficulty, mode))


def generate_questions(software_list, count=10, difficulty="all", mode="mixed"):
    '''Create a list of questions (default arguments, PPT 1.4). No shortcut repeats in one quiz.'''
    pool = get_pool(software_list, difficulty, mode)
    all_shortcuts = combine_shortcuts(*software_list)
    if count > len(pool):
        count = len(pool)
    chosen = random.sample(pool, count)          # random.sample never picks the same item twice
    questions = []
    for shortcut in chosen:
        questions.append(make_question(shortcut, choose_kind(mode), all_shortcuts))
    return questions


def generate_daily_questions(today=None):
    '''Create the 10 Daily Challenge questions. Everyone gets the same ones on the same day.'''
    if today is None:
        today = datetime.date.today()
    # random.seed with the date: the "random" choices are the same for the whole day
    random.seed("daily-" + str(today))
    questions = generate_questions(get_all_software_names(), config.DAILY_QUESTIONS, "all", "mixed")
    random.seed()                                # back to normal random numbers
    return questions


def find_shortcut(software, keys):
    '''Return the Shortcut object with these keys in this software (or None).'''
    for shortcut in get_shortcuts(software):
        if shortcut.keys == keys:
            return shortcut
    return None


def generate_revise_questions(weak_rows, count=10):
    '''Create questions from the player's weakest shortcuts (rows from mistakes.csv).'''
    questions = []
    for row in weak_rows:
        shortcut = find_shortcut(row["software"], row["keys"])
        if shortcut is None:
            continue                     # the shortcut was removed from the data files
        all_shortcuts = get_shortcuts(shortcut.software)
        questions.append(make_question(shortcut, choose_kind("mixed"), all_shortcuts))
        if len(questions) == count:
            break
    random.shuffle(questions)
    return questions


def generate_review_questions(old_questions):
    '''Create new questions (new options) for the questions answered wrongly last time.'''
    questions = []
    for old in get_wrong_answers(old_questions):
        all_shortcuts = get_shortcuts(old.shortcut.software)
        questions.append(make_question(old.shortcut, old.kind, all_shortcuts))
    random.shuffle(questions)
    return questions


# ---------------------------------------------------------------- quiz sessions

class QuizSession:
    '''A normal quiz: questions, score, streak, lives and a timer for each question.'''

    def __init__(self, questions, mode, software_list, seconds_per_question=20, lives_mode=False):
        '''Start a new quiz with a ready list of Question objects.'''
        self.questions = questions
        self.mode = mode                          # key of QUIZ_MODES
        self.software_list = software_list
        self.seconds_per_question = seconds_per_question
        self.lives_mode = lives_mode
        if lives_mode:
            self.lives = config.LIVES
        else:
            self.lives = 0
        self.index = 0
        self.score = 0
        self.streak = 0
        self.best_streak = 0
        self.hints_used = 0
        self.start_time = time.time()
        self.end_time = 0.0
        self.paused_at = 0.0
        self.paused_total = 0.0

    def get_mode_name(self):
        '''Return the readable name of the quiz mode.'''
        return QUIZ_MODES.get(self.mode, self.mode)

    def current_question(self):
        '''Return the Question that is being asked now.'''
        return self.questions[self.index]

    def total_questions(self):
        '''Return the number of questions in this quiz.'''
        return len(self.questions)

    def has_timer_per_question(self):
        '''True when every question has its own countdown.'''
        return self.seconds_per_question > 0

    def record_answer(self, is_correct, seconds_left=0):
        '''Update streak, score and lives after an answer. Returns the points earned.'''
        question = self.current_question()
        if is_correct:
            self.streak = self.streak + 1
            if self.streak > self.best_streak:
                self.best_streak = self.streak
        else:
            self.streak = 0
            if self.lives_mode:
                self.lives = self.lives - 1
        points = calculate_points(is_correct, seconds_left, self.streak, question.used_hint)
        question.points = points
        self.score = max(0, self.score + points)
        return points

    def record_skip(self, reason="Skipped"):
        '''Skip the current question (also used when the time runs out).'''
        self.current_question().mark_skipped(reason)
        self.record_answer(False)

    def use_hint(self):
        '''Mark the hint as used and return the hint text (the first main key).'''
        question = self.current_question()
        if not question.used_hint:
            question.used_hint = True
            self.hints_used = self.hints_used + 1
        main_keys = key_utils.get_main_keys(question.shortcut.keys)
        if question.kind == "action":
            return "Category: " + question.shortcut.category
        return "The main key is: " + main_keys[0]

    def next_question(self):
        '''Move to the next question.'''
        self.index = self.index + 1

    def is_finished(self):
        '''True when all questions are done or all lives are lost.'''
        if self.lives_mode and self.lives <= 0:
            return True
        return self.index >= len(self.questions)

    def pause(self):
        '''Remember when the pause started.'''
        if self.paused_at == 0.0:
            self.paused_at = time.time()

    def resume(self):
        '''Add the paused time, so it is not counted as playing time.'''
        if self.paused_at != 0.0:
            self.paused_total = self.paused_total + (time.time() - self.paused_at)
            self.paused_at = 0.0

    def finish(self):
        '''Stop the clock and keep only the questions that were really answered.'''
        self.resume()
        self.end_time = time.time()
        self.questions = [q for q in self.questions if q.answered]

    def get_time_taken(self):
        '''Return the playing time in whole seconds (pauses not counted).'''
        end = self.end_time
        if end == 0.0:
            end = time.time()
        return int(end - self.start_time - self.paused_total)

    def get_per_software(self):
        '''Return a dictionary: software -> [total, correct] for this quiz.'''
        result = {}
        for q in self.questions:
            name = q.shortcut.software
            if name not in result:
                result[name] = [0, 0]
            result[name][0] = result[name][0] + 1
            if q.is_correct:
                result[name][1] = result[name][1] + 1
        return result

    def get_summary(self):
        '''Return everything the results screen and storage need, as one dictionary.'''
        correct, wrong, skipped, accuracy, grade = calculate_result(self.questions)
        return {"mode": self.mode, "mode_name": self.get_mode_name(),
                "software_list": list(self.software_list), "total": len(self.questions),
                "correct": correct, "wrong": wrong, "skipped": skipped,
                "score": self.score, "accuracy": accuracy, "grade": grade,
                "time_taken": self.get_time_taken(), "xp": self.score // 2,
                "best_streak": self.best_streak, "hints_used": self.hints_used,
                "lives_mode": self.lives_mode, "lives_left": self.lives,
                "per_software": self.get_per_software()}


class TimedQuizSession(QuizSession):
    '''A quiz with ONE timer for the whole quiz (single inheritance from QuizSession).'''

    def __init__(self, questions, mode, software_list, total_seconds=60):
        '''Create the quiz without per-question timers and with a total time limit.'''
        super().__init__(questions, mode, software_list, seconds_per_question=0, lives_mode=False)
        self.total_seconds = total_seconds

    def get_time_left(self):
        '''Return the seconds left for the whole quiz (never below 0).'''
        paused_now = 0.0
        if self.paused_at != 0.0:
            paused_now = time.time() - self.paused_at
        used = time.time() - self.start_time - self.paused_total - paused_now
        return max(0.0, self.total_seconds - used)

    def is_finished(self):
        '''Method overriding: the quiz also ends when the total time is over.'''
        if self.get_time_left() <= 0:
            return True
        return super().is_finished()


class SpeedRunSession(TimedQuizSession):
    '''Speed Run: 60 seconds, as many correct answers as possible (multilevel inheritance).'''

    def __init__(self, software_list, difficulty="all"):
        '''Create the first batch of questions and start the 60-second clock.'''
        self.difficulty = difficulty
        questions = generate_questions(software_list, 20, difficulty, "mixed")
        super().__init__(questions, "speed", software_list, config.SPEED_RUN_SECONDS)

    def next_question(self):
        '''Method overriding: add more questions when the list is almost used up.'''
        super().next_question()
        if self.index >= len(self.questions) - 2:
            asked = set([(q.shortcut.software, q.shortcut.keys) for q in self.questions])
            extra = generate_questions(self.software_list, 20, self.difficulty, "mixed")
            new_ones = [q for q in extra if (q.shortcut.software, q.shortcut.keys) not in asked]
            if len(new_ones) == 0:
                new_ones = extra             # every shortcut was asked once, allow repeats now
            self.questions.extend(new_ones)
