'''
python_idle_jupyter.py - Python IDLE (Windows) and Jupyter Notebook shortcuts.

Every action starts with "IDLE:" or "Jupyter:" so it is clear which program it belongs to.
Jupyter "command mode" shortcuts are single keys pressed after Esc (blue cell border).
Chords like "D, D" mean: press D two times quickly.
'''

SHORTCUTS = [
    # ---------- IDLE: files ----------
    {"keys": "Ctrl+N", "action": "IDLE: Create a new editor file", "category": "IDLE Editor", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+O", "action": "IDLE: Open a file", "category": "IDLE Editor", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "IDLE: Save the file", "category": "IDLE Editor", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "IDLE: Save the file with a new name", "category": "IDLE Editor", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Q", "action": "IDLE: Exit IDLE", "category": "IDLE Editor", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+M", "action": "IDLE: Open a module by name", "category": "IDLE Editor", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+C", "action": "IDLE: Open the Class / Module Browser", "category": "IDLE Editor", "difficulty": "hard", "mode": "press"},
    {"keys": "F1", "action": "IDLE: Open the Python documentation", "category": "IDLE Editor", "difficulty": "medium", "mode": "press"},

    # ---------- IDLE: run ----------
    {"keys": "F5", "action": "IDLE: Run the current module", "category": "IDLE Run", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+X", "action": "IDLE: Check the module for syntax errors", "category": "IDLE Run", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F6", "action": "IDLE: Restart the Shell", "category": "IDLE Run", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+C", "action": "IDLE: Interrupt the running program (Shell)", "category": "IDLE Run", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+P", "action": "IDLE: Previous command in the Shell history", "category": "IDLE Run", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+N", "action": "IDLE: Next command in the Shell history", "category": "IDLE Run", "difficulty": "medium", "mode": "press"},

    # ---------- IDLE: editing ----------
    {"keys": "Alt+3", "action": "IDLE: Comment out the selected region", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+4", "action": "IDLE: Uncomment the selected region", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+5", "action": "IDLE: Tabify the region (spaces to tabs)", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+6", "action": "IDLE: Untabify the region (tabs to spaces)", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+]", "action": "IDLE: Indent the selected region", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+[", "action": "IDLE: Dedent the selected region", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Q", "action": "IDLE: Format (re-wrap) the paragraph", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+/", "action": "IDLE: Expand a word you started typing", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Space", "action": "IDLE: Show code completions", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+\\", "action": "IDLE: Show the call tip of a function", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+G", "action": "IDLE: Go to a line number", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+F", "action": "IDLE: Find text", "category": "IDLE Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+G", "action": "IDLE: Find the next match again", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+H", "action": "IDLE: Find and replace", "category": "IDLE Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+2", "action": "IDLE: Zoom the window to full height", "category": "IDLE Editing", "difficulty": "hard", "mode": "press"},

    # ---------- Jupyter: run cells ----------
    {"keys": "Shift+Enter", "action": "Jupyter: Run the cell and select the next one", "category": "Jupyter Run", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Enter", "action": "Jupyter: Run the selected cell(s)", "category": "Jupyter Run", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+Enter", "action": "Jupyter: Run the cell and insert one below", "category": "Jupyter Run", "difficulty": "medium", "mode": "press"},
    {"keys": "I, I", "action": "Jupyter: Interrupt the kernel", "category": "Jupyter Run", "difficulty": "hard", "mode": "press"},
    {"keys": "0, 0", "action": "Jupyter: Restart the kernel", "category": "Jupyter Run", "difficulty": "hard", "mode": "press"},

    # ---------- Jupyter: command mode ----------
    {"keys": "Esc", "action": "Jupyter: Enter command mode", "category": "Jupyter Command Mode", "difficulty": "easy", "mode": "press"},
    {"keys": "Enter", "action": "Jupyter: Enter edit mode", "category": "Jupyter Command Mode", "difficulty": "easy", "mode": "press"},
    {"keys": "A", "action": "Jupyter: Insert a new cell above", "category": "Jupyter Command Mode", "difficulty": "easy", "mode": "press"},
    {"keys": "B", "action": "Jupyter: Insert a new cell below", "category": "Jupyter Command Mode", "difficulty": "easy", "mode": "press"},
    {"keys": "D, D", "action": "Jupyter: Delete the selected cell", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "Z", "action": "Jupyter: Undo cell deletion", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "M", "action": "Jupyter: Change the cell to Markdown", "category": "Jupyter Command Mode", "difficulty": "easy", "mode": "press"},
    {"keys": "Y", "action": "Jupyter: Change the cell to Code", "category": "Jupyter Command Mode", "difficulty": "easy", "mode": "press"},
    {"keys": "R", "action": "Jupyter: Change the cell to Raw", "category": "Jupyter Command Mode", "difficulty": "hard", "mode": "press"},
    {"keys": "C", "action": "Jupyter: Copy the selected cell", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "X", "action": "Jupyter: Cut the selected cell", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "V", "action": "Jupyter: Paste the cell below", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+V", "action": "Jupyter: Paste the cell above", "category": "Jupyter Command Mode", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+M", "action": "Jupyter: Merge the selected cells", "category": "Jupyter Command Mode", "difficulty": "hard", "mode": "press"},
    {"keys": "K", "action": "Jupyter: Select the cell above", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "J", "action": "Jupyter: Select the cell below", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "L", "action": "Jupyter: Show or hide line numbers", "category": "Jupyter Command Mode", "difficulty": "hard", "mode": "press"},
    {"keys": "O", "action": "Jupyter: Show or hide the cell output", "category": "Jupyter Command Mode", "difficulty": "hard", "mode": "press"},
    {"keys": "H", "action": "Jupyter: Show the keyboard shortcuts help", "category": "Jupyter Command Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Jupyter: Open the command palette (Notebook 7)", "category": "Jupyter Command Mode", "difficulty": "hard", "mode": "press"},

    # ---------- Jupyter: edit mode ----------
    {"keys": "Tab", "action": "Jupyter: Code completion or indent", "category": "Jupyter Edit Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Tab", "action": "Jupyter: Show the tooltip / docstring", "category": "Jupyter Edit Mode", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+/", "action": "Jupyter: Comment or uncomment lines", "category": "Jupyter Edit Mode", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+-", "action": "Jupyter: Split the cell at the cursor", "category": "Jupyter Edit Mode", "difficulty": "hard", "mode": "press"},
]
