'''
results_screen.py - the result of a finished quiz:

* big score, grade, stars, accuracy and XP drawn on a Canvas (+ confetti for grade A / A+)
* a pie chart (Correct / Wrong / Skipped) and a bar chart (accuracy per software)
  made in the same style as the Matplotlib slides, embedded in the window
* a Treeview with every question, the user's answer and the correct answer
'''

import random
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import config
from core import quiz_engine
from data.shortcuts import SOFTWARE_INFO, get_display_name
from ui.base_screen import Screen
from ui.widgets import HoverButton, draw_star, style_chart

CONFETTI_COLORS = ("#e74c3c", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6", "#e67e22")


class ResultsScreen(Screen):
    '''Shows the summary of the last quiz (inherits from Screen).'''

    def build(self):
        '''Create the hero canvas, the chart area, the Treeview and the buttons (method overriding).'''
        self.make_header("Results")
        self.figure = None
        self.chart_widget = None
        self.confetti = []
        self.confetti_job = None
        top = tk.Frame(self, bg=self.colors["bg"])
        top.pack(fill="x", padx=16, pady=(10, 6))
        self.hero = tk.Canvas(top, width=360, height=250, bg=self.colors["panel"], highlightthickness=0)
        self.hero.pack(side="left")
        self.chart_frame = tk.Frame(top, bg=self.colors["panel"])
        self.chart_frame.pack(side="left", fill="both", expand=True, padx=(12, 0))
        self.build_buttons()                 # packed at the bottom first, so it always stays visible
        self.build_table()

    def build_table(self):
        '''Treeview with a Scrollbar: one row per question.'''
        box = tk.Frame(self, bg=self.colors["bg"])
        box.pack(fill="both", expand=True, padx=16)
        columns = ("number", "software", "question", "yours", "correct", "result")
        self.table = ttk.Treeview(box, columns=columns, show="headings", height=6)
        headings = ("#", "Software", "Question", "Your answer", "Correct answer", "")
        widths = (40, 140, 330, 210, 210, 40)
        for column, heading, width in zip(columns, headings, widths):
            self.table.heading(column, text=heading)
            self.table.column(column, width=width, anchor="w")
        self.table.tag_configure("right", foreground=self.colors["success"])
        self.table.tag_configure("wrong", foreground=self.colors["danger"])
        scrollbar = ttk.Scrollbar(box, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_buttons(self):
        '''Play Again, Review Mistakes, Save Chart as PNG and Home.'''
        row = tk.Frame(self, bg=self.colors["bg"])
        row.pack(side="bottom", fill="x", padx=16, pady=10)
        HoverButton(row, "↻ Play Again", self.app.replay_last_quiz, self.colors).pack(side="left")
        HoverButton(row, "Review Mistakes", self.review_mistakes, self.colors, kind="danger").pack(side="left", padx=8)
        HoverButton(row, "Save Chart as PNG", self.save_chart, self.colors, kind="secondary").pack(side="left")
        HoverButton(row, "Home", lambda: self.app.show_screen("home"), self.colors, kind="secondary").pack(side="right")
        self.badges_label = self.make_label(row, "", config.FONT_BOLD, "warning")
        self.badges_label.pack(side="right", padx=12)

    # ---------------------------------------------------------------- showing

    def on_show(self, session=None, summary=None, level_up=False, new_badges=None, **data):
        '''Fill everything with the data of the finished quiz (method overriding).'''
        if session is None:
            return
        self.session = session
        self.summary = summary
        self.draw_hero(summary, level_up)
        self.draw_charts(summary)
        self.fill_table(session)
        if new_badges:
            self.badges_label.config(text="★ New badges: " + str(len(new_badges)))
        else:
            self.badges_label.config(text="")
        if summary["grade"] in ("A", "A+"):
            self.start_confetti()

    def on_hide(self):
        '''Stop the confetti and free the chart (method overriding).'''
        if self.confetti_job is not None:
            self.after_cancel(self.confetti_job)
            self.confetti_job = None
        self.remove_chart()

    def grade_color(self, grade):
        '''Colour of the grade circle (if-elif-else).'''
        if grade in ("A+", "A"):
            return self.colors["success"]
        elif grade in ("B", "C"):
            return self.colors["accent"]
        elif grade == "D":
            return self.colors["warning"]
        else:
            return self.colors["danger"]

    def count_stars(self, accuracy):
        '''1 to 3 stars depending on the accuracy.'''
        if accuracy >= 90:
            return 3
        elif accuracy >= 70:
            return 2
        else:
            return 1

    def draw_hero(self, summary, level_up):
        '''Draw the grade circle, stars, score and the other numbers on the canvas.'''
        c = self.hero
        c.delete("all")
        grade = summary["grade"]
        c.create_oval(20, 20, 120, 120, fill=self.grade_color(grade), outline="")
        c.create_text(70, 70, text=grade, fill="white", font=config.FONT_HUGE)
        c.create_text(140, 38, text=str(summary["score"]) + " points", anchor="w",
                      fill=self.colors["text"], font=config.FONT_LARGE)
        c.create_text(140, 72, text=summary["mode_name"], anchor="w", fill=self.colors["subtext"],
                      font=config.FONT_NORMAL)
        stars = self.count_stars(summary["accuracy"])
        for number in range(3):
            if number < stars:
                fill = "#f1c40f"
            else:
                fill = self.colors["panel_alt"]
            draw_star(c, 160 + number * 40, 105, 16, fill)
        lines = ["Accuracy: %.1f%%" % summary["accuracy"],
                 "Correct %d   |   Wrong %d   |   Skipped %d" % (summary["correct"], summary["wrong"], summary["skipped"]),
                 "Time: %d s   |   Best streak: %d" % (summary["time_taken"], summary["best_streak"]),
                 "XP earned: +%d" % summary["xp"]]
        y = 148
        for line in lines:
            c.create_text(20, y, text=line, anchor="w", fill=self.colors["text"], font=config.FONT_NORMAL)
            y = y + 22
        if level_up:
            c.create_text(340, 232, text="LEVEL UP!  Level %d" % self.app.player.get_level(), anchor="e",
                          fill=self.colors["warning"], font=config.FONT_BOLD)

    # ---------------------------------------------------------------- charts (PPT 1.8 style)

    def draw_charts(self, summary):
        '''Embed a Matplotlib figure with a pie chart and a bar chart.

        NOTE (advanced): plt.show() would open a separate window and stop the program until it
        is closed. FigureCanvasTkAgg puts the chart inside our Tkinter window instead.'''
        self.remove_chart()
        self.figure = Figure(figsize=(6.6, 2.5), dpi=100)
        pie_axes = self.figure.add_subplot(1, 2, 1)       # like plt.subplot(1, 2, 1)
        bar_axes = self.figure.add_subplot(1, 2, 2)       # like plt.subplot(1, 2, 2)
        self.draw_pie(pie_axes, summary)
        self.draw_bars(bar_axes, summary)
        style_chart(self.figure, [pie_axes, bar_axes], self.colors)
        self.figure.tight_layout()
        try:
            canvas = FigureCanvasTkAgg(self.figure, master=self.chart_frame)
            canvas.draw()
            self.chart_widget = canvas.get_tk_widget()
            self.chart_widget.pack(fill="both", expand=True)
        except Exception as error:
            self.chart_widget = tk.Label(self.chart_frame, text="Chart could not be drawn: " + str(error),
                                         bg=self.colors["panel"], fg=self.colors["danger"])
            self.chart_widget.pack(fill="both", expand=True)

    def draw_pie(self, axes, summary):
        '''Pie chart of Correct / Wrong / Skipped (same options as the slide pie chart).'''
        slices = []
        activities = []
        cols = []
        all_parts = [(summary["correct"], "Correct", self.colors["success"]),
                     (summary["wrong"], "Wrong", self.colors["danger"]),
                     (summary["skipped"], "Skipped", self.colors["warning"])]
        for value, name, color in all_parts:
            if value > 0:                     # an empty slice would only show "0.0%"
                slices.append(value)
                activities.append(name)
                cols.append(color)
        if len(slices) == 0:
            axes.text(0.5, 0.5, "No answers", ha="center")
            axes.axis("off")
            return
        explode = [0.1] + [0] * (len(slices) - 1)       # pull the first slice out a little
        axes.pie(slices,
                 labels=activities,
                 colors=cols,
                 startangle=90,
                 shadow=True,
                 explode=explode,
                 autopct='%1.1f%%',
                 textprops={"color": self.colors["text"], "fontsize": 8})
        axes.legend(fontsize=7, loc="upper left", bbox_to_anchor=(-0.3, 1.0))
        axes.set_title('Your answers', fontsize=10)

    def draw_bars(self, axes, summary):
        '''Bar chart of the accuracy per software (same options as the slide bar chart).'''
        names = []
        accuracy = []
        for software_key, numbers in summary["per_software"].items():
            names.append(SOFTWARE_INFO.get(software_key, {"initials": software_key})["initials"])
            accuracy.append(round(numbers[1] * 100 / numbers[0], 1))
        positions = list(range(len(names)))
        axes.bar(positions, accuracy, label="Accuracy %", width=.5, color=self.colors["accent"])
        axes.set_xticks(positions)
        axes.set_xticklabels(names, fontsize=8)
        axes.set_ylim(0, 125)               # free space at the top for the legend
        axes.legend(fontsize=7, loc="upper right")
        axes.set_xlabel('Software', fontsize=8)
        axes.set_ylabel('Accuracy (%)', fontsize=8)
        axes.set_title('Accuracy per software', fontsize=10)

    def remove_chart(self):
        '''Destroy the chart widget and the figure, so memory does not grow.'''
        if self.chart_widget is not None:
            self.chart_widget.destroy()
            self.chart_widget = None
        if self.figure is not None:
            self.figure.clear()
            self.figure = None

    def save_chart(self):
        '''Save the chart as a PNG image (fig.savefig).'''
        if self.figure is None:
            return
        path = filedialog.asksaveasfilename(parent=self, title="Save chart", defaultextension=".png",
                                            initialfile="quiz_result.png", filetypes=[("PNG image", "*.png")])
        if not path:
            return
        try:
            self.figure.savefig(path, facecolor=self.figure.get_facecolor())
            messagebox.showinfo("Saved", "The chart was saved to:\n" + path)
        except (OSError, ValueError) as error:
            messagebox.showerror("Save failed", "Could not save the chart:\n" + str(error))

    # ---------------------------------------------------------------- table and buttons

    def fill_table(self, session):
        '''One row per question with ✓ or ✗.'''
        self.table.delete(*self.table.get_children())
        for number, q in enumerate(session.questions, start=1):
            if q.kind == "action":
                question_text = "What does " + q.shortcut.keys + " do?"
            elif q.kind == "shortcut":
                question_text = q.shortcut.action
            else:
                question_text = "Press: " + q.shortcut.action
            if q.is_correct:
                mark, tag = "✓", "right"
            else:
                mark, tag = "✗", "wrong"
            self.table.insert("", "end", values=(number, get_display_name(q.shortcut.software), question_text,
                                                 q.user_answer, q.get_correct_answer_text(), mark), tags=(tag,))

    def review_mistakes(self):
        '''Start a new quiz with only the questions that were wrong or skipped.'''
        questions = quiz_engine.generate_review_questions(self.session.questions)
        if len(questions) == 0:
            messagebox.showinfo("Review", "No mistakes to review - perfect!")
            return
        software_list = sorted(set([q.shortcut.software for q in questions]))
        self.app.start_quiz(questions, "review", software_list)

    # ---------------------------------------------------------------- confetti

    def start_confetti(self):
        '''Create small coloured ovals above the canvas; they fall down with after().'''
        self.confetti = []
        for number in range(60):
            x = random.randint(0, 360)
            y = random.randint(-250, 0)
            size = random.randint(4, 9)
            oval = self.hero.create_oval(x, y, x + size, y + size, fill=random.choice(CONFETTI_COLORS), outline="")
            self.confetti.append([oval, random.uniform(2, 5), random.uniform(-1, 1)])
        self.confetti_steps = 0
        self.move_confetti()

    def move_confetti(self):
        '''One animation step: every oval falls a bit and drifts sideways.'''
        for oval, speed, drift in self.confetti:
            self.hero.move(oval, drift, speed)
        self.confetti_steps = self.confetti_steps + 1
        if self.confetti_steps < 140:
            self.confetti_job = self.after(30, self.move_confetti)
        else:
            for oval, speed, drift in self.confetti:
                self.hero.delete(oval)
            self.confetti_job = None
