'''
figma.py - Figma shortcuts (desktop app or browser on Windows, default shortcuts).
'''

SHORTCUTS = [
    # ---------- Tools ----------
    {"keys": "V", "action": "Select the Move tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "K", "action": "Select the Scale tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "F", "action": "Select the Frame tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "R", "action": "Select the Rectangle tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "O", "action": "Select the Ellipse tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "L", "action": "Select the Line tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+L", "action": "Select the Arrow tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "P", "action": "Select the Pen tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+P", "action": "Select the Pencil tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "T", "action": "Select the Text tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "C", "action": "Add a comment", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "I", "action": "Pick a color (eyedropper)", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+S", "action": "Select the Section tool", "category": "Tools", "difficulty": "hard", "mode": "press"},

    # ---------- Edit ----------
    {"keys": "Ctrl+D", "action": "Duplicate the selection", "category": "Edit", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Rename the selected layer", "category": "Edit", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+V", "action": "Paste over the selection", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+C", "action": "Copy the properties", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+V", "action": "Paste the properties", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Copy the selection as a PNG image", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+A", "action": "Select all layers", "category": "Edit", "difficulty": "easy", "mode": "press"},
    {"keys": "Enter", "action": "Select the children of the selection", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+Enter", "action": "Select the parent of the selection", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Tab", "action": "Select the next sibling layer", "category": "Edit", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+Tab", "action": "Select the previous sibling layer", "category": "Edit", "difficulty": "hard", "mode": "press"},

    # ---------- Objects and components ----------
    {"keys": "Ctrl+G", "action": "Group the selection", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+G", "action": "Ungroup the selection", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Alt+G", "action": "Wrap the selection in a frame", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+A", "action": "Add auto layout", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+K", "action": "Create a component", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+B", "action": "Detach the instance", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+M", "action": "Use the selection as a mask", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Flatten the selection", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+H", "action": "Show or hide the selection", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+L", "action": "Lock or unlock the selection", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+]", "action": "Bring the layer forward", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+[", "action": "Send the layer backward", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+H", "action": "Flip horizontally", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+V", "action": "Flip vertically", "category": "Objects", "difficulty": "medium", "mode": "press"},

    # ---------- Alignment ----------
    {"keys": "Alt+A", "action": "Align left", "category": "Alignment", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+D", "action": "Align right", "category": "Alignment", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+W", "action": "Align top", "category": "Alignment", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+S", "action": "Align bottom", "category": "Alignment", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+H", "action": "Align horizontal centers", "category": "Alignment", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+V", "action": "Align vertical centers", "category": "Alignment", "difficulty": "hard", "mode": "press"},

    # ---------- Text ----------
    {"keys": "Ctrl+B", "action": "Make text bold", "category": "Text", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Make text italic", "category": "Text", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+U", "action": "Underline text", "category": "Text", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+X", "action": "Strikethrough text", "category": "Text", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+L", "action": "Align text left", "category": "Text", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+T", "action": "Align text center", "category": "Text", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+R", "action": "Align text right", "category": "Text", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+J", "action": "Justify text", "category": "Text", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+7", "action": "Make a numbered list", "category": "Text", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+8", "action": "Make a bulleted list", "category": "Text", "difficulty": "hard", "mode": "press"},

    # ---------- View ----------
    {"keys": "Shift+0", "action": "Zoom to 100%", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+1", "action": "Zoom to fit everything", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+2", "action": "Zoom to the selection", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+\\", "action": "Show or hide the user interface", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+R", "action": "Show or hide rulers", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+'", "action": "Show or hide the pixel grid", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+4", "action": "Show or hide layout grids", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Y", "action": "Turn outline mode on or off", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+1", "action": "Open the Layers panel", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+2", "action": "Open the Assets panel", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+/", "action": "Open Quick Actions (search commands)", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+/", "action": "Show the keyboard shortcuts panel", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+Enter", "action": "Present / play the prototype", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+E", "action": "Export the selection", "category": "View", "difficulty": "medium", "mode": "press"},
]
