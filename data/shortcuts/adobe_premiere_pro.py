'''
adobe_premiere_pro.py - Adobe Premiere Pro (current Creative Cloud version, Windows, default shortcuts).
'''

SHORTCUTS = [
    # ---------- Tools ----------
    {"keys": "V", "action": "Select the Selection tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "C", "action": "Select the Razor tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "A", "action": "Select the Track Select Forward tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+A", "action": "Select the Track Select Backward tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "B", "action": "Select the Ripple Edit tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "N", "action": "Select the Rolling Edit tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "R", "action": "Select the Rate Stretch tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "Y", "action": "Select the Slip tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "U", "action": "Select the Slide tool", "category": "Tools", "difficulty": "hard", "mode": "press"},
    {"keys": "P", "action": "Select the Pen tool", "category": "Tools", "difficulty": "medium", "mode": "press"},
    {"keys": "H", "action": "Select the Hand tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "Z", "action": "Select the Zoom tool", "category": "Tools", "difficulty": "easy", "mode": "press"},
    {"keys": "T", "action": "Select the Type tool", "category": "Tools", "difficulty": "easy", "mode": "press"},

    # ---------- Playback ----------
    {"keys": "Space", "action": "Play or stop", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "J", "action": "Shuttle (play) backward", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "K", "action": "Stop the shuttle", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "L", "action": "Shuttle (play) forward", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Left", "action": "Step back one frame", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Right", "action": "Step forward one frame", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Up", "action": "Go to the previous edit point", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Down", "action": "Go to the next edit point", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Home", "action": "Go to the start of the sequence", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "End", "action": "Go to the end of the sequence", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Enter", "action": "Render effects in the work area", "category": "Playback", "difficulty": "medium", "mode": "press"},

    # ---------- Marking ----------
    {"keys": "I", "action": "Mark the In point", "category": "Marking", "difficulty": "easy", "mode": "press"},
    {"keys": "O", "action": "Mark the Out point", "category": "Marking", "difficulty": "easy", "mode": "press"},
    {"keys": "X", "action": "Mark the clip under the playhead", "category": "Marking", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+I", "action": "Clear the In point", "category": "Marking", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+O", "action": "Clear the Out point", "category": "Marking", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Shift+X", "action": "Clear both In and Out points", "category": "Marking", "difficulty": "medium", "mode": "press"},
    {"keys": "M", "action": "Add a marker", "category": "Marking", "difficulty": "easy", "mode": "press"},
    {"keys": "Shift+M", "action": "Go to the next marker", "category": "Marking", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+M", "action": "Go to the previous marker", "category": "Marking", "difficulty": "hard", "mode": "press"},

    # ---------- Editing ----------
    {"keys": "Ctrl+K", "action": "Add an edit (cut) at the playhead", "category": "Editing", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+K", "action": "Add an edit to all tracks", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Q", "action": "Ripple trim the previous edit to the playhead", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "W", "action": "Ripple trim the next edit to the playhead", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+Delete", "action": "Ripple delete (close the gap)", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": ",", "action": "Insert the source clip", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": ".", "action": "Overwrite with the source clip", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": ";", "action": "Lift the marked section", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "'", "action": "Extract the marked section", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+L", "action": "Link or unlink audio and video", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+G", "action": "Group the selected clips", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+G", "action": "Ungroup clips", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+R", "action": "Open Speed / Duration", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+E", "action": "Enable or disable the clip", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Alt+V", "action": "Paste attributes", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+D", "action": "Apply the default video transition", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Shift+D", "action": "Apply the default audio transition", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+D", "action": "Apply default transitions to the selection", "category": "Editing", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+G", "action": "Open Audio Gain", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "S", "action": "Turn timeline snapping on or off", "category": "Editing", "difficulty": "medium", "mode": "press"},
    {"keys": "F", "action": "Match frame (open the source frame)", "category": "Editing", "difficulty": "hard", "mode": "press"},

    # ---------- Timeline view and panels ----------
    {"keys": "=", "action": "Zoom in on the timeline", "category": "View & Panels", "difficulty": "easy", "mode": "press"},
    {"keys": "-", "action": "Zoom out on the timeline", "category": "View & Panels", "difficulty": "easy", "mode": "press"},
    {"keys": "\\", "action": "Zoom to fit the whole sequence", "category": "View & Panels", "difficulty": "medium", "mode": "press"},
    {"keys": "`", "action": "Maximize the panel under the mouse", "category": "View & Panels", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+1", "action": "Open the Project panel", "category": "View & Panels", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+2", "action": "Open the Source Monitor", "category": "View & Panels", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+3", "action": "Open the Timeline panel", "category": "View & Panels", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+4", "action": "Open the Program Monitor", "category": "View & Panels", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+5", "action": "Open the Effect Controls panel", "category": "View & Panels", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+7", "action": "Open the Effects panel", "category": "View & Panels", "difficulty": "hard", "mode": "press"},

    # ---------- File ----------
    {"keys": "Ctrl+Alt+N", "action": "Create a new project", "category": "File", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+N", "action": "Create a new sequence", "category": "File", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+O", "action": "Open a project", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+S", "action": "Save the project", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Shift+S", "action": "Save the project as a new file", "category": "File", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+I", "action": "Import media files", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+M", "action": "Export media", "category": "File", "difficulty": "easy", "mode": "press"},
    {"keys": "Ctrl+Q", "action": "Quit Premiere Pro", "category": "File", "difficulty": "medium", "mode": "press"},
]
