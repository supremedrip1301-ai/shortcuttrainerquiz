'''
youtube.py - YouTube video player shortcuts (web browser on Windows).
"<" and ">" are written with the real keys: Shift+, and Shift+.
'''

SHORTCUTS = [
    # ---------- Playback ----------
    {"keys": "K", "action": "Play or pause the video", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "J", "action": "Rewind 10 seconds", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "L", "action": "Fast forward 10 seconds", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Left", "action": "Rewind 5 seconds", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "Right", "action": "Fast forward 5 seconds", "category": "Playback", "difficulty": "easy", "mode": "press"},
    {"keys": "0", "action": "Jump to the start of the video", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "End", "action": "Jump to the end of the video", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "1", "action": "Jump to 10% of the video", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": "5", "action": "Jump to the middle (50%) of the video", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "9", "action": "Jump to 90% of the video", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": ",", "action": "Go back one frame (while paused)", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": ".", "action": "Go forward one frame (while paused)", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+.", "action": "Increase the playback speed (> key)", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+,", "action": "Decrease the playback speed (< key)", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Ctrl+Left", "action": "Go to the previous chapter", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": "Ctrl+Right", "action": "Go to the next chapter", "category": "Playback", "difficulty": "hard", "mode": "press"},
    {"keys": "Shift+N", "action": "Play the next video", "category": "Playback", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+P", "action": "Play the previous video (in a playlist)", "category": "Playback", "difficulty": "hard", "mode": "press"},

    # ---------- Sound and view ----------
    {"keys": "M", "action": "Mute or unmute the video", "category": "Sound & View", "difficulty": "easy", "mode": "press"},
    {"keys": "Up", "action": "Increase the volume by 5%", "category": "Sound & View", "difficulty": "easy", "mode": "press"},
    {"keys": "Down", "action": "Decrease the volume by 5%", "category": "Sound & View", "difficulty": "easy", "mode": "press"},
    {"keys": "F", "action": "Turn full screen on or off", "category": "Sound & View", "difficulty": "easy", "mode": "press"},
    {"keys": "T", "action": "Turn theater mode on or off", "category": "Sound & View", "difficulty": "medium", "mode": "press"},
    {"keys": "I", "action": "Open the miniplayer", "category": "Sound & View", "difficulty": "medium", "mode": "press"},
    {"keys": "C", "action": "Turn captions (subtitles) on or off", "category": "Sound & View", "difficulty": "easy", "mode": "press"},

    # ---------- Site ----------
    {"keys": "/", "action": "Go to the search box", "category": "Site", "difficulty": "medium", "mode": "press"},
    {"keys": "Shift+/", "action": "Show all keyboard shortcuts (? key)", "category": "Site", "difficulty": "medium", "mode": "press"},
]
