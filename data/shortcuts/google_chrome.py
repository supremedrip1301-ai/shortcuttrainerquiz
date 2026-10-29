'''
google_chrome.py - Google Chrome shortcuts (Windows). Most of them also work in
other Chromium browsers such as Microsoft Edge and Brave.
'''

SHORTCUTS = [
    # ---------- Tabs and windows ----------
    {"keys": "Ctrl+T", "action": "Open a new tab", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+N", "action": "Open a new window", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+N", "action": "Open a new Incognito window", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+W", "action": "Close the current tab", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+W", "action": "Close the current window", "category": "Tabs & Windows", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+T", "action": "Reopen the last closed tab", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Tab", "action": "Go to the next open tab", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+Tab", "action": "Go to the previous open tab", "category": "Tabs & Windows", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+1", "action": "Jump to the first tab", "category": "Tabs & Windows", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+9", "action": "Jump to the last tab", "category": "Tabs & Windows", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+PageUp", "action": "Move the current tab to the left", "category": "Tabs & Windows", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+PageDown", "action": "Move the current tab to the right", "category": "Tabs & Windows", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+A", "action": "Search your open tabs", "category": "Tabs & Windows", "difficulty": "medium", "mode": "press"},
    {"keys": "F11", "action": "Turn full-screen mode on or off", "category": "Tabs & Windows", "difficulty": "easy", "mode": "press"},

    # ---------- Navigation ----------
    {"keys": "Alt+Left", "action": "Go back to the previous page", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+Right", "action": "Go forward to the next page", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Home", "action": "Open your home page", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "F5", "action": "Reload the current page", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+R", "action": "Reload the page, ignoring cached content", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "Esc", "action": "Stop loading the page", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Space", "action": "Scroll down one screen", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Space", "action": "Scroll up one screen", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Home", "action": "Go to the top of the page", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "End", "action": "Go to the bottom of the page", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "F7", "action": "Turn caret browsing on or off", "category": "Navigation", "difficulty": "hard", "mode": "press"},

    # ---------- Address bar ----------
    {"keys": "Ctrl+L", "action": "Jump to the address bar", "category": "Address Bar", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+K", "action": "Search with your default search engine", "category": "Address Bar", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Enter", "action": "Add www. and .com to the typed name", "category": "Address Bar", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+Enter", "action": "Open the typed address in a new tab", "category": "Address Bar", "difficulty": "hard", "mode": "press"},

    # ---------- Page actions ----------
    {"keys": "Ctrl+F", "action": "Find text on the page", "category": "Page", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+G", "action": "Go to the next find match", "category": "Page", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+G", "action": "Go to the previous find match", "category": "Page", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Print the current page", "category": "Page", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the current page", "category": "Page", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Open a file from your computer", "category": "Page", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+U", "action": "View the page source code", "category": "Page", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+=", "action": "Zoom in (make everything larger)", "category": "Page", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+-", "action": "Zoom out (make everything smaller)", "category": "Page", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+0", "action": "Reset the zoom to default", "category": "Page", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+V", "action": "Paste without formatting", "category": "Page", "difficulty": "medium", "mode": "press"},

    # ---------- Bookmarks and Chrome features ----------
    {"keys": "Ctrl+D", "action": "Bookmark the current page", "category": "Bookmarks & Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+D", "action": "Bookmark all open tabs in a folder", "category": "Bookmarks & Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+B", "action": "Show or hide the bookmarks bar", "category": "Bookmarks & Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+O", "action": "Open the Bookmarks Manager", "category": "Bookmarks & Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+H", "action": "Open the History page", "category": "Bookmarks & Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+J", "action": "Open the Downloads page", "category": "Bookmarks & Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+Esc", "action": "Open the Chrome Task Manager", "category": "Bookmarks & Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+Delete", "action": "Open Clear browsing data", "category": "Bookmarks & Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+F", "action": "Open the Chrome menu", "category": "Bookmarks & Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Shift+T", "action": "Move focus to the toolbar", "category": "Bookmarks & Tools", "difficulty": "hard", "mode": "press"},

    # ---------- Developer tools ----------
    {"keys": "Ctrl+Shift+I", "action": "Open Developer Tools", "category": "Developer", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+J", "action": "Open the DevTools Console", "category": "Developer", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Inspect an element on the page", "category": "Developer", "difficulty": "hard", "mode": "press"},
]
