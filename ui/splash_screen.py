'''
splash_screen.py - the first screen: an animated drawing on a Canvas (PPT 3.3)
and a ttk.Progressbar that fills up with after(). Then the login screen opens.
'''

import tkinter as tk
from tkinter import ttk

import config
from data.shortcuts import count_all_shortcuts, get_all_software_names
from ui.base_screen import Screen


class SplashScreen(Screen):
    '''Animated welcome screen (inherits from Screen).'''

    CAP_TEXTS = ("Ctrl", "Shift", "Alt")      # tuple: the three bouncing key caps

    def build(self):
        '''Create the canvas, the progress bar and the status text (method overriding).'''
        self.canvas = tk.Canvas(self, bg=self.colors["bg"], highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.status = self.make_label(self, "Loading...", config.FONT_NORMAL, "subtext")
        self.status.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal", mode="determinate",
                                        maximum=100, length=440)
        self.progress.pack(pady=(6, 40))
        self.canvas.bind("<Button-1>", self.skip)
        # place() (PPT 3.5): put the small hint at the top-right corner using relative position
        skip_hint = self.make_label(self, "Click to skip", config.FONT_SMALL, "subtext")
        skip_hint.place(relx=0.98, rely=0.02, anchor="ne")
        self.jobs = []
        self.caps = []
        self.software_count = len(get_all_software_names())
        self.shortcut_count = count_all_shortcuts()       # recursive counter (PPT 1.4)

    def on_show(self, **data):
        '''Start the animation when the screen appears.'''
        self.value = 0
        self.progress["value"] = 0
        self.jobs.append(self.after(80, self.draw_scene))

    def on_hide(self):
        '''Stop every scheduled after() call.'''
        for job in self.jobs:
            try:
                self.after_cancel(job)
            except tk.TclError:
                pass
        self.jobs = []

    def draw_scene(self):
        '''Draw the background shapes, the title and the key caps above the window.'''
        c = self.canvas
        c.delete("all")
        width = max(c.winfo_width(), 600)
        height = max(c.winfo_height(), 400)
        # decorations: arcs, ovals and lines (create_arc / create_oval / create_line)
        c.create_arc(-160, -160, 260, 260, start=270, extent=90, fill=self.colors["accent"], outline="")
        c.create_arc(width - 220, height - 220, width + 180, height + 180, start=90, extent=90,
                     fill=self.colors["panel_alt"], outline="")
        c.create_oval(width - 140, 40, width - 90, 90, outline=self.colors["accent"], width=3)
        c.create_oval(70, height - 110, 100, height - 80, fill=self.colors["warning"], outline="")
        c.create_line(0, height - 30, width, height - 30, fill=self.colors["panel_alt"], width=2, dash=(6, 4))
        c.create_text(width / 2, height * 0.18, text=config.APP_TITLE, font=config.FONT_HUGE,
                      fill=self.colors["text"])
        c.create_text(width / 2, height * 0.18 + 50, text="Learn keyboard shortcuts the smart way",
                      font=config.FONT_MEDIUM, fill=self.colors["subtext"])
        self.create_caps(width, height)
        self.jobs.append(self.after(20, self.animate))

    def create_caps(self, width, height):
        '''Create the three key caps above the visible area; they fall down and bounce.'''
        self.caps = []
        cap_width = 120
        gap = 60
        total = len(self.CAP_TEXTS) * cap_width + (len(self.CAP_TEXTS) - 1) * gap
        x = (width - total) / 2
        self.target_y = height * 0.48
        for number, text in enumerate(self.CAP_TEXTS):
            tag = "cap" + str(number)
            start_y = -100 - number * 90                 # each cap starts a bit higher
            self.canvas.create_rectangle(x, start_y + 8, x + cap_width, start_y + 78,
                                         fill=self.colors["key_border"], outline="", tags=tag)
            self.canvas.create_rectangle(x, start_y, x + cap_width, start_y + 70,
                                         fill=self.colors["key_bg"], outline=self.colors["accent"],
                                         width=3, tags=tag)
            self.canvas.create_text(x + cap_width / 2, start_y + 35, text=text, font=config.FONT_LARGE,
                                    fill=self.colors["key_text"], tags=tag)
            # every cap remembers: tag, current top y, speed
            self.caps.append([tag, start_y, 0.0])
            if number > 0:
                self.canvas.create_text(x - gap / 2, self.target_y + 35, text="+", font=config.FONT_LARGE,
                                        fill=self.colors["subtext"], state="hidden", tags="plus")
            x = x + cap_width + gap

    def animate(self):
        '''One animation step: move the caps (simple gravity + bounce) and fill the bar.'''
        for cap in self.caps:
            tag, y, speed = cap
            speed = speed + 1.6                  # gravity
            new_y = y + speed
            if new_y > self.target_y:            # hit the "floor": bounce back up a little
                new_y = self.target_y
                speed = -speed * 0.45
                if abs(speed) < 2:
                    speed = 0.0
            self.canvas.move(tag, 0, new_y - y)
            cap[1] = new_y
            cap[2] = speed
        self.value = self.value + 1.2
        if self.value > 55:
            self.canvas.itemconfig("plus", state="normal")     # show the "+" signs
        self.progress["value"] = self.value
        self.update_status()
        if self.value >= 100:
            self.jobs.append(self.after(350, self.go_next))
        else:
            self.jobs.append(self.after(20, self.animate))

    def update_status(self):
        '''Change the status text while the bar fills (if-elif-else).'''
        if self.value < 35:
            text = "Loading " + str(self.software_count) + " software..."
        elif self.value < 70:
            text = "Counting " + str(self.shortcut_count) + " shortcuts..."
        elif self.value < 100:
            text = "Preparing the quiz engine..."
        else:
            text = "Ready!"
        self.status.config(text=text)

    def skip(self, event=None):
        '''A click on the canvas skips the animation.'''
        self.value = 100

    def go_next(self):
        '''Open the login screen.'''
        self.app.show_screen("login")
