'''
widgets.py - reusable widgets and Canvas drawings used by many screens.

HoverButton      a flat tk.Button that changes colour on <Enter> / <Leave>
KeyCaps          a Canvas that draws a combo as key caps:  [Ctrl] + [Shift] + [N]
TimerBar         a Canvas countdown bar (green -> yellow -> red)
OnScreenKeyboard a full keyboard drawn on a Canvas (create_rectangle + create_text)
ScrollableFrame  a Frame with a vertical scrollbar
Toast            a small borderless Toplevel that disappears after 2.5 seconds
draw_...()       small Canvas drawings: badge, star, heart, flame (PPT 3.3: Canvas)
'''

import math
import tkinter as tk
from tkinter import ttk

import config
from core import key_utils


# ---------------------------------------------------------------- buttons and inputs

class HoverButton(tk.Button):
    '''A flat button with a hover colour (inherits from tk.Button).'''

    # kind -> (normal colour key, hover colour key, text colour key)
    KINDS = {"primary": ("accent", "accent_hover", "white"),
             "secondary": ("panel_alt", "accent", "text"),
             "success": ("success", "accent_hover", "white"),
             "danger": ("danger", "accent_hover", "white")}

    def __init__(self, parent, text, command, colors, kind="primary", font=config.FONT_BOLD, **options):
        '''Create the button with colours taken from the theme dictionary.'''
        normal_key, hover_key, fg_key = self.KINDS[kind]
        self.normal_bg = colors[normal_key]
        self.hover_bg = colors[hover_key]
        if fg_key == "white":
            self.normal_fg = "white"
        else:
            self.normal_fg = colors[fg_key]
        super().__init__(parent, text=text, command=command, bg=self.normal_bg, fg=self.normal_fg,
                         activebackground=self.hover_bg, activeforeground="white",
                         disabledforeground=colors["subtext"], relief="flat", bd=0, font=font,
                         padx=14, pady=6, cursor="hand2", **options)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        '''Mouse enters the button: use the hover colour.'''
        if str(self["state"]) != "disabled":
            self.config(bg=self.hover_bg, fg="white")

    def on_leave(self, event):
        '''Mouse leaves the button: back to the normal colour.'''
        self.config(bg=self.normal_bg, fg=self.normal_fg)

    def set_base_color(self, bg, fg="white"):
        '''Change the normal colour (used to show green / red after an answer).'''
        self.normal_bg = bg
        self.normal_fg = fg
        self.config(bg=bg, fg=fg)


def make_checkbutton(parent, text, variable, colors, bg_key="panel", command=None):
    '''Create a tk.Checkbutton that fits the theme.'''
    return tk.Checkbutton(parent, text=text, variable=variable, command=command,
                          bg=colors[bg_key], fg=colors["text"], selectcolor=colors["entry_bg"],
                          activebackground=colors[bg_key], activeforeground=colors["text"],
                          font=config.FONT_NORMAL, anchor="w", cursor="hand2")


def make_radiobutton(parent, text, variable, value, colors, bg_key="panel", command=None):
    '''Create a tk.Radiobutton that fits the theme.'''
    return tk.Radiobutton(parent, text=text, variable=variable, value=value, command=command,
                          bg=colors[bg_key], fg=colors["text"], selectcolor=colors["entry_bg"],
                          activebackground=colors[bg_key], activeforeground=colors["text"],
                          font=config.FONT_NORMAL, anchor="w", cursor="hand2")


def make_entry(parent, colors, width=24, **options):
    '''Create a tk.Entry with theme colours.'''
    return tk.Entry(parent, width=width, font=config.FONT_NORMAL, bg=colors["entry_bg"],
                    fg=colors["text"], insertbackground=colors["text"], relief="flat",
                    highlightthickness=1, highlightbackground=colors["key_border"],
                    highlightcolor=colors["accent"], **options)


# ---------------------------------------------------------------- key caps

