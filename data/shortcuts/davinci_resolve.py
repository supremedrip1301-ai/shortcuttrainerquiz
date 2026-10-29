'''
davinci_resolve.py - DaVinci Resolve (version 18 / 19, Windows, default keyboard layout).
Most shortcuts are for the Edit page; node shortcuts are for the Color page.
'''

SHORTCUTS = [
    # ---------- Playback ----------
    {"keys": "Space", "action": "Play or stop", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "J", "action": "Play in reverse", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "K", "action": "Stop playback", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "L", "action": "Play forward", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Left", "action": "Go back one frame", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Right", "action": "Go forward one frame", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Up", "action": "Go to the previous edit point", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Down", "action": "Go to the next edit point", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Home", "action": "Go to the start of the timeline", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "End", "action": "Go to the end of the timeline", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Q", "action": "Switch between source and timeline viewer", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F", "action": "Show the viewer in full screen", "category": "Playback", "difficulty": "medium", "mode": "press"},

    # ---------- Marking ----------
    {"keys": "I", "action": "Mark the In point", "category": "Marking", "difficulty": "easy", "mode": "press"},
    {"keys": "O", "action": "Mark the Out point", "category": "Marking", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+X", "action": "Clear both In and Out points", "category": "Marking", "difficulty": "medium", "mode": "press"},
    {"keys": "X", "action": "Mark the clip under the playhead", "category": "Marking", "difficulty": "medium", "mode": "press"},
    {"keys": "M", "action": "Add a marker", "category": "Marking", "difficulty": "easy", "mode": "press"},

    # ---------- Edit modes and editing ----------
    {"keys": "A", "action": "Selection mode (pointer)", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "B", "action": "Blade edit mode", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "T", "action": "Trim edit mode", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Split (razor) the clip at the playhead", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Backspace", "action": "Delete the selected clips (leave a gap)", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Backspace", "action": "Ripple delete the selected clips", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "N", "action": "Turn snapping on or off", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+L", "action": "Turn linked selection on or off", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "D", "action": "Enable or disable the selected clip", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+T", "action": "Add the default transition", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Show the retime controls", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "F9", "action": "Insert edit", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "F10", "action": "Overwrite edit", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "F11", "action": "Replace edit", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "F12", "action": "Place on top edit", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+F10", "action": "Ripple overwrite edit", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+F12", "action": "Append the clip at the end of the timeline", "category": "Editing", "difficulty": "hard", "mode": "press"},

    # ---------- Timeline view ----------
    {"keys": "Shift+Z", "action": "Zoom the timeline to fit", "category": "Timeline View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+=", "action": "Zoom in on the timeline", "category": "Timeline View", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+-", "action": "Zoom out on the timeline", "category": "Timeline View", "difficulty": "easy", "mode": "press"},

    # ---------- Pages ----------
    {"keys": "Shift+2", "action": "Open the Media page", "category": "Pages", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+3", "action": "Open the Cut page", "category": "Pages", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+4", "action": "Open the Edit page", "category": "Pages", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+5", "action": "Open the Fusion page", "category": "Pages", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+6", "action": "Open the Color page", "category": "Pages", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+7", "action": "Open the Fairlight (audio) page", "category": "Pages", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+8", "action": "Open the Deliver page", "category": "Pages", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+9", "action": "Open Project Settings", "category": "Pages", "difficulty": "hard", "mode": "press"},

    # ---------- Color page ----------
    {"keys": "Alt+S", "action": "Add a serial node", "category": "Color Page", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+P", "action": "Add a parallel node", "category": "Color Page", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+L", "action": "Add a layer node", "category": "Color Page", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+D", "action": "Bypass all color grades", "category": "Color Page", "difficulty": "hard", "mode": "press"},

    # ---------- Project ----------
    {"keys": "Ctrl+N", "action": "Create a new timeline", "category": "Project", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+N", "action": "Create a new bin", "category": "Project", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Import media", "category": "Project", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the project", "category": "Project", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Z", "action": "Undo", "category": "Project", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+Z", "action": "Redo", "category": "Project", "difficulty": "medium", "mode": "press"},
]
