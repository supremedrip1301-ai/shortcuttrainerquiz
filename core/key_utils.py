'''
key_utils.py - helper functions for key names and key combos.

Every shortcut in this project is written in ONE canonical (standard) text form:
    modifiers in the order Ctrl, Alt, Shift, Win, then the main key   ->  "Ctrl+Shift+N"
    two-step chords are joined with a comma and a space               ->  "Ctrl+K, Ctrl+C"
The functions below turn Tkinter key events and typed text into this form,
so that a pressed combo can be compared with the expected combo.

Decision about the "plus" key: the key next to Backspace is called "=" here
(so "Zoom in" is stored as "Ctrl+="). While checking answers "Ctrl+Plus", "Ctrl++",
"Ctrl+=" and "Ctrl+Numpad +" are all treated as the same answer.
'''

import time

# Tuple (fixed order) of the four modifier keys.
MODIFIER_ORDER = ("Ctrl", "Alt", "Shift", "Win")

# Special (non-letter) keys that may be used in the data files (tuple = fixed list).
SPECIAL_KEYS = ("Ctrl", "Alt", "Shift", "Win", "Tab", "Enter", "Esc", "Space", "Backspace",
                "Delete", "Insert", "Home", "End", "PageUp", "PageDown", "Up", "Down", "Left",
                "Right", "PrtScn", "CapsLock", "Menu", "NumLock", "ScrollLock", "Pause")


def build_vk_names():
    '''Return a dictionary: Windows virtual-key code -> canonical key name.'''
    names = {}
    for code in range(65, 91):                     # 65-90 -> A-Z
        names[code] = chr(code)
    for code in range(48, 58):                     # 48-57 -> 0-9
        names[code] = chr(code)
    for code in range(96, 106):                    # 96-105 -> Numpad 0-9
        names[code] = "Numpad " + str(code - 96)
    for code in range(112, 124):                   # 112-123 -> F1-F12
        names[code] = "F" + str(code - 111)
    names.update({106: "Numpad *", 107: "Numpad +", 109: "Numpad -", 110: "Numpad .",
                  111: "Numpad /", 186: ";", 187: "=", 188: ",", 189: "-", 190: ".",
                  191: "/", 192: "`", 219: "[", 220: "\\", 221: "]", 222: "'",
                  8: "Backspace", 9: "Tab", 13: "Enter", 27: "Esc", 32: "Space",
                  33: "PageUp", 34: "PageDown", 35: "End", 36: "Home", 37: "Left",
                  38: "Up", 39: "Right", 40: "Down", 44: "PrtScn", 45: "Insert",
                  46: "Delete", 20: "CapsLock", 93: "Menu"})
    return names


# NOTE (advanced): on Windows, Tkinter's event.keycode is the virtual-key code (vk).
# It is used instead of event.char, because while Ctrl is held event.char is a control
# character (like '\x01' for A), and with Shift it changes ('!' instead of '1').
VK_NAMES = build_vk_names()

# Different ways people write a key -> canonical name (all lower case on the left).
ALIASES = {
    "control": "Ctrl", "ctrl": "Ctrl", "alt": "Alt", "option": "Alt", "shift": "Shift",
    "win": "Win", "windows": "Win", "cmd": "Win", "meta": "Win", "super": "Win",
    "esc": "Esc", "escape": "Esc", "enter": "Enter", "return": "Enter",
    "del": "Delete", "delete": "Delete", "ins": "Insert", "insert": "Insert",
    "pgup": "PageUp", "pageup": "PageUp", "page up": "PageUp", "prior": "PageUp",
    "pgdn": "PageDown", "pagedown": "PageDown", "page down": "PageDown", "next": "PageDown",
    "space": "Space", "spacebar": "Space", "tab": "Tab", "backspace": "Backspace",
    "home": "Home", "end": "End", "up": "Up", "down": "Down", "left": "Left", "right": "Right",
    "prtscn": "PrtScn", "prtsc": "PrtScn", "printscreen": "PrtScn", "print": "PrtScn",
    "capslock": "CapsLock", "caps_lock": "CapsLock", "menu": "Menu", "app": "Menu",
    "plus": "=", "equal": "=", "minus": "-", "comma": ",", "period": ".", "slash": "/",
}