class KeyCaps(tk.Canvas):
    '''Draws a key combo as key caps, e.g.  [Ctrl] + [Shift] + [N]  then  [Ctrl] + [C].'''

    def __init__(self, parent, colors, height=64, bg_key="panel"):
        '''Create an empty canvas; call show("Ctrl+N") to draw.'''
        super().__init__(parent, height=height, bg=colors[bg_key], highlightthickness=0)
        self.colors = colors
        self.combo_text = ""
        self.bind("<Configure>", lambda event: self.redraw())

    def show(self, combo_text):
        '''Remember the combo and draw it.'''
        self.combo_text = combo_text
        self.redraw()

    def clear(self):
        '''Remove all key caps.'''
        self.show("")

    def build_items(self):
        '''Return a list of (kind, text, width) items to draw from left to right.'''
        items = []
        steps = key_utils.combo_to_key_list(self.combo_text)
        for step_number, step in enumerate(steps):
            if step_number > 0:
                items.append(("text", "then", 64))
            for key_number, name in enumerate(step):
                if key_number > 0:
                    items.append(("text", "+", 26))
                items.append(("key", name, max(50, 22 + 11 * len(name))))
        return items

    def redraw(self):
        '''Draw every key cap centred on the canvas.'''
        self.delete("all")
        if self.combo_text == "":
            return
        items = self.build_items()
        total = sum([width for kind, text, width in items])
        x = (self.winfo_width() - total) / 2
        y = 8
        cap_height = int(self["height"]) - 18
        for kind, text, width in items:
            if kind == "key":
                self.draw_key_cap(x, y, width, cap_height, text)
            else:
                self.create_text(x + width / 2, y + cap_height / 2, text=text,
                                 fill=self.colors["subtext"], font=config.FONT_BOLD)
            x = x + width

    def draw_key_cap(self, x, y, width, height, text):
        '''Draw one key cap: a darker "shadow" rectangle and the key on top of it.'''
        self.create_rectangle(x + 2, y + 5, x + width - 2, y + height + 5,
                              fill=self.colors["key_border"], outline="")
        self.create_rectangle(x + 2, y, x + width - 2, y + height,
                              fill=self.colors["key_bg"], outline=self.colors["key_border"], width=2)
        self.create_text(x + width / 2, y + height / 2, text=text,
                         fill=self.colors["key_text"], font=config.FONT_KEY)


# ---------------------------------------------------------------- timer bar

class TimerBar(tk.Canvas):
    '''A countdown bar that changes colour from green to yellow to red.'''

    def __init__(self, parent, colors, height=14, bg_key="bg"):
        '''Create the bar (full at the start).'''
        super().__init__(parent, height=height, bg=colors[bg_key], highlightthickness=0)
        self.colors = colors
        self.fraction = 1.0
        self.bind("<Configure>", lambda event: self.set_fraction(self.fraction))

    def set_fraction(self, fraction):
        '''Draw the bar filled to `fraction` (0.0 - 1.0).'''
        self.fraction = max(0.0, min(1.0, fraction))
        if self.fraction > 0.5:
            color = self.colors["success"]
        elif self.fraction > 0.25:
            color = self.colors["warning"]
        else:
            color = self.colors["danger"]
        width = self.winfo_width()
        height = int(self["height"])
        self.delete("all")
        self.create_rectangle(0, 0, width, height, fill=self.colors["panel_alt"], outline="")
        self.create_rectangle(0, 0, width * self.fraction, height, fill=color, outline="")


# ---------------------------------------------------------------- on-screen keyboard

# Short labels for long key names (dictionary).
KEY_LABELS = {"Backspace": "Bksp", "CapsLock": "Caps", "PageUp": "PgUp", "PageDown": "PgDn",
              "Insert": "Ins", "Delete": "Del", "PrtScn": "PrtSc", "ScrollLock": "ScrLk",
              "NumLock": "Num", "Up": "↑", "Down": "↓", "Left": "←",
              "Right": "→", "Space": "", "Escape": "Esc"}


def keyboard_layout():
    '''Return the keyboard as a list of (name, x, y, width, height) in "key units".'''
    keys = []
    row0 = [("Esc", 0, 1)]
    x = 2
    for number in range(1, 13):
        row0.append(("F" + str(number), x, 1))
        x = x + 1
        if number in (4, 8):
            x = x + 0.5
    rows = [
        ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", ("Backspace", 2)],
        [("Tab", 1.5), "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", ("\\", 1.5)],
        [("CapsLock", 1.75), "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", ("Enter", 2.25)],
        [("Shift", 2.25), "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", ("Shift", 2.75)],
        [("Ctrl", 1.25), ("Win", 1.25), ("Alt", 1.25), ("Space", 6.25), ("Alt", 1.25),
         ("Win", 1.25), ("Menu", 1.25), ("Ctrl", 1.25)],
    ]
    for name, x, width in row0:
        keys.append((name, x, 0, width, 1))
    for row_number, row in enumerate(rows):
        x = 0
        y = row_number + 1.25          # small gap under the F-key row
        for item in row:
            if isinstance(item, tuple):
                name, width = item
            else:
                name, width = item, 1
            keys.append((name, x, y, width, 1))
            x = x + width
    # navigation block and arrows
    for name, x, y in [("PrtScn", 15.25, 0), ("ScrollLock", 16.25, 0), ("Pause", 17.25, 0),
                       ("Insert", 15.25, 1.25), ("Home", 16.25, 1.25), ("PageUp", 17.25, 1.25),
                       ("Delete", 15.25, 2.25), ("End", 16.25, 2.25), ("PageDown", 17.25, 2.25),
                       ("Up", 16.25, 4.25), ("Left", 15.25, 5.25), ("Down", 16.25, 5.25),
                       ("Right", 17.25, 5.25)]:
        keys.append((name, x, y, 1, 1))
    # number pad
    pad = [("NumLock", 0, 0), ("Numpad /", 1, 0), ("Numpad *", 2, 0), ("Numpad -", 3, 0),
           ("Numpad 7", 0, 1), ("Numpad 8", 1, 1), ("Numpad 9", 2, 1),
           ("Numpad 4", 0, 2), ("Numpad 5", 1, 2), ("Numpad 6", 2, 2),
           ("Numpad 1", 0, 3), ("Numpad 2", 1, 3), ("Numpad 3", 2, 3), ("Numpad .", 2, 4)]
    for name, x, y in pad:
        keys.append((name, 18.5 + x, 1.25 + y, 1, 1))
    keys.append(("Numpad +", 21.5, 2.25, 1, 2))
    keys.append(("Enter", 21.5, 4.25, 1, 2))
    keys.append(("Numpad 0", 18.5, 5.25, 2, 1))
    return keys


