'''
adobe_lightroom.py - Adobe Lightroom Classic (current version, Windows, default shortcuts).
'''

SHORTCUTS = [
    # ---------- Modules and views ----------
    {"keys": "G", "action": "Go to the Library Grid view", "category": "Modules & Views", "difficulty": "easy", "mode": "press"},
    {"keys": "E", "action": "Go to the Library Loupe view", "category": "Modules & Views", "difficulty": "easy", "mode": "press"},
    {"keys": "C", "action": "Go to the Compare view", "category": "Modules & Views", "difficulty": "medium", "mode": "press"},
    {"keys": "N", "action": "Go to the Survey view", "category": "Modules & Views", "difficulty": "medium", "mode": "press"},
    {"keys": "D", "action": "Go to the Develop module", "category": "Modules & Views", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Alt+1", "action": "Switch to the Library module", "category": "Modules & Views", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+2", "action": "Switch to the Develop module", "category": "Modules & Views", "difficulty": "hard", "mode": "press"},
    {"keys": "F", "action": "Show a full-screen preview", "category": "Modules & Views", "difficulty": "medium", "mode": "press"},
    {"keys": "L", "action": "Cycle the Lights Out modes", "category": "Modules & Views", "difficulty": "medium", "mode": "press"},
    {"keys": "Tab", "action": "Show or hide the side panels", "category": "Modules & Views", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Tab", "action": "Show or hide all panels", "category": "Modules & Views", "difficulty": "medium", "mode": "press"},
    {"keys": "Z", "action": "Switch between zoomed and fit view", "category": "Modules & Views", "difficulty": "easy", "mode": "press"},
    {"keys": "I", "action": "Cycle the info overlay", "category": "Modules & Views", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+/", "action": "Show the shortcuts of the current module", "category": "Modules & Views", "difficulty": "hard", "mode": "press"},

    # ---------- Rating and flags ----------
    {"keys": "P", "action": "Flag the photo as a Pick", "category": "Rating & Flags", "difficulty": "easy", "mode": "press"},
    {"keys": "X", "action": "Flag the photo as Rejected", "category": "Rating & Flags", "difficulty": "easy", "mode": "press"},
    {"keys": "U", "action": "Remove the flag (unflag)", "category": "Rating & Flags", "difficulty": "medium", "mode": "press"},
    {"keys": "1", "action": "Set a 1-star rating", "category": "Rating & Flags", "difficulty": "easy", "mode": "press"},
    {"keys": "5", "action": "Set a 5-star rating", "category": "Rating & Flags", "difficulty": "easy", "mode": "press"},
    {"keys": "0", "action": "Remove the star rating", "category": "Rating & Flags", "difficulty": "medium", "mode": "press"},
    {"keys": "]", "action": "Increase the star rating", "category": "Rating & Flags", "difficulty": "hard", "mode": "press"},
    {"keys": "[", "action": "Decrease the star rating", "category": "Rating & Flags", "difficulty": "hard", "mode": "press"},
    {"keys": "6", "action": "Set the red color label", "category": "Rating & Flags", "difficulty": "medium", "mode": "press"},
    {"keys": "7", "action": "Set the yellow color label", "category": "Rating & Flags", "difficulty": "medium", "mode": "press"},
    {"keys": "8", "action": "Set the green color label", "category": "Rating & Flags", "difficulty": "medium", "mode": "press"},
    {"keys": "9", "action": "Set the blue color label", "category": "Rating & Flags", "difficulty": "medium", "mode": "press"},

    # ---------- Develop ----------
    {"keys": "R", "action": "Open the Crop tool", "category": "Develop", "difficulty": "easy", "mode": "press"},
    {"keys": "Q", "action": "Open the Spot Removal (Heal) tool", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "W", "action": "Pick the White Balance selector", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "V", "action": "Convert to black and white", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "J", "action": "Show the clipping warnings", "category": "Develop", "difficulty": "hard", "mode": "press"},
    {"keys": "\\", "action": "Show the Before view", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "Y", "action": "Show Before / After side by side", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+R", "action": "Reset all develop settings", "category": "Develop", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Copy the develop settings", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+V", "action": "Paste the develop settings", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "Sync the settings to selected photos", "category": "Develop", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+'", "action": "Create a virtual copy", "category": "Develop", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+[", "action": "Rotate the photo left (counter-clockwise)", "category": "Develop", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+]", "action": "Rotate the photo right (clockwise)", "category": "Develop", "difficulty": "medium", "mode": "press"},

    # ---------- Library and files ----------
    {"keys": "Ctrl+Shift+I", "action": "Import photos", "category": "Library & Files", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+E", "action": "Export photos", "category": "Library & Files", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Alt+Shift+E", "action": "Export with the previous settings", "category": "Library & Files", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+N", "action": "Create a new collection", "category": "Library & Files", "difficulty": "medium", "mode": "press"},
    {"keys": "B", "action": "Add the photo to the Quick Collection", "category": "Library & Files", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Show the Quick Collection", "category": "Library & Files", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F", "action": "Find photos (text filter)", "category": "Library & Files", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+K", "action": "Edit keywords", "category": "Library & Files", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+G", "action": "Group the photos into a stack", "category": "Library & Files", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Edit the photo in Photoshop", "category": "Library & Files", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Show the file in Explorer", "category": "Library & Files", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+,", "action": "Open Preferences", "category": "Library & Files", "difficulty": "hard", "mode": "press"},
]
