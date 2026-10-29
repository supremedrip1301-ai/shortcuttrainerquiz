'''
notepad_paint.py - Windows 11 Notepad and Microsoft Paint shortcuts.
Every action starts with "Notepad:" or "Paint:" so it is clear which app it belongs to.
(Both apps share some combos, so each combo is listed only once.)
'''

SHORTCUTS = [
    # ---------- Notepad: files and tabs ----------
    {"keys": "Ctrl+N", "action": "Notepad: Open a new tab", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+N", "action": "Notepad: Open a new window", "category": "Notepad", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Notepad: Open a file", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Notepad: Save the file", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "Notepad: Save the file as a new name", "category": "Notepad", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+S", "action": "Notepad: Save all open tabs", "category": "Notepad", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Notepad: Print the file", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Tab", "action": "Notepad: Go to the next tab", "category": "Notepad", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+Tab", "action": "Notepad: Go to the previous tab", "category": "Notepad", "difficulty": "medium", "mode": "press"},

    # ---------- Notepad: editing ----------
    {"keys": "Ctrl+F", "action": "Notepad: Find text", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "F3", "action": "Notepad: Find the next match", "category": "Notepad", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F3", "action": "Notepad: Find the previous match", "category": "Notepad", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+H", "action": "Notepad: Find and replace", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+G", "action": "Notepad: Go to a line number", "category": "Notepad", "difficulty": "medium", "mode": "press"},
    {"keys": "F5", "action": "Notepad: Insert the current time and date", "category": "Notepad", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+=", "action": "Notepad: Zoom in", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+-", "action": "Notepad: Zoom out", "category": "Notepad", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+0", "action": "Notepad: Restore the default zoom", "category": "Notepad", "difficulty": "medium", "mode": "press"},

    # ---------- Paint ----------
    {"keys": "F12", "action": "Paint: Save the picture as a new file", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Paint: Open Image properties", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+W", "action": "Paint: Resize and skew the picture", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+X", "action": "Paint: Crop the picture to the selection", "category": "Paint", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Paint: Show or hide the rulers", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+PageUp", "action": "Paint: Zoom in", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+PageDown", "action": "Paint: Zoom out", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "F11", "action": "Paint: View the picture in full screen", "category": "Paint", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Paint: Make the selected text bold", "category": "Paint", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Paint: Make the selected text italic", "category": "Paint", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+U", "action": "Paint: Underline the selected text", "category": "Paint", "difficulty": "easy", "mode": "press"},
]
