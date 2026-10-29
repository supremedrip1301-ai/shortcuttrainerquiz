'''
adobe_after_effects.py - Adobe After Effects (current Creative Cloud version, Windows, default shortcuts).
Letters like P, S, R, T show one property of the selected layer in the timeline.
'''

SHORTCUTS = [
    # ---------- Tools ----------
    {"keys": "V", "action": "Select the Selection tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "H", "action": "Select the Hand tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "Z", "action": "Select the Zoom tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "W", "action": "Select the Rotation tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "C", "action": "Cycle through the Camera tools", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "Y", "action": "Select the Pan Behind (Anchor Point) tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Q", "action": "Cycle through the Shape tools", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "G", "action": "Select the Pen tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+T", "action": "Select the Type tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+B", "action": "Cycle through Brush, Clone Stamp and Eraser", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "Alt+W", "action": "Select the Roto Brush tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+P", "action": "Select the Puppet tools", "category": "Tools", "difficulty": "hard", "mode": "press"},

    # ---------- Layer properties ----------
    {"keys": "P", "action": "Show the Position property", "category": "Layer Properties", "difficulty": "easy", "mode": "press"},
    {"keys": "S", "action": "Show the Scale property", "category": "Layer Properties", "difficulty": "easy", "mode": "press"},
    {"keys": "R", "action": "Show the Rotation property", "category": "Layer Properties", "difficulty": "easy", "mode": "press"},
    {"keys": "T", "action": "Show the Opacity property", "category": "Layer Properties", "difficulty": "easy", "mode": "press"},
    {"keys": "A", "action": "Show the Anchor Point property", "category": "Layer Properties", "difficulty": "medium", "mode": "press"},
    {"keys": "U", "action": "Show all animated (keyframed) properties", "category": "Layer Properties", "difficulty": "medium", "mode": "press"},
    {"keys": "U, U", "action": "Show all modified properties", "category": "Layer Properties", "difficulty": "hard", "mode": "press"},
    {"keys": "E", "action": "Show the applied effects", "category": "Layer Properties", "difficulty": "medium", "mode": "press"},
    {"keys": "M", "action": "Show the Mask Path property", "category": "Layer Properties", "difficulty": "hard", "mode": "press"},
    {"keys": "F", "action": "Show the Mask Feather property", "category": "Layer Properties", "difficulty": "hard", "mode": "press"},
    {"keys": "L", "action": "Show the Audio Levels property", "category": "Layer Properties", "difficulty": "hard", "mode": "press"},

    # ---------- Layers ----------
    {"keys": "Ctrl+Y", "action": "Create a new Solid layer", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+Y", "action": "Create a new Adjustment layer", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+Shift+Y", "action": "Create a new Null Object", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+Shift+L", "action": "Create a new Light", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+Shift+C", "action": "Create a new Camera", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+C", "action": "Pre-compose the selected layers", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+D", "action": "Duplicate the layer", "category": "Layers", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+D", "action": "Split the layer at the current time", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+[", "action": "Trim the layer In point to the current time", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+]", "action": "Trim the layer Out point to the current time", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "[", "action": "Move the layer In point to the current time", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "]", "action": "Move the layer Out point to the current time", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+R", "action": "Time-reverse the layer", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+T", "action": "Enable Time Remapping", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+Home", "action": "Center the anchor point in the layer", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Home", "action": "Center the layer in the composition", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+F", "action": "Fit the layer to the composition", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+L", "action": "Lock the selected layers", "category": "Layers", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+N", "action": "Create a new mask", "category": "Layers", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+E", "action": "Remove all effects from the layer", "category": "Layers", "difficulty": "hard", "mode": "press"},

    # ---------- Keyframes ----------
    {"keys": "F9", "action": "Apply Easy Ease to keyframes", "category": "Keyframes", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+F9", "action": "Apply Easy Ease In", "category": "Keyframes", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+F9", "action": "Apply Easy Ease Out", "category": "Keyframes", "difficulty": "hard", "mode": "press"},
    {"keys": "J", "action": "Go to the previous keyframe", "category": "Keyframes", "difficulty": "medium", "mode": "press"},
    {"keys": "K", "action": "Go to the next keyframe", "category": "Keyframes", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Shift+P", "action": "Add a Position keyframe", "category": "Keyframes", "difficulty": "hard", "mode": "press"},

    # ---------- Time and preview ----------
    {"keys": "Space", "action": "Play or stop the preview", "category": "Time & Preview", "difficulty": "easy", "mode": "press"},
    {"keys": "Numpad 0", "action": "Preview from the current time", "category": "Time & Preview", "difficulty": "medium", "mode": "mcq"},
    {"keys": "Home", "action": "Go to the beginning of the composition", "category": "Time & Preview", "difficulty": "easy", "mode": "press"},
    {"keys": "End", "action": "Go to the end of the composition", "category": "Time & Preview", "difficulty": "easy", "mode": "press"},
    {"keys": "PageDown", "action": "Go forward one frame", "category": "Time & Preview", "difficulty": "medium", "mode": "press"},
    {"keys": "PageUp", "action": "Go back one frame", "category": "Time & Preview", "difficulty": "medium", "mode": "press"},
    {"keys": "B", "action": "Set the start of the work area", "category": "Time & Preview", "difficulty": "medium", "mode": "press"},
    {"keys": "N", "action": "Set the end of the work area", "category": "Time & Preview", "difficulty": "medium", "mode": "press"},
    {"keys": "I", "action": "Go to the layer In point", "category": "Time & Preview", "difficulty": "medium", "mode": "press"},
    {"keys": "O", "action": "Go to the layer Out point", "category": "Time & Preview", "difficulty": "medium", "mode": "press"},
    {"keys": "Alt+Shift+J", "action": "Go to a specific time", "category": "Time & Preview", "difficulty": "hard", "mode": "press"},

    # ---------- Project and render ----------
    {"keys": "Ctrl+Alt+N", "action": "Create a new project", "category": "Project & Render", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+N", "action": "Create a new composition", "category": "Project & Render", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+K", "action": "Open Composition Settings", "category": "Project & Render", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Import a file", "category": "Project & Render", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the project", "category": "Project & Render", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "Save the project as a new file", "category": "Project & Render", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+/", "action": "Add the selected items to the composition", "category": "Project & Render", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+M", "action": "Add the composition to the Render Queue", "category": "Project & Render", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Alt+M", "action": "Add the composition to Media Encoder", "category": "Project & Render", "difficulty": "hard", "mode": "press"},

    # ---------- View ----------
    {"keys": "F3", "action": "Show or hide the Effect Controls panel", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "`", "action": "Maximize the panel under the mouse", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Show or hide rulers", "category": "View", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+'", "action": "Show or hide the grid", "category": "View", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+;", "action": "Show or hide guides", "category": "View", "difficulty": "hard", "mode": "press"},
]
