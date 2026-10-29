'''
ms_word.py - Microsoft Word (Microsoft 365 / Word 2021, Windows) shortcuts.
Note: "Ctrl+=" is the key next to Backspace (written Ctrl+Plus in some guides).
'''

SHORTCUTS = [
    # ---------- File ----------
    {"keys": "Ctrl+N", "action": "Create a new blank document", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Open a document", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the document", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "F12", "action": "Open the Save As dialog", "category": "File", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Print the document", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+W", "action": "Close the document", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+F2", "action": "Show the print preview", "category": "File", "difficulty": "hard", "mode": "press"},

    # ---------- Edit and find ----------
    {"keys": "Ctrl+F", "action": "Search in the Navigation pane", "category": "Edit", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+H", "action": "Find and replace text", "category": "Edit", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+G", "action": "Go to a page, section or bookmark", "category": "Edit", "difficulty": "medium", "mode": "press"},
    {"keys": "F4", "action": "Repeat the last action", "category": "Edit", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+V", "action": "Open Paste Special", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Copy formatting", "category": "Edit", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+V", "action": "Paste formatting", "category": "Edit", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Shift+Up", "action": "Move the paragraph up", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Shift+Down", "action": "Move the paragraph down", "category": "Edit", "difficulty": "hard", "mode": "press"},

    # ---------- Character formatting ----------
    {"keys": "Ctrl+B", "action": "Make text bold", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Make text italic", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+U", "action": "Underline text", "category": "Text Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+D", "action": "Double underline text", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+=", "action": "Apply subscript", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+=", "action": "Apply superscript", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+]", "action": "Increase font size by 1 point", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+[", "action": "Decrease font size by 1 point", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+.", "action": "Increase font size to the next size", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+,", "action": "Decrease font size to the previous size", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+D", "action": "Open the Font dialog", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F3", "action": "Change the case of letters", "category": "Text Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+A", "action": "Format letters as all capitals", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+K", "action": "Format letters as small capitals", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Space", "action": "Remove manual character formatting", "category": "Text Formatting", "difficulty": "hard", "mode": "press"},

    # ---------- Paragraph formatting ----------
    {"keys": "Ctrl+E", "action": "Center the paragraph", "category": "Paragraph", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+L", "action": "Align the paragraph left", "category": "Paragraph", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Align the paragraph right", "category": "Paragraph", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+J", "action": "Justify the paragraph", "category": "Paragraph", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+1", "action": "Set single line spacing", "category": "Paragraph", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+2", "action": "Set double line spacing", "category": "Paragraph", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+5", "action": "Set 1.5 line spacing", "category": "Paragraph", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+M", "action": "Indent the paragraph", "category": "Paragraph", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+M", "action": "Remove a paragraph indent", "category": "Paragraph", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+T", "action": "Create a hanging indent", "category": "Paragraph", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Q", "action": "Remove paragraph formatting", "category": "Paragraph", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+8", "action": "Show or hide formatting marks", "category": "Paragraph", "difficulty": "medium", "mode": "press"},

    # ---------- Styles ----------
    {"keys": "Ctrl+Alt+1", "action": "Apply the Heading 1 style", "category": "Styles", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+2", "action": "Apply the Heading 2 style", "category": "Styles", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+3", "action": "Apply the Heading 3 style", "category": "Styles", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+N", "action": "Apply the Normal style", "category": "Styles", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+L", "action": "Apply the List Bullet style", "category": "Styles", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "Open the Apply Styles pane", "category": "Styles", "difficulty": "hard", "mode": "press"},

    # ---------- Insert ----------
    {"keys": "Ctrl+K", "action": "Insert a hyperlink", "category": "Insert", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Enter", "action": "Insert a page break", "category": "Insert", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+Enter", "action": "Insert a column break", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+Enter", "action": "Insert a line break", "category": "Insert", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+C", "action": "Insert the copyright symbol", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+T", "action": "Insert the trademark symbol", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+R", "action": "Insert the registered trademark symbol", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+M", "action": "Insert a comment", "category": "Insert", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+F", "action": "Insert a footnote", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+D", "action": "Insert an endnote", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Shift+D", "action": "Insert the current date", "category": "Insert", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Shift+T", "action": "Insert the current time", "category": "Insert", "difficulty": "hard", "mode": "press"},

    # ---------- Review ----------
    {"keys": "F7", "action": "Check spelling and grammar", "category": "Review", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+F7", "action": "Open the Thesaurus", "category": "Review", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+E", "action": "Turn Track Changes on or off", "category": "Review", "difficulty": "medium", "mode": "press"},

    # ---------- View and navigation ----------
    {"keys": "Ctrl+Alt+P", "action": "Switch to Print Layout view", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+O", "action": "Switch to Outline view", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+N", "action": "Switch to Draft view", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F1", "action": "Show or hide the ribbon", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Home", "action": "Go to the start of the document", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+End", "action": "Go to the end of the document", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Up", "action": "Move to the previous paragraph", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Down", "action": "Move to the next paragraph", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F5", "action": "Go back to the last edit location", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Q", "action": "Go to the Search (Tell me) box", "category": "Navigation", "difficulty": "medium", "mode": "press"},

    # ---------- Fields and macros ----------
    {"keys": "F9", "action": "Update the selected fields", "category": "Fields & Macros", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F9", "action": "Insert empty field braces", "category": "Fields & Macros", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+F9", "action": "Switch between field codes and results", "category": "Fields & Macros", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+F8", "action": "Open the Macros dialog", "category": "Fields & Macros", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+F11", "action": "Open the Visual Basic (VBA) editor", "category": "Fields & Macros", "difficulty": "hard", "mode": "press"},
]
