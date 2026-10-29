'''
windows_general.py - Windows 11 general and desktop shortcuts.

Every combo that uses the Win key, or that Windows itself catches (Alt+Tab, Alt+F4,
Ctrl+Shift+Esc, PrtScn, ...), has mode "mcq", because it cannot be pressed inside our app.
Key order is always Ctrl, Alt, Shift, Win, then the main key (so Win+Ctrl+D is "Ctrl+Win+D").
'''

SHORTCUTS = [
    # ---------- Editing (work in almost every app) ----------
    {"keys": "Ctrl+C", "action": "Copy the selected item", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+X", "action": "Cut the selected item", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+V", "action": "Paste the copied item", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Z", "action": "Undo the last action", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Y", "action": "Redo the last undone action", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+A", "action": "Select all items or all text", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Backspace", "action": "Delete the previous word", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Delete", "action": "Delete the next word", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Left", "action": "Move the cursor to the previous word", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Right", "action": "Move the cursor to the next word", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+Left", "action": "Select the previous word", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+Right", "action": "Select the next word", "category": "Editing", "difficulty": "hard", "mode": "press"},

    # ---------- General ----------
    {"keys": "Esc", "action": "Stop or leave the current task", "category": "General", "difficulty": "easy", "mode": "press"},
    {"keys": "F5", "action": "Refresh the active window", "category": "General", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+F10", "action": "Open the right-click menu of the selection", "category": "General", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+F4", "action": "Close the active document (in tabbed apps)", "category": "General", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+F4", "action": "Close the active app", "category": "General", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Ctrl+Shift+Esc", "action": "Open Task Manager", "category": "General", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Ctrl+Alt+Delete", "action": "Open the security options screen", "category": "General", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Alt+Space", "action": "Open the window menu of the active window", "category": "General", "difficulty": "hard", "mode": "mcq"},

    # ---------- Start, search and system ----------
    {"keys": "Win", "action": "Open or close the Start menu", "category": "Start & Search", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Ctrl+Esc", "action": "Open the Start menu (without Win key)", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+S", "action": "Open Windows Search", "category": "Start & Search", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+R", "action": "Open the Run dialog box", "category": "Start & Search", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+E", "action": "Open File Explorer", "category": "Start & Search", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+I", "action": "Open Settings", "category": "Start & Search", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+L", "action": "Lock your PC", "category": "Start & Search", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+X", "action": "Open the Quick Link (power user) menu", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+A", "action": "Open Quick Settings (Wi-Fi, volume...)", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+N", "action": "Open the notification center and calendar", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+W", "action": "Open Widgets", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+V", "action": "Open clipboard history", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+.", "action": "Open the emoji panel", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+H", "action": "Start voice typing", "category": "Start & Search", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+Pause", "action": "Open System > About in Settings", "category": "Start & Search", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+Space", "action": "Switch the input language / keyboard layout", "category": "Start & Search", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+U", "action": "Open Accessibility settings", "category": "Start & Search", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Ctrl+Shift+Win+B", "action": "Wake up / restart the graphics driver", "category": "Start & Search", "difficulty": "hard", "mode": "mcq"},

    # ---------- Window management ----------
    {"keys": "Alt+Tab", "action": "Switch between open apps", "category": "Window Management", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Ctrl+Alt+Tab", "action": "Show open apps and keep the switcher open", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Alt+Esc", "action": "Cycle through windows in the order opened", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+Tab", "action": "Open Task View", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+D", "action": "Show or hide the desktop", "category": "Window Management", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+M", "action": "Minimize all windows", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Shift+Win+M", "action": "Restore minimized windows on the desktop", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+,", "action": "Peek at the desktop for a moment", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+Up", "action": "Maximize the active window", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+Down", "action": "Restore down / minimize the active window", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+Left", "action": "Snap the window to the left half", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+Right", "action": "Snap the window to the right half", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+Z", "action": "Open snap layouts", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Shift+Win+Up", "action": "Stretch the window to the top and bottom", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Shift+Win+Left", "action": "Move the window to the monitor on the left", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Shift+Win+Right", "action": "Move the window to the monitor on the right", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+P", "action": "Choose a presentation / display mode", "category": "Window Management", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+K", "action": "Open Cast to connect a wireless display", "category": "Window Management", "difficulty": "hard", "mode": "mcq"},

    # ---------- Taskbar ----------
    {"keys": "Win+1", "action": "Open the first app pinned on the taskbar", "category": "Taskbar", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+T", "action": "Cycle through the apps on the taskbar", "category": "Taskbar", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+B", "action": "Set focus to the system tray (notification area)", "category": "Taskbar", "difficulty": "hard", "mode": "mcq"},

    # ---------- Virtual desktops ----------
    {"keys": "Ctrl+Win+D", "action": "Add a new virtual desktop", "category": "Virtual Desktops", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Ctrl+Win+Left", "action": "Switch to the virtual desktop on the left", "category": "Virtual Desktops", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Ctrl+Win+Right", "action": "Switch to the virtual desktop on the right", "category": "Virtual Desktops", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Ctrl+Win+F4", "action": "Close the current virtual desktop", "category": "Virtual Desktops", "difficulty": "hard", "mode": "mcq"},

    # ---------- Screenshots and recording ----------
    {"keys": "PrtScn", "action": "Take a screenshot (Snipping Tool)", "category": "Screenshots", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Shift+Win+S", "action": "Snip a part of the screen", "category": "Screenshots", "difficulty": "easy", "mode": "mcq"},
    {"keys": "Win+PrtScn", "action": "Save a full screenshot to the Pictures folder", "category": "Screenshots", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Alt+PrtScn", "action": "Copy a screenshot of the active window", "category": "Screenshots", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Win+G", "action": "Open Xbox Game Bar", "category": "Screenshots", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Alt+Win+R", "action": "Start or stop screen recording (Game Bar)", "category": "Screenshots", "difficulty": "hard", "mode": "mcq"},

    # ---------- Accessibility ----------
    {"keys": "Win+=", "action": "Open Magnifier and zoom in", "category": "Accessibility", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+-", "action": "Zoom out with Magnifier", "category": "Accessibility", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Win+Esc", "action": "Close Magnifier", "category": "Accessibility", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Ctrl+Win+Enter", "action": "Turn Narrator on or off", "category": "Accessibility", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Ctrl+Win+O", "action": "Open the on-screen keyboard", "category": "Accessibility", "difficulty": "hard", "mode": "mcq"},
]