# Keys that count as the same key when answers are compared.
EQUIVALENT_KEYS = {"Numpad +": "=", "Numpad -": "-"}

# Every key name that is allowed inside the data files (a set: fast "in" checks).
ALLOWED_KEY_NAMES = set(SPECIAL_KEYS) | set(VK_NAMES.values())

# System combos that Windows itself captures -> these shortcuts must be "mcq" mode.
# Ctrl+Alt+Arrow keys are in the list because some graphics drivers rotate the screen with them.
SYSTEM_COMBOS = {"Alt+Tab", "Alt+Shift+Tab", "Alt+Esc", "Ctrl+Esc", "Ctrl+Alt+Delete",
                 "Ctrl+Shift+Esc", "Alt+Space", "Alt+F4", "Ctrl+Alt+Tab",
                 "Ctrl+Alt+Up", "Ctrl+Alt+Down", "Ctrl+Alt+Left", "Ctrl+Alt+Right"}


def is_modifier(name):
    '''Return True if the canonical key name is Ctrl, Alt, Shift or Win.'''
    return name in MODIFIER_ORDER


def build_combo(modifiers, main_key):
    '''Join a set of held modifiers and one main key in the canonical order.'''
    parts = []
    for name in MODIFIER_ORDER:      # this loop keeps Ctrl, Alt, Shift, Win in order
        if name in modifiers:
            parts.append(name)
    parts.append(main_key)
    return "+".join(parts)


def split_chord(combo_text):
    '''Split "Ctrl+K, Ctrl+C" into a list of steps: ["Ctrl+K", "Ctrl+C"].'''
    steps = []
    for step in combo_text.split(", "):
        if step.strip() != "":
            steps.append(step.strip())
    return steps


def split_step(step_text):
    '''Split one step like "Ctrl+Numpad +" into key names: ["Ctrl", "Numpad +"].'''
    pieces = step_text.split("+")
    keys = []
    i = 0
    while i < len(pieces):
        piece = pieces[i].strip()
        if piece == "" and i + 1 < len(pieces) and pieces[i + 1].strip() == "":
            keys.append("Plus")          # "Ctrl++" -> the plus key itself
            i = i + 2
            continue
        if pieces[i].endswith("Numpad ") and i + 1 < len(pieces) and pieces[i + 1] == "":
            keys.append("Numpad +")      # "Numpad +" contains a "+" sign itself
            i = i + 2
            continue
        if piece != "":
            keys.append(piece)
        i = i + 1
    return keys


def normalize_key_name(text):
    '''Return the canonical name of one typed key name ("ctrl" -> "Ctrl", "a" -> "A").'''
    clean = text.strip()
    lower = clean.lower()
    if lower in ALIASES:
        return ALIASES[lower]
    if lower.startswith("numpad"):
        return "Numpad " + clean[6:].strip()
    if len(lower) >= 2 and lower[0] == "f" and lower[1:].isdigit():
        return "F" + lower[1:]
    if len(clean) == 1:
        return clean.upper()
    return clean


def normalize_step(step_text):
    '''Return one step in canonical order, e.g. "shift+ctrl+n" -> "Ctrl+Shift+N".'''
    modifiers = set()
    main_key = ""
    for piece in split_step(step_text):
        name = normalize_key_name(piece)
        if is_modifier(name):
            modifiers.add(name)
        else:
            main_key = name
    if main_key == "":                 # a step made only of modifiers, e.g. "Ctrl+Shift"
        return "+".join([m for m in MODIFIER_ORDER if m in modifiers])
    return build_combo(modifiers, main_key)


def normalize_combo_text(combo_text):
    '''Return any combo text in the canonical form (works for chords too).'''
    steps = []
    for step in split_chord(combo_text):
        steps.append(normalize_step(step))
    return ", ".join(steps)


def step_to_key_set(step_text):
    '''Return a set of key names for one step, with equivalent keys made equal.'''
    keys = set()
    for name in split_step(normalize_step(step_text)):
        if name in EQUIVALENT_KEYS:
            name = EQUIVALENT_KEYS[name]
        keys.add(name)
    return keys


def steps_match(pressed_step, expected_step):
    '''Compare two single steps as SETS of keys (order does not matter).'''
    return step_to_key_set(pressed_step) == step_to_key_set(expected_step)