class OnScreenKeyboard(tk.Canvas):
    '''A keyboard drawn with create_rectangle / create_text. Keys can be lit up in colours.'''

    WIDTH_UNITS = 22.6
    HEIGHT_UNITS = 6.35

    def __init__(self, parent, colors, unit=36, bg_key="panel"):
        '''Draw the keyboard; unit = size of one key in pixels.'''
        super().__init__(parent, width=int(self.WIDTH_UNITS * unit), height=int(self.HEIGHT_UNITS * unit),
                         bg=colors[bg_key], highlightthickness=0)
        self.colors = colors
        self.unit = unit
        self.key_items = {}          # key name -> list of (rectangle id, text id)
        self.draw_keyboard()

    def draw_keyboard(self):
        '''Draw every key of the layout.'''
        self.delete("all")
        self.key_items = {}
        u = self.unit
        font_size = max(7, int(u / 4))
        for name, x, y, width, height in keyboard_layout():
            x0 = 4 + x * u
            y0 = 4 + y * u
            rect = self.create_rectangle(x0, y0, x0 + width * u - 4, y0 + height * u - 4,
                                         fill=self.colors["key_bg"], outline=self.colors["key_border"])
            label = KEY_LABELS.get(name, name.replace("Numpad ", ""))
            text = self.create_text(x0 + (width * u - 4) / 2, y0 + (height * u - 4) / 2, text=label,
                                    fill=self.colors["key_text"], font=(config.FONT_FAMILY, font_size))
            if name not in self.key_items:
                self.key_items[name] = []
            self.key_items[name].append((rect, text))

    def reset(self):
        '''Turn every key back to the normal colour.'''
        for name in self.key_items:
            self.color_key(name, self.colors["key_bg"], self.colors["key_text"])

    def color_key(self, name, fill, text_color="white"):
        '''Colour one key (both copies, e.g. left and right Shift).'''
        for rect, text in self.key_items.get(name, []):
            self.itemconfig(rect, fill=fill)
            self.itemconfig(text, fill=text_color)

    def highlight(self, names, fill):
        '''Colour a list of keys with the same colour.'''
        for name in names:
            self.color_key(name, fill)


# ---------------------------------------------------------------- scrollable frame

