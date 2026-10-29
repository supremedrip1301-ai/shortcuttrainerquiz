'''
ms_powerpoint.py - Microsoft PowerPoint (Microsoft 365 / PowerPoint 2021, Windows) shortcuts.
'''

SHORTCUTS = [
    # ---------- File ----------
    {"keys": "Ctrl+N", "action": "Create a new presentation", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Open a presentation", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the presentation", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "F12", "action": "Open the Save As dialog", "category": "File", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Print the presentation", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+W", "action": "Close the presentation", "category": "File", "difficulty": "easy", "mode": "press"},

    # ---------- Slides ----------
    {"keys": "Ctrl+M", "action": "Insert a new slide", "category": "Slides", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+D", "action": "Duplicate the selected slide or object", "category": "Slides", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Up", "action": "Move the selected slide up", "category": "Slides", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Down", "action": "Move the selected slide down", "category": "Slides", "difficulty": "hard", "mode": "press"},

    # ---------- Slide show ----------
    {"keys": "F5", "action": "Start the slide show from the beginning", "category": "Slide Show", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+F5", "action": "Start the slide show from the current slide", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+F5", "action": "Start the slide show in Presenter View", "category": "Slide Show", "difficulty": "hard", "mode": "press"},
    {"keys": "Esc", "action": "End the slide show", "category": "Slide Show", "difficulty": "easy", "mode": "press"},
    {"keys": "N", "action": "Go to the next slide (slide show)", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "P", "action": "Go to the previous slide (slide show)", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "Home", "action": "Go to the first slide (slide show)", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "End", "action": "Go to the last slide (slide show)", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "B", "action": "Show a black screen (slide show)", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "W", "action": "Show a white screen (slide show)", "category": "Slide Show", "difficulty": "medium", "mode": "press"},
    {"keys": "E", "action": "Erase drawings on the screen (slide show)", "category": "Slide Show", "difficulty": "hard", "mode": "press"},
    {"keys": "S", "action": "Stop or restart an automatic show", "category": "Slide Show", "difficulty": "hard", "mode": "press"},

    # ---------- Objects ----------
    {"keys": "Ctrl+G", "action": "Group the selected objects", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+G", "action": "Ungroup the selected group", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+]", "action": "Bring the object to the front", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+[", "action": "Send the object to the back", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Copy formatting", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+V", "action": "Paste formatting", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+V", "action": "Open Paste Special", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+K", "action": "Insert a hyperlink", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+M", "action": "Insert a new comment", "category": "Objects", "difficulty": "hard", "mode": "press"},

    # ---------- Text formatting ----------
    {"keys": "Ctrl+B", "action": "Make text bold", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Make text italic", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+U", "action": "Underline text", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Center the paragraph", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+L", "action": "Align the paragraph left", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Align the paragraph right", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+J", "action": "Justify the paragraph", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+T", "action": "Open the Font dialog", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+.", "action": "Increase the font size", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+,", "action": "Decrease the font size", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+=", "action": "Apply subscript", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+=", "action": "Apply superscript", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+F3", "action": "Change the case of letters", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Space", "action": "Remove manual character formatting", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Shift+Left", "action": "Promote a paragraph (move left one level)", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Shift+Right", "action": "Demote a paragraph (move right one level)", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},

    # ---------- Review and view ----------
    {"keys": "Ctrl+F", "action": "Find text", "category": "Review & View", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+H", "action": "Replace text", "category": "Review & View", "difficulty": "medium", "mode": "press"},
    {"keys": "F7", "action": "Check spelling", "category": "Review & View", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F9", "action": "Show or hide the gridlines", "category": "Review & View", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+F9", "action": "Show or hide the guides", "category": "Review & View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F1", "action": "Show or hide the ribbon", "category": "Review & View", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Q", "action": "Go to the Search (Tell me) box", "category": "Review & View", "difficulty": "medium", "mode": "press"},
]