def combos_match(pressed_text, expected_text):
    '''Return True if the pressed combo (maybe a chord) equals the expected one.'''
    pressed_steps = split_chord(pressed_text)
    expected_steps = split_chord(expected_text)
    if len(pressed_steps) != len(expected_steps):
        return False
    for i in range(len(expected_steps)):
        if not steps_match(pressed_steps[i], expected_steps[i]):
            return False
    return True


def combo_to_key_list(combo_text):
    '''Return a list of steps, each step a list of key names (used to draw key caps).'''
    result = []
    for step in split_chord(combo_text):
        result.append(split_step(step))
    return result


def format_combo_for_display(combo_text):
    '''Return a friendly text like "Ctrl + K  then  Ctrl + C" (uses map with lambda).'''
    steps = split_chord(combo_text)
    # map() runs the lambda on every step: "Ctrl+K" -> "Ctrl + K"
    pretty_steps = list(map(lambda step: " + ".join(split_step(step)), steps))
    return "  then  ".join(pretty_steps)


def get_main_keys(combo_text):
    '''Return a list with the main (non-modifier) key of every step (used for hints).'''
    main_keys = []
    for step in combo_to_key_list(combo_text):
        for name in step:
            if not is_modifier(name):
                main_keys.append(name)
    return main_keys


def is_system_combo(combo_text):
    '''Return True if Windows itself catches this combo (Win key, Alt+Tab, PrtScn, ...).'''
    for step in split_chord(combo_text):
        keys = split_step(step)
        if "Win" in keys or "PrtScn" in keys:
            return True
        if normalize_step(step) in SYSTEM_COMBOS:
            return True
    return False


# ---------------- Tkinter key events (real key detection) ----------------
# NOTE (advanced): Tkinter puts the held modifiers into event.state as bit flags.
# On Windows: Shift = 0x0001, Ctrl = 0x0004, Alt = 0x20000 (0x0008 is Num Lock there).
TK_SHIFT_MASK = 0x0001
TK_CTRL_MASK = 0x0004
TK_ALT_MASK = 0x20000

TK_MODIFIER_KEYSYMS = {"Control_L": "Ctrl", "Control_R": "Ctrl", "Alt_L": "Alt", "Alt_R": "Alt",
                       "Shift_L": "Shift", "Shift_R": "Shift", "Win_L": "Win", "Win_R": "Win",
                       "Super_L": "Win", "Super_R": "Win"}


def modifiers_from_tk_state(state):
    '''Read Ctrl / Alt / Shift from a Tkinter event.state number (bit masks).'''
    modifiers = set()
    if state & TK_CTRL_MASK:
        modifiers.add("Ctrl")
    if state & TK_ALT_MASK:
        modifiers.add("Alt")
    if state & TK_SHIFT_MASK:
        modifiers.add("Shift")
    return modifiers


def name_from_tk_event(keysym, keycode):
    '''Turn a Tkinter KeyPress event (keysym + keycode) into a canonical key name.

    On Windows event.keycode is the Windows virtual-key code (see VK_NAMES).'''
    if keysym in TK_MODIFIER_KEYSYMS:
        return TK_MODIFIER_KEYSYMS[keysym]
    if keycode in VK_NAMES:
        return VK_NAMES[keycode]
    return normalize_key_name(keysym)


class ChordTracker:
    '''Remembers the first step of a two-step chord (like "Ctrl+K, Ctrl+C") for a short time.'''

    def __init__(self, timeout=1.5):
        '''timeout = seconds to wait for the second step.'''
        self.timeout = timeout
        self.first_step = ""
        self.first_time = 0.0

    def reset(self):
        '''Forget the remembered first step.'''
        self.first_step = ""
        self.first_time = 0.0

    def add_step(self, combo, expected, now=None):
        '''Give one pressed combo. Returns (finished, answer_text).

        finished is False when the combo was the first step of the expected chord
        and the app should wait for the second step.'''
        if now is None:
            now = time.time()
        if self.first_step != "" and now - self.first_time <= self.timeout:
            answer = self.first_step + ", " + combo
            self.reset()
            return True, answer
        self.reset()
        expected_steps = split_chord(expected)
        if len(expected_steps) > 1 and steps_match(combo, expected_steps[0]):
            self.first_step = combo
            self.first_time = now
            return False, combo
        return True, combo
