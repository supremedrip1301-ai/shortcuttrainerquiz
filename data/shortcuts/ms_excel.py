'''
ms_excel.py - Microsoft Excel (Microsoft 365 / Excel 2021, Windows) shortcuts.
Note: Excel's "Ctrl+Plus" (insert cells) is the "=" key with Shift, so it is "Ctrl+Shift+=".
'''

SHORTCUTS = [
    # ---------- Workbook ----------
    {"keys": "Ctrl+N", "action": "Create a new blank workbook", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Open a workbook", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the workbook", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "F12", "action": "Open the Save As dialog", "category": "File", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Print / open print preview", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+W", "action": "Close the workbook", "category": "File", "difficulty": "easy", "mode": "press"},

    # ---------- Navigation ----------
    {"keys": "Ctrl+Home", "action": "Go to cell A1", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+End", "action": "Go to the last used cell", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Up", "action": "Jump to the top edge of the data region", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Down", "action": "Jump to the bottom edge of the data region", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+PageDown", "action": "Move to the next worksheet", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+PageUp", "action": "Move to the previous worksheet", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+G", "action": "Open the Go To dialog", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+PageDown", "action": "Move one screen to the right", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+PageUp", "action": "Move one screen to the left", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Backspace", "action": "Scroll to show the active cell", "category": "Navigation", "difficulty": "hard", "mode": "press"},

    # ---------- Selection ----------
    {"keys": "Ctrl+Space", "action": "Select the entire column", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Space", "action": "Select the entire row", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+A", "action": "Select the current region / whole sheet", "category": "Selection", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+Down", "action": "Extend the selection to the last filled cell below", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+Right", "action": "Extend the selection to the last filled cell right", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+End", "action": "Extend the selection to the last used cell", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+F8", "action": "Add non-adjacent cells to the selection", "category": "Selection", "difficulty": "hard", "mode": "press"},

    # ---------- Editing cells ----------
    {"keys": "F2", "action": "Edit the active cell", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+Enter", "action": "Start a new line inside the same cell", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Enter", "action": "Fill the selected cells with the current entry", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+D", "action": "Fill down from the cell above", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Fill right from the cell on the left", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Use Flash Fill", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+;", "action": "Insert today's date", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+;", "action": "Insert the current time", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+'", "action": "Copy the formula from the cell above", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+V", "action": "Open Paste Special", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+=", "action": "Insert cells, rows or columns", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+-", "action": "Delete cells, rows or columns", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F11", "action": "Insert a new worksheet", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+F", "action": "Find text in the sheet", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+H", "action": "Find and replace", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+9", "action": "Hide the selected rows", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+0", "action": "Hide the selected columns", "category": "Editing", "difficulty": "hard", "mode": "press"},

    # ---------- Formatting ----------
    {"keys": "Ctrl+1", "action": "Open the Format Cells dialog", "category": "Formatting", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Make the cell text bold", "category": "Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Make the cell text italic", "category": "Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+U", "action": "Underline the cell text", "category": "Formatting", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+5", "action": "Apply strikethrough", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+4", "action": "Apply the Currency format", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+5", "action": "Apply the Percentage format", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+1", "action": "Apply the Number format (2 decimals)", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+3", "action": "Apply the Date format", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+`", "action": "Apply the General number format", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+7", "action": "Add an outline border to the cells", "category": "Formatting", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+-", "action": "Remove the outline border", "category": "Formatting", "difficulty": "hard", "mode": "press"},

    # ---------- Formulas and data ----------
    {"keys": "Alt+=", "action": "Insert the AutoSum formula", "category": "Formulas", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F3", "action": "Open the Insert Function dialog", "category": "Formulas", "difficulty": "medium", "mode": "press"},
    {"keys": "F4", "action": "Switch absolute / relative reference ($)", "category": "Formulas", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+`", "action": "Show formulas instead of values", "category": "Formulas", "difficulty": "hard", "mode": "press"},
    {"keys": "F9", "action": "Calculate all open workbooks", "category": "Formulas", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F3", "action": "Open the Name Manager", "category": "Formulas", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+T", "action": "Create a table", "category": "Data", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+L", "action": "Turn filters on or off", "category": "Data", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+F1", "action": "Create a chart on the same sheet", "category": "Data", "difficulty": "hard", "mode": "press"},
    {"keys": "F11", "action": "Create a chart on a new chart sheet", "category": "Data", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+K", "action": "Insert a hyperlink", "category": "Data", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F2", "action": "Add or edit a cell note", "category": "Data", "difficulty": "hard", "mode": "press"},
    {"keys": "F7", "action": "Check spelling", "category": "Data", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+F1", "action": "Show or hide the ribbon", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+F11", "action": "Open the Visual Basic (VBA) editor", "category": "View", "difficulty": "hard", "mode": "press"},
]