class ScrollableFrame(tk.Frame):
    '''A frame whose content can scroll up and down. Put widgets into self.inner.'''

    def __init__(self, parent, colors, bg_key="bg"):
        '''Create a Canvas + Scrollbar and a Frame inside the Canvas.'''
        super().__init__(parent, bg=colors[bg_key])
        self.canvas = tk.Canvas(self, bg=colors[bg_key], highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.inner = tk.Frame(self.canvas, bg=colors[bg_key])
        # NOTE (advanced): a Frame cannot scroll by itself, so it is placed inside a Canvas
        # with create_window(); the Canvas scrolls and the Frame moves with it.
        self.window_id = self.canvas.create_window(0, 0, window=self.inner, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.inner.bind("<Configure>", self.on_inner_resize)
        self.canvas.bind("<Configure>", self.on_canvas_resize)
        self.canvas.bind("<Enter>", self.start_wheel)
        self.canvas.bind("<Leave>", self.stop_wheel)

    def on_inner_resize(self, event):
        '''Update the scroll area when the content changes size.'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_resize(self, event):
        '''Make the inner frame as wide as the canvas.'''
        self.canvas.itemconfig(self.window_id, width=event.width)

    def start_wheel(self, event):
        '''Mouse is over the list: the mouse wheel scrolls it.'''
        self.canvas.bind_all("<MouseWheel>", self.on_wheel)

    def stop_wheel(self, event):
        '''Mouse left the list: stop listening to the wheel.'''
        self.canvas.unbind_all("<MouseWheel>")

    def on_wheel(self, event):
        '''Scroll 3 lines per wheel step (event.delta is 120 per step on Windows).'''
        self.canvas.yview_scroll(int(-event.delta / 120) * 3, "units")

    def scroll_to_top(self):
        '''Scroll back to the top of the list.'''
        self.canvas.yview_moveto(0)


# ---------------------------------------------------------------- toast popup

class Toast(tk.Toplevel):
    '''A small borderless window at the bottom-right of the app that closes itself.'''

    def __init__(self, root, title, message, color, duration=2500):
        '''Show the toast for `duration` milliseconds.'''
        super().__init__(root)
        self.overrideredirect(True)          # no title bar and no border
        self.attributes("-topmost", True)
        frame = tk.Frame(self, bg=color, padx=18, pady=12)
        frame.pack(fill="both", expand=True)
        tk.Label(frame, text=title, font=config.FONT_BOLD, bg=color, fg="white").pack(anchor="w")
        tk.Label(frame, text=message, font=config.FONT_NORMAL, bg=color, fg="white",
                 wraplength=300, justify="left").pack(anchor="w")
        self.update_idletasks()
        x = root.winfo_rootx() + root.winfo_width() - self.winfo_width() - 24
        y = root.winfo_rooty() + root.winfo_height() - self.winfo_height() - 24
        self.geometry("+%d+%d" % (x, y))
        self.after(duration, self.destroy)


# ---------------------------------------------------------------- canvas drawings

def draw_badge(canvas, x, y, size, initials, color, text_color="white"):
    '''Draw a round coloured badge with initials, centred at (x, y) (create_oval).'''
    half = size / 2
    canvas.create_oval(x - half, y - half, x + half, y + half, fill=color, outline="")
    font_size = max(8, int(size / 3.2))
    if len(initials) >= 3:
        font_size = max(7, int(size / 4))
    canvas.create_text(x, y, text=initials, fill=text_color, font=(config.FONT_FAMILY, font_size, "bold"))


def draw_star(canvas, cx, cy, radius, fill, outline=""):
    '''Draw a five-pointed star with create_polygon (10 corner points).'''
    points = []
    for i in range(10):
        if i % 2 == 0:
            r = radius
        else:
            r = radius * 0.45
        angle = math.radians(-90 + i * 36)
        points.append(cx + r * math.cos(angle))
        points.append(cy + r * math.sin(angle))
    return canvas.create_polygon(points, fill=fill, outline=outline, width=2)


def draw_heart(canvas, x, y, size, color):
    '''Draw a heart: two circles (create_oval) and a triangle (create_polygon).'''
    half = size / 2
    canvas.create_oval(x, y, x + half + 1, y + half + 1, fill=color, outline="")
    canvas.create_oval(x + half - 1, y, x + size, y + half + 1, fill=color, outline="")
    canvas.create_polygon(x + 0.6, y + half * 0.62, x + size - 0.6, y + half * 0.62,
                          x + half, y + size, fill=color, outline="")


def draw_flame(canvas, x, y, size, active=True):
    '''Draw a small flame (streak icon) with two smooth polygons.'''
    if active:
        outer, inner = "#ff7a18", "#ffd23f"
    else:
        outer, inner = "#6b6f85", "#9aa1bd"
    s = size
    canvas.create_polygon(x + s * 0.5, y, x + s * 0.95, y + s * 0.6, x + s * 0.75, y + s,
                          x + s * 0.25, y + s, x + s * 0.05, y + s * 0.6, x + s * 0.3, y + s * 0.35,
                          fill=outer, outline="", smooth=True)
    canvas.create_polygon(x + s * 0.5, y + s * 0.35, x + s * 0.72, y + s * 0.75, x + s * 0.5, y + s * 0.98,
                          x + s * 0.28, y + s * 0.75, fill=inner, outline="", smooth=True)


def style_chart(figure, axes_list, colors):
    '''Give a Matplotlib figure the colours of the current theme.'''
    figure.patch.set_facecolor(colors["chart_bg"])
    for ax in axes_list:
        ax.set_facecolor(colors["chart_bg"])
        ax.tick_params(colors=colors["text"])
        ax.title.set_color(colors["text"])
        ax.xaxis.label.set_color(colors["text"])
        ax.yaxis.label.set_color(colors["text"])
        for spine in ax.spines.values():
            spine.set_color(colors["key_border"])
