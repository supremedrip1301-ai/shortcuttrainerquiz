'''
blender.py - Blender 4.x shortcuts (default keymap, 3D Viewport and modelling).

Numpad shortcuts use names like "Numpad 1". They are "mcq" only, because many laptops
have no number pad (and with Num Lock off the numpad sends other keys).
Some keys mean different things in Object mode and Edit mode; the action says which.
'''

SHORTCUTS = [
    # ---------- Transform ----------
    {"keys": "G", "action": "Grab / move the selection", "category": "Transform", "difficulty": "easy", "mode": "press"},
    {"keys": "R", "action": "Rotate the selection", "category": "Transform", "difficulty": "easy", "mode": "press"},
    {"keys": "S", "action": "Scale the selection", "category": "Transform", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+G", "action": "Clear the location (object mode)", "category": "Transform", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+R", "action": "Clear the rotation (object mode)", "category": "Transform", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+S", "action": "Clear the scale (object mode)", "category": "Transform", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+A", "action": "Open the Apply menu (apply scale, rotation...)", "category": "Transform", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+S", "action": "Open the Snap menu", "category": "Transform", "difficulty": "medium", "mode": "press"},
    {"keys": ".", "action": "Open the Pivot Point pie menu", "category": "Transform", "difficulty": "hard", "mode": "press"},
    {"keys": ",", "action": "Open the Transform Orientation pie menu", "category": "Transform", "difficulty": "hard", "mode": "press"},

    # ---------- Objects ----------
    {"keys": "Tab", "action": "Switch between Object and Edit mode", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Tab", "action": "Open the mode pie menu", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+A", "action": "Open the Add menu (add mesh, light...)", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+D", "action": "Duplicate the selection", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+D", "action": "Make a linked duplicate", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "X", "action": "Delete the selection (with a menu)", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Delete", "action": "Delete the selection without asking", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+J", "action": "Join the selected objects", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Set the parent object", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+P", "action": "Clear the parent", "category": "Objects", "difficulty": "hard", "mode": "press"},
    {"keys": "H", "action": "Hide the selection", "category": "Objects", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+H", "action": "Show (unhide) everything", "category": "Objects", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+H", "action": "Hide everything that is not selected", "category": "Objects", "difficulty": "hard", "mode": "press"},

    # ---------- Selection ----------
    {"keys": "A", "action": "Select all", "category": "Selection", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+A", "action": "Deselect all", "category": "Selection", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Invert the selection", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "B", "action": "Box select", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "C", "action": "Circle select", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "L", "action": "Select linked geometry under the mouse", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+L", "action": "Select all linked geometry", "category": "Selection", "difficulty": "hard", "mode": "press"},
    {"keys": "1", "action": "Vertex select mode (edit mode)", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "2", "action": "Edge select mode (edit mode)", "category": "Selection", "difficulty": "medium", "mode": "press"},
    {"keys": "3", "action": "Face select mode (edit mode)", "category": "Selection", "difficulty": "medium", "mode": "press"},

    # ---------- Modeling (edit mode) ----------
    {"keys": "E", "action": "Extrude the selection", "category": "Modeling", "difficulty": "easy", "mode": "press"},
    {"keys": "Alt+E", "action": "Open the Extrude menu", "category": "Modeling", "difficulty": "hard", "mode": "press"},
    {"keys": "I", "action": "Inset the selected faces", "category": "Modeling", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Add a loop cut", "category": "Modeling", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Bevel the selected edges", "category": "Modeling", "difficulty": "medium", "mode": "press"},
    {"keys": "K", "action": "Use the Knife tool", "category": "Modeling", "difficulty": "medium", "mode": "press"},
    {"keys": "M", "action": "Merge vertices (edit mode)", "category": "Modeling", "difficulty": "medium", "mode": "press"},
    {"keys": "F", "action": "Fill / make a face or edge", "category": "Modeling", "difficulty": "medium", "mode": "press"},
    {"keys": "V", "action": "Rip the vertices apart", "category": "Modeling", "difficulty": "hard", "mode": "press"},
    {"keys": "P", "action": "Separate the selection into a new object", "category": "Modeling", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+N", "action": "Recalculate the normals outside", "category": "Modeling", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+V", "action": "Open the Vertex menu", "category": "Modeling", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+E", "action": "Open the Edge menu", "category": "Modeling", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+F", "action": "Open the Face menu", "category": "Modeling", "difficulty": "hard", "mode": "press"},

    # ---------- Viewport and navigation ----------
    {"keys": "Numpad 1", "action": "Front view", "category": "Viewport", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Ctrl+Numpad 1", "action": "Back view", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Numpad 3", "action": "Right view", "category": "Viewport", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Ctrl+Numpad 3", "action": "Left view", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Numpad 7", "action": "Top view", "category": "Viewport", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Ctrl+Numpad 7", "action": "Bottom view", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Numpad 5", "action": "Switch perspective / orthographic view", "category": "Viewport", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Numpad 0", "action": "Look through the active camera", "category": "Viewport", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Ctrl+Alt+Numpad 0", "action": "Align the active camera to the view", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Numpad 4", "action": "Orbit the view to the left", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Numpad 6", "action": "Orbit the view to the right", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Numpad .", "action": "Frame (zoom to) the selected object", "category": "Viewport", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Numpad /", "action": "Toggle local view (isolate selection)", "category": "Viewport", "difficulty": "hard", "mode": "mcq"},
    {"keys": "Home", "action": "Frame all objects in the view", "category": "Viewport", "difficulty": "medium", "mode": "press"},
    {"keys": "`", "action": "Open the View pie menu", "category": "Viewport", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+C", "action": "Reset the 3D cursor and view all", "category": "Viewport", "difficulty": "hard", "mode": "press"},
    {"keys": "Z", "action": "Open the Shading pie menu", "category": "Viewport", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Z", "action": "Toggle X-Ray", "category": "Viewport", "difficulty": "medium", "mode": "press"},
    {"keys": "N", "action": "Show or hide the Sidebar", "category": "Viewport", "difficulty": "easy", "mode": "press"},
    {"keys": "T", "action": "Show or hide the Toolbar", "category": "Viewport", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Space", "action": "Maximize the area under the mouse", "category": "Viewport", "difficulty": "medium", "mode": "press"},

    # ---------- General, render and animation ----------
    {"keys": "F3", "action": "Search for any menu operation", "category": "General", "difficulty": "medium", "mode": "press"},
    {"keys": "F9", "action": "Adjust the last operation", "category": "General", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+R", "action": "Repeat the last action", "category": "General", "difficulty": "hard", "mode": "press"},
    {"keys": "F4", "action": "Open the File context menu", "category": "General", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+N", "action": "Create a new file", "category": "General", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Open a .blend file", "category": "General", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the file", "category": "General", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "Save the file as a new name", "category": "General", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Z", "action": "Undo", "category": "General", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+Z", "action": "Redo", "category": "General", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Q", "action": "Quit Blender", "category": "General", "difficulty": "medium", "mode": "press"},
    {"keys": "F12", "action": "Render the current frame", "category": "Render & Animation", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+F12", "action": "Render the animation", "category": "Render & Animation", "difficulty": "medium", "mode": "press"},
    {"keys": "F11", "action": "Show the render window", "category": "Render & Animation", "difficulty": "hard", "mode": "press"},
    {"keys": "Space", "action": "Play or pause the animation", "category": "Render & Animation", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+Left", "action": "Jump to the start frame", "category": "Render & Animation", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Right", "action": "Jump to the end frame", "category": "Render & Animation", "difficulty": "medium", "mode": "press"},
]
