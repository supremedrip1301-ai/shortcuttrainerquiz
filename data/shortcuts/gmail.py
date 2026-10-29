'''
gmail.py - Gmail web shortcuts (Settings > "Keyboard shortcuts on" must be enabled for most).

Symbols are written with the real keys pressed on a US keyboard:
"#" = Shift+3, "!" = Shift+1, "?" = Shift+/, "*" = Shift+8.
Chords like "G, I" mean: press G, release, then press I.
'''

SHORTCUTS = [
    # ---------- Compose and chat ----------
    {"keys": "C", "action": "Compose a new email", "category": "Compose", "difficulty": "easy", "mode": "press"},
    {"keys": "D", "action": "Compose a new email in a new tab", "category": "Compose", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Enter", "action": "Send the email", "category": "Compose", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Add Cc recipients", "category": "Compose", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+B", "action": "Add Bcc recipients", "category": "Compose", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+K", "action": "Insert a link", "category": "Compose", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Make the text bold", "category": "Compose", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Make the text italic", "category": "Compose", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+U", "action": "Underline the text", "category": "Compose", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+7", "action": "Insert a numbered list", "category": "Compose", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+8", "action": "Insert a bulleted list", "category": "Compose", "difficulty": "hard", "mode": "press"},

    # ---------- Reading and navigation ----------
    {"keys": "/", "action": "Put the cursor in the search box", "category": "Navigation", "difficulty": "easy", "mode": "press"},
    {"keys": "K", "action": "Go to the newer conversation", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "J", "action": "Go to the older conversation", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "N", "action": "Go to the next message in the conversation", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "P", "action": "Go to the previous message in the conversation", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "O", "action": "Open the conversation", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "U", "action": "Go back to the inbox / conversation list", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+/", "action": "Show the keyboard shortcuts help (? key)", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "G, I", "action": "Go to the Inbox", "category": "Navigation", "difficulty": "medium", "mode": "press"},
    {"keys": "G, S", "action": "Go to Starred conversations", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "G, T", "action": "Go to Sent messages", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "G, D", "action": "Go to Drafts", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "G, A", "action": "Go to All Mail", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "G, C", "action": "Go to Contacts", "category": "Navigation", "difficulty": "hard", "mode": "press"},
    {"keys": "G, K", "action": "Go to Tasks", "category": "Navigation", "difficulty": "hard", "mode": "press"},

    # ---------- Actions on conversations ----------
    {"keys": "R", "action": "Reply to the sender", "category": "Actions", "difficulty": "easy", "mode": "press"},
    {"keys": "A", "action": "Reply to all", "category": "Actions", "difficulty": "easy", "mode": "press"},
    {"keys": "F", "action": "Forward the email", "category": "Actions", "difficulty": "easy", "mode": "press"},
    {"keys": "E", "action": "Archive the conversation", "category": "Actions", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+3", "action": "Delete the conversation (# key)", "category": "Actions", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+1", "action": "Report as spam (! key)", "category": "Actions", "difficulty": "hard", "mode": "press"},
    {"keys": "M", "action": "Mute the conversation", "category": "Actions", "difficulty": "hard", "mode": "press"},
    {"keys": "S", "action": "Star or unstar the conversation", "category": "Actions", "difficulty": "medium", "mode": "press"},
    {"keys": "X", "action": "Select the conversation", "category": "Actions", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+I", "action": "Mark as read", "category": "Actions", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+U", "action": "Mark as unread", "category": "Actions", "difficulty": "medium", "mode": "press"},
    {"keys": "=", "action": "Mark as important", "category": "Actions", "difficulty": "hard", "mode": "press"},
    {"keys": "-", "action": "Mark as not important", "category": "Actions", "difficulty": "hard", "mode": "press"},
    {"keys": "L", "action": "Open the Label menu", "category": "Actions", "difficulty": "hard", "mode": "press"},
    {"keys": "V", "action": "Open the Move to menu", "category": "Actions", "difficulty": "hard", "mode": "press"},
    {"keys": "Z", "action": "Undo the last action", "category": "Actions", "difficulty": "medium", "mode": "press"},

    # ---------- Selection (the * key = Shift+8) ----------
    {"keys": "Shift+8, A", "action": "Select all conversations", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+8, N", "action": "Deselect all conversations", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+8, R", "action": "Select all read conversations", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+8, U", "action": "Select all unread conversations", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+8, S", "action": "Select all starred conversations", "category": "Selection", "difficulty": "hard", "mode": "press"},
]
