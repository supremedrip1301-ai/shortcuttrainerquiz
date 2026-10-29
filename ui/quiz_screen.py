'''
quiz_screen.py - the quiz itself (all modes).

MCQ questions  : 4 option buttons (also keys 1-4)
Press questions: the user presses the real shortcut. It is detected with Tkinter's
                 own <KeyPress> / <KeyRelease> events (widget.bind, PPT 3.4) and the
                 TkKeyReader in core/key_listener.py. Held keys light up on the
                 on-screen keyboard.

How the keys reach this screen:
    <KeyPress> event --> TkKeyReader --put()--> app.key_queue --get()--> poll_keys()
poll_keys() runs every 30 ms with after().
'''

import queue
import tkinter as tk
from tkinter import messagebox, ttk

import config
from core import key_utils, quiz_engine, sound, stats, storage
from core.key_listener import TkKeyReader
from core.models import ACHIEVEMENT_DEFINITIONS
from data.shortcuts import SOFTWARE_INFO, get_display_name
from ui.base_screen import Screen
from ui.widgets import HoverButton, KeyCaps, OnScreenKeyboard, TimerBar, draw_badge, draw_flame, draw_heart

POLL_MS = 30            # how often the key queue is read
TICK_MS = 100           # how often the timer is updated


class QuizScreen(Screen):
    '''Shows the questions of a QuizSession and checks the answers (inherits from Screen).'''

    def build(self):
        '''Create all parts of the quiz screen (method overriding).'''
        self.session = None
        self.jobs = {}                       # name -> after() job id
        self.tk_reader = TkKeyReader(self.app.key_queue)
        self.chord = key_utils.ChordTracker(config.CHORD_TIMEOUT)
        self.build_top_bar()
        self.timer_bar = TimerBar(self, self.colors, 12)
        self.timer_bar.pack(fill="x", padx=16, pady=(6, 0))
        self.build_question_card()
        self.answer_area = tk.Frame(self, bg=self.colors["bg"])
        self.answer_area.pack(fill="both", expand=True, padx=16)
        self.build_options()
        self.build_keyboard()
        self.feedback = self.make_label(self, "", config.FONT_MEDIUM)
        self.feedback.pack(pady=(2, 2))
        self.build_bottom_bar()
        self.bind_keys()

    # ---------------------------------------------------------------- building

    def build_top_bar(self):
        '''Software badge, mode, question number, progress bar, score, streak and hearts.'''
        bar = tk.Frame(self, bg=self.colors["panel"], padx=12, pady=6)
        bar.pack(fill="x")
        self.badge = tk.Canvas(bar, width=36, height=36, bg=self.colors["panel"], highlightthickness=0)
        self.badge.pack(side="left")
        self.software_label = self.make_label(bar, "", config.FONT_BOLD, bg="panel")
        self.software_label.pack(side="left", padx=8)
        self.mode_label = self.make_label(bar, "", config.FONT_NORMAL, "subtext", "panel")
        self.mode_label.pack(side="left", padx=8)
        self.hearts = tk.Canvas(bar, width=80, height=26, bg=self.colors["panel"], highlightthickness=0)
        self.hearts.pack(side="right", padx=(10, 0))
        self.streak_label = self.make_label(bar, "x0", config.FONT_BOLD, bg="panel")
        self.streak_label.pack(side="right")
        self.flame = tk.Canvas(bar, width=24, height=28, bg=self.colors["panel"], highlightthickness=0)
        self.flame.pack(side="right")
        self.score_label = self.make_label(bar, "Score: 0", config.FONT_BOLD, "accent", "panel")
        self.score_label.pack(side="right", padx=14)
        self.time_label = self.make_label(bar, "", config.FONT_BOLD, bg="panel")
        self.time_label.pack(side="right", padx=10)
        self.number_label = self.make_label(bar, "", config.FONT_BOLD, bg="panel")
        self.number_label.pack(side="right", padx=10)
        self.progress = ttk.Progressbar(self, orient="horizontal", maximum=100)
        self.progress.pack(fill="x")

    def build_question_card(self):
        '''The question: a small title, a big text or key caps, and a hint line.'''
        card = self.make_card(self, 20, 10)
        card.pack(fill="x", padx=16, pady=8)
        self.title_label = self.make_label(card, "", config.FONT_NORMAL, "subtext", "panel")
        self.title_label.pack()
        self.main_label = self.make_label(card, "", config.FONT_LARGE, bg="panel", wraplength=900)
        self.caps = KeyCaps(card, self.colors, 64)
        self.hint_label = self.make_label(card, "", config.FONT_NORMAL, "warning", "panel")
        self.hint_label.pack(side="bottom")

    def build_options(self):
        '''Four option buttons in a 2 x 2 grid.'''
        self.options_frame = tk.Frame(self.answer_area, bg=self.colors["bg"])
        self.option_buttons = []
        for number in range(4):
            button = HoverButton(self.options_frame, "", lambda n=number: self.answer_option(n),
                                 self.colors, kind="secondary", font=config.FONT_MEDIUM,
                                 anchor="w", justify="left", wraplength=440, height=2)
            button.grid(row=number // 2, column=number % 2, padx=6, pady=6, sticky="nsew")
            self.option_buttons.append(button)
        self.options_frame.columnconfigure(0, weight=1, uniform="options")
        self.options_frame.columnconfigure(1, weight=1, uniform="options")

    def build_keyboard(self):
        '''On-screen keyboard and the "you pressed" line for Press the Keys questions.'''
        self.keyboard_frame = tk.Frame(self.answer_area, bg=self.colors["bg"])
        self.pressed_label = self.make_label(self.keyboard_frame, "", config.FONT_BOLD, "subtext")
        self.pressed_label.pack(pady=(0, 4))
        self.keyboard = OnScreenKeyboard(self.keyboard_frame, self.colors, unit=34, bg_key="bg")
        self.keyboard.pack()

    def build_bottom_bar(self):
        '''Hint, Skip, Pause and End buttons.'''
        bar = tk.Frame(self, bg=self.colors["bg"])
        bar.pack(fill="x", padx=16, pady=(0, 10))
        self.hint_button = HoverButton(bar, "? Hint (-3)", self.show_hint, self.colors, kind="secondary")
        self.hint_button.pack(side="left")
        HoverButton(bar, "Skip  »", self.skip_question, self.colors, kind="secondary").pack(side="left", padx=8)
        self.pause_button = HoverButton(bar, "|| Pause", self.toggle_pause, self.colors, kind="secondary")
        self.pause_button.pack(side="left")
        HoverButton(bar, "End quiz", self.end_quiz, self.colors, kind="danger").pack(side="right")
        self.engine_label = self.make_label(bar, "", config.FONT_SMALL, "subtext")
        self.engine_label.pack(side="right", padx=10)

    def bind_keys(self):
        '''widget.bind(event, handler) (PPT 3.4). The handlers return "break" so the window
        does not react to the keys itself (no menu on Alt, no F11 full screen, ...).'''
        self.bind("<KeyPress>", self.on_key_press)
        self.bind("<KeyRelease>", self.on_key_release)
        self.bind("<Alt_L>", self.on_key_press)
        self.bind("<Alt_R>", self.on_key_press)
        self.bind("<F10>", self.on_key_press)

    # ---------------------------------------------------------------- start and stop

    def on_show(self, session=None, practice=False, **data):
        '''Start a new quiz session (method overriding).'''
        self.app.root.config(menu="")        # no menubar during the quiz (Alt must not open it)
        self.session = session
        self.practice = practice
        self.paused = False
        self.locked = False
        self.clear_queue()
        self.mode_label.config(text=session.get_mode_name())
        if self.needs_key_detection():
            self.start_key_detection()
        else:
            self.engine_label.config(text="Keys 1-4 choose an answer")
        self.schedule("poll", POLL_MS, self.poll_keys)
        self.show_question()

    def on_hide(self):
        '''Stop the timers when the screen is left (method overriding).'''
        for job in list(self.jobs.values()):
            try:
                self.after_cancel(job)
            except tk.TclError:
                pass
        self.jobs = {}
        self.session = None
        if "home" in self.app.screens:
            self.app.root.config(menu=self.app.screens["home"].menubar)

    def is_running(self):
        '''True while a quiz is going on (used by App.show_screen to ask before leaving).'''
        return self.session is not None

    def needs_key_detection(self):
        '''True if at least one question is a "press" question.'''
        for q in self.session.questions:
            if q.kind == "press":
                return True
        return False

    def start_key_detection(self):
        '''Press questions: the keys are read from Tkinter's <KeyPress> events (TkKeyReader).'''
        self.tk_reader.reset_held()
        self.engine_label.config(text="Key detection: Tkinter key events")

    def schedule(self, name, delay, function):
        '''Run a function later with after() and remember the job (so it can be cancelled).

        An older job with the same name is cancelled first, so a timer never runs twice.'''
        if name in self.jobs:
            try:
                self.after_cancel(self.jobs[name])
            except tk.TclError:
                pass
        self.jobs[name] = self.after(delay, function)

    def clear_queue(self):
        '''Throw away old key events.'''
        while True:
            try:
                self.app.key_queue.get_nowait()
            except queue.Empty:
                break

    # ---------------------------------------------------------------- showing a question

    def show_question(self):
        '''Show the current question, or finish the quiz when it is over.'''
        if self.session is None:
            return
        if self.session.is_finished():
            self.finish_quiz()
            return
        q = self.session.current_question()
        self.locked = False
        self.chord.reset()
        self.tk_reader.reset_held()
        self.feedback.config(text="")
        self.hint_label.config(text="")
        self.update_top_bar(q)
        self.show_question_text(q)
        if q.kind == "press":
            self.show_keyboard()
        else:
            self.show_options(q)
        self.time_left = float(self.session.seconds_per_question)
        self.last_whole_second = -1
        self.schedule("tick", TICK_MS, self.tick)
        self.focus_set()                       # our frame gets the key events

    def update_top_bar(self, q):
        '''Badge, software name, number, progress, score, streak and hearts.'''
        info = SOFTWARE_INFO.get(q.shortcut.software, {"initials": "?", "color": self.colors["accent"]})
        self.badge.delete("all")
        draw_badge(self.badge, 18, 18, 34, info["initials"], info["color"])
        self.software_label.config(text=get_display_name(q.shortcut.software))
        number = self.session.index + 1
        if isinstance(self.session, quiz_engine.TimedQuizSession):
            self.number_label.config(text="Question " + str(number))
        else:
            total = self.session.total_questions()
            self.number_label.config(text="Question %d / %d" % (number, total))
            self.progress["value"] = (number - 1) * 100 / total
        self.update_score()

    def update_score(self):
        '''Show the score, the streak (flame) and the hearts.'''
        self.score_label.config(text="Score: " + str(self.session.score))
        self.streak_label.config(text="x" + str(self.session.streak))
        self.flame.delete("all")
        draw_flame(self.flame, 0, 2, 22, self.session.streak >= 3)
        self.hearts.delete("all")
        if self.session.lives_mode:
            for number in range(config.LIVES):
                if number < self.session.lives:
                    color = self.colors["danger"]
                else:
                    color = self.colors["panel_alt"]
                draw_heart(self.hearts, 4 + number * 26, 3, 20, color)

    def show_question_text(self, q):
        '''Title + big text (or key caps) for the three question kinds (if-elif-else).'''
        self.main_label.pack_forget()
        self.caps.pack_forget()
        if q.kind == "action":
            self.title_label.config(text="What does this shortcut do?")
            self.caps.pack(fill="x", pady=4)
            self.caps.show(q.shortcut.keys)
        elif q.kind == "shortcut":
            self.title_label.config(text="Which shortcut does this?")
            self.main_label.config(text=q.shortcut.action)
            self.main_label.pack(pady=6)
        else:
            self.title_label.config(text="Press the keys for:")
            self.main_label.config(text=q.shortcut.action)
            self.main_label.pack(pady=6)

    def show_options(self, q):
        '''Fill the 4 option buttons (combos are shown as "Ctrl + Shift + N").'''
        self.keyboard_frame.pack_forget()
        self.options_frame.pack(fill="both", expand=True, pady=4)
        for number in range(4):
            text = q.options[number]
            if q.kind == "shortcut":
                text = key_utils.format_combo_for_display(text)
            button = self.option_buttons[number]
            button.set_base_color(self.colors["panel_alt"], self.colors["text"])
            button.config(text="  " + str(number + 1) + "   " + text)

    def show_keyboard(self):
        '''Show the on-screen keyboard for a Press the Keys question.'''
        self.options_frame.pack_forget()
        self.keyboard_frame.pack(pady=2)
        self.keyboard.reset()
        self.pressed_label.config(text="Press the shortcut now...", fg=self.colors["subtext"])

    # ---------------------------------------------------------------- timer

    def tick(self):
        '''Update the countdown every 100 ms (per question, or for the whole Speed Run).'''
        if self.session is None:
            return
        if not self.paused and not self.locked:
            if isinstance(self.session, quiz_engine.TimedQuizSession):
                self.time_left = self.session.get_time_left()
                total = self.session.total_seconds
                self.progress["value"] = (total - self.time_left) * 100 / total   # time used
            else:
                self.time_left = self.time_left - TICK_MS / 1000
                total = self.session.seconds_per_question
            self.timer_bar.set_fraction(self.time_left / total)
            self.time_label.config(text="%ds" % max(0, round(self.time_left)))
            self.tick_sound()
            if self.time_left <= 0:
                self.time_over()
                return
        self.schedule("tick", TICK_MS, self.tick)

    def tick_sound(self):
        '''A short tick in each of the last 3 seconds.'''
        whole = int(self.time_left) + 1
        if whole <= 3 and whole != self.last_whole_second:
            self.last_whole_second = whole
            sound.play_tick(self.app.sound_on())

    def time_over(self):
        '''The time is over: skip the question (or end the Speed Run).'''
        if isinstance(self.session, quiz_engine.TimedQuizSession):
            self.finish_quiz()
            return
        q = self.session.current_question()
        self.session.record_skip("Time over")
        self.save_mistake(q, False)
        self.show_answer(q, False, "Time's up! The answer was: " + self.answer_text(q))

    # ---------------------------------------------------------------- answering

    def answer_option(self, number):
        '''An option button (or key 1-4) was chosen.'''
        if self.locked or self.paused or self.session is None:
            return
        q = self.session.current_question()
        if q.kind == "press":
            return
        correct = q.check_option(number)
        if not correct:
            self.option_buttons[number].set_base_color(self.colors["danger"])
        self.handle_answer(q, correct)

    def handle_combo(self, combo):
        '''A key combo was pressed during a Press the Keys question.'''
        q = self.session.current_question()
        if q.kind != "press" or self.locked or self.paused:
            return
        finished, answer = self.chord.add_step(combo, q.shortcut.keys)
        if not finished:
            self.pressed_label.config(text="First step " + answer + " OK - now the second step...",
                                      fg=self.colors["warning"])
            return
        self.pressed_label.config(text="You pressed: " + answer, fg=self.colors["text"])
        correct = q.check_combo(answer)
        self.handle_answer(q, correct)

    def handle_answer(self, q, correct):
        '''Give points, save the mistake counter and show the feedback.'''
        seconds_left = 0
        if self.session.has_timer_per_question():
            seconds_left = max(0, int(self.time_left))
        points = self.session.record_answer(correct, seconds_left)
        self.save_mistake(q, correct)
        if correct:
            self.show_answer(q, True, "Correct!  +" + str(points))
        else:
            self.show_answer(q, False, "Wrong - the answer was: " + self.answer_text(q))

    def answer_text(self, q):
        '''The correct answer as nice text.'''
        if q.kind == "action":
            return q.shortcut.action
        return q.shortcut.keys

    def save_mistake(self, q, correct):
        '''Update mistakes.csv (weak shortcuts). A fixed weak shortcut counts for "Comeback".'''
        try:
            fixed = storage.update_mistake(self.app.player.name, q.shortcut.software, q.shortcut.keys, correct)
        except OSError:
            return
        if fixed:
            self.app.player.fixed_count = self.app.player.fixed_count + 1

    def show_answer(self, q, correct, message):
        '''Green / red feedback, sound, then the next question after a short delay.'''
        self.locked = True
        if correct:
            self.feedback.config(text=message, fg=self.colors["success"])
            sound.play_correct(self.app.sound_on())
        else:
            self.feedback.config(text=message, fg=self.colors["danger"])
            sound.play_wrong(self.app.sound_on())
        if q.kind == "press":
            self.show_keyboard_answer(q, correct)
        else:
            self.option_buttons[q.correct_index].set_base_color(self.colors["success"])
        self.update_score()
        delay = config.NEXT_QUESTION_DELAY
        if isinstance(self.session, quiz_engine.TimedQuizSession) and correct:
            delay = 500                       # Speed Run: go on faster
        self.schedule("next", delay, self.go_next)

    def show_keyboard_answer(self, q, correct):
        '''Correct keys in green; wrongly pressed keys in red.'''
        expected = set()
        for step in key_utils.combo_to_key_list(q.shortcut.keys):
            expected.update(step)
        pressed = set()
        for step in key_utils.combo_to_key_list(q.user_answer):
            pressed.update(step)
        self.keyboard.reset()
        if not q.skipped:
            self.keyboard.highlight(pressed - expected, self.colors["danger"])
        self.keyboard.highlight(expected, self.colors["success"])
        if not correct:
            self.pressed_label.config(text="Correct keys: " + key_utils.format_combo_for_display(q.shortcut.keys),
                                      fg=self.colors["success"])

    def go_next(self):
        '''Move on to the next question.'''
        if self.session is None:
            return
        self.session.next_question()
        self.show_question()

    def skip_question(self):
        '''The Skip button.'''
        if self.locked or self.paused or self.session is None:
            return
        q = self.session.current_question()
        self.session.record_skip("Skipped")
        self.save_mistake(q, False)
        self.show_answer(q, False, "Skipped - the answer was: " + self.answer_text(q))

    def show_hint(self):
        '''The Hint button: show a hint (costs 3 points if the answer is correct).'''
        if self.locked or self.paused or self.session is None:
            return
        q = self.session.current_question()
        self.hint_label.config(text="Hint: " + self.session.use_hint())
        if q.kind == "press":
            main_keys = key_utils.get_main_keys(q.shortcut.keys)
            self.keyboard.highlight(main_keys[:1], self.colors["warning"])
        self.focus_set()

    # ---------------------------------------------------------------- pause

    def toggle_pause(self):
        '''Pause or resume the quiz (the Pause button).'''
        if self.session is None or self.locked:
            return
        self.paused = not self.paused
        if self.paused:
            self.session.pause()
            self.pause_button.config(text="▶ Resume")
            self.title_label.config(text="")
            self.main_label.config(text="Paused - press Resume to continue")
            self.main_label.pack(pady=6)
            self.caps.pack_forget()
            self.options_frame.pack_forget()
            self.keyboard_frame.pack_forget()
        else:
            self.session.resume()
            self.pause_button.config(text="|| Pause")
            q = self.session.current_question()
            self.show_question_text(q)
            if q.kind == "press":
                self.keyboard_frame.pack(pady=2)
            else:
                self.options_frame.pack(fill="both", expand=True, pady=4)
            self.focus_set()

    # ---------------------------------------------------------------- keys

    def poll_keys(self):
        '''Read all waiting key messages from the queue (runs every 30 ms with after()).'''
        if self.session is None:
            return
        for count in range(50):               # at most 50 events per call
            try:
                kind, value = self.app.key_queue.get_nowait()
            except queue.Empty:
                break
            self.handle_event(kind, value)
        self.schedule("poll", POLL_MS, self.poll_keys)

    def handle_event(self, kind, value):
        '''Handle one queue message: held keys or a finished combo.'''
        if self.session is None or self.session.is_finished():
            return
        q = self.session.current_question()
        if q.kind != "press" or self.focus_get() is None:
            return                            # keys typed in another program are ignored
        if kind == "held" and not self.locked and not self.paused:
            self.keyboard.reset()
            self.keyboard.highlight(value, self.colors["held"])
        elif kind == "combo":
            self.handle_combo(value)

    def on_key_press(self, event):
        '''Tkinter <KeyPress>: keys 1-4 for MCQ, and the key reader for press questions.'''
        if self.session is not None and not self.session.is_finished():
            q = self.session.current_question()
            if q.kind != "press" and event.char in ("1", "2", "3", "4"):
                self.answer_option(int(event.char) - 1)
            elif q.kind == "press":
                self.tk_reader.handle_press(event)
        return "break"                        # stop Tkinter's own reaction to the key

    def on_key_release(self, event):
        '''Tkinter <KeyRelease>: the key reader removes the key from the held keys.'''
        self.tk_reader.handle_release(event)
        return "break"

    # ---------------------------------------------------------------- the end

    def end_quiz(self):
        '''The End quiz button: finish now and save the answered questions.'''
        if self.session is None:
            return
        if messagebox.askyesno("End quiz", "End the quiz now? Your answered questions will be saved."):
            self.finish_quiz()                # finish() drops the question that was not answered

    def finish_quiz(self):
        '''Stop everything, save the results and open the results screen.'''
        session = self.session
        if session is None:
            return
        self.session = None                   # stops tick() and poll_keys()
        session.finish()
        summary = session.get_summary()
        level_up, new_badges = self.save_results(session, summary)
        self.app.show_screen("results", session=session, summary=summary,
                             level_up=level_up, new_badges=new_badges)

    def save_results(self, session, summary):
        '''Update the player (XP, streak, counters), history.csv and the achievements.'''
        player = self.app.player
        if summary["total"] == 0:
            return False, []
        player.quizzes = player.quizzes + 1
        player.update_streak()
        if session.best_streak > player.best_streak:
            player.best_streak = session.best_streak
        level_up = player.add_xp(summary["xp"])
        self.app.save_player()
        mode_label = summary["mode_name"]
        if summary["mode"] == "daily" and self.practice:
            mode_label = "Daily Practice"
        try:
            storage.add_history(player.name, summary, mode_label)
            unlocked = storage.load_achievements(player.name)
            new_badges = stats.check_new_achievements(player, summary, unlocked)
            for badge_id in new_badges:
                storage.unlock_achievement(player.name, badge_id)
        except OSError as error:
            messagebox.showerror("Save error", "Could not save the results:\n" + str(error))
            return level_up, []
        self.show_badge_toasts(new_badges)
        return level_up, new_badges

    def show_badge_toasts(self, new_badges):
        '''Show one toast per new badge, 2.7 seconds apart.'''
        titles = {}
        for badge_id, title, description, color, symbol in ACHIEVEMENT_DEFINITIONS:
            titles[badge_id] = (title, description, color)
        for number, badge_id in enumerate(new_badges):
            title, description, color = titles[badge_id]
            self.app.root.after(number * 2700, lambda t=title, d=description, c=color:
                                self.badge_toast(t, d, c))

    def badge_toast(self, title, description, color):
        '''Show one "badge unlocked" toast with a little melody.'''
        sound.play_achievement(self.app.sound_on())
        self.app.show_toast("★ Badge unlocked: " + title, description, color)
