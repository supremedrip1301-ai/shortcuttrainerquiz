'''
windows_file_explorer.py - File Explorer shortcuts (Windows 11).
'''

SHORTCUTS = [
    # ---------- Windows and tabs ----------
    {"keys": "Ctrl+N", "action": "Open a new File Explorer window", "category": "Window", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+T", "action": "Open a new tab", "category": "Window", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+W", "action": "Close the current tab or window", "category": "Window", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Tab", "action": "Switch to the next tab", "category": "Window", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+Tab", "action": "Switch to the previous tab", "category": "Window", "difficulty": "medium", "mode": "press"},
    {"keys": "F11", "action": "Make the Explorer window full screen", "category": "Window", "difficulty": "medium", "mode": "press"},
    {"keys": "F6", "action": "Cycle through the parts of the window", "category": "Window", "difficulty": "medium", "mode": "press"},

    # ---------- Navigation ----------
    {"keys": "Alt+Left", "action": "Go back to the previous folder", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+Right", "action": "Go forward to the next folder", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Up", "action": "Go up to the parent folder", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Backspace", "action": "View the previous folder", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+L", "action": "Select the address bar", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "F4", "action": "Open the address bar drop-down list", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Select the search box", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Home", "action": "Jump to the top of the file list", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "End", "action": "Jump to the bottom of the file list", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+E", "action": "Show all folders above the selected folder", "category": "Navigation", "difficulty": "hard", "mode": "press"},

    # ---------- Files and folders ----------
    {"keys": "Ctrl+Shift+N", "action": "Create a new folder", "category": "Files", "difficulty": "easy", "mode": "press"},
    {"keys": "F2", "action": "Rename the selected item", "category": "Files", "difficulty": "easy", "mode": "press"},
    {"keys": "Delete", "action": "Move the selected item to the Recycle Bin", "category": "Files", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+Delete", "action": "Delete permanently (skip the Recycle Bin)", "category": "Files", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Enter", "action": "Open Properties of the selected item", "category": "Files", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Copy the full path of the selected item", "category": "Files", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+A", "action": "Select all files and folders", "category": "Files", "difficulty": "easy", "mode": "press"},
    {"keys": "F5", "action": "Refresh the folder contents", "category": "Files", "difficulty": "easy", "mode": "press"},

    # ---------- Panes and views ----------
    {"keys": "Alt+P", "action": "Show or hide the preview pane", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Shift+P", "action": "Show or hide the details pane", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+1", "action": "Change the view to Extra large icons", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+2", "action": "Change the view to Large icons", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+3", "action": "Change the view to Medium icons", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+4", "action": "Change the view to Small icons", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+5", "action": "Change the view to List", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+6", "action": "Change the view to Details", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+7", "action": "Change the view to Tiles", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+8", "action": "Change the view to Content", "category": "View", "difficulty": "hard", "mode": "press"},
]
