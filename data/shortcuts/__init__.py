'''
data/shortcuts/__init__.py - collects the shortcut lists of every software.

Every software has its own file in this folder (for example vs_code.py) with a list
called SHORTCUTS. This file loads all of them into ONE dictionary:

    ALL_SOFTWARE = {software_key: list_of_shortcut_dictionaries}

To add a new software: create a new file here with a SHORTCUTS list and add one
line for it in SOFTWARE_INFO below. Nothing else has to change.
'''

import importlib

from core.models import make_shortcut

# Sections of the home screen, in display order (tuple = fixed).
SECTIONS = ("Operating System", "Office & Productivity", "Browsers & Web", "Programming",
            "Design & Photo", "Video & Motion", "3D & CAD", "Communication")

# software_key (= file name) -> display name, badge initials, badge colour, home-screen section
SOFTWARE_INFO = {
    "windows_general": {"name": "Windows 11", "initials": "Win", "color": "#0078d4", "section": "Operating System"},
    "windows_file_explorer": {"name": "File Explorer", "initials": "FE", "color": "#e0a800", "section": "Operating System"},
    "notepad_paint": {"name": "Notepad & Paint", "initials": "NP", "color": "#5b8def", "section": "Operating System"},
    "ms_word": {"name": "Microsoft Word", "initials": "W", "color": "#2b579a", "section": "Office & Productivity"},
    "ms_excel": {"name": "Microsoft Excel", "initials": "X", "color": "#217346", "section": "Office & Productivity"},
    "ms_powerpoint": {"name": "PowerPoint", "initials": "P", "color": "#c43e1c", "section": "Office & Productivity"},
    "google_chrome": {"name": "Google Chrome", "initials": "Ch", "color": "#1a73e8", "section": "Browsers & Web"},
    "gmail": {"name": "Gmail", "initials": "M", "color": "#d93025", "section": "Browsers & Web"},
    "youtube": {"name": "YouTube", "initials": "YT", "color": "#cc0000", "section": "Browsers & Web"},
    "vs_code": {"name": "VS Code", "initials": "VS", "color": "#007acc", "section": "Programming"},
    "python_idle_jupyter": {"name": "Python IDLE & Jupyter", "initials": "Py", "color": "#3776ab", "section": "Programming"},
    "adobe_photoshop": {"name": "Photoshop", "initials": "Ps", "color": "#1c3d5a", "section": "Design & Photo"},
    "adobe_illustrator": {"name": "Illustrator", "initials": "Ai", "color": "#8a4b00", "section": "Design & Photo"},
    "adobe_lightroom": {"name": "Lightroom Classic", "initials": "Lr", "color": "#2d4f6c", "section": "Design & Photo"},
    "figma": {"name": "Figma", "initials": "Fg", "color": "#a259ff", "section": "Design & Photo"},
    "adobe_premiere_pro": {"name": "Premiere Pro", "initials": "Pr", "color": "#5b3f99", "section": "Video & Motion"},
    "adobe_after_effects": {"name": "After Effects", "initials": "Ae", "color": "#4b3b8f", "section": "Video & Motion"},
    "davinci_resolve": {"name": "DaVinci Resolve", "initials": "DR", "color": "#c0392b", "section": "Video & Motion"},
    "blender": {"name": "Blender", "initials": "Bl", "color": "#e87d0d", "section": "3D & CAD"},
    "autocad": {"name": "AutoCAD", "initials": "AC", "color": "#b5121b", "section": "3D & CAD"},
    "microsoft_teams": {"name": "Microsoft Teams", "initials": "T", "color": "#5059c9", "section": "Communication"},
}


def load_all_software():
    '''Import every software file listed in SOFTWARE_INFO and return ALL_SOFTWARE.'''
    all_software = {}
    for software_key in SOFTWARE_INFO:
        try:
            # NOTE (advanced): importlib loads a module from its name stored in a string,
            # so a new software only needs a new file + one line in SOFTWARE_INFO.
            module = importlib.import_module("data.shortcuts." + software_key)
            all_software[software_key] = module.SHORTCUTS
        except (ImportError, AttributeError) as error:
            print("Could not load shortcuts for", software_key, "-", error)
    return all_software


ALL_SOFTWARE = load_all_software()


def get_all_software_names():
    '''Return a list of all software keys that were loaded.'''
    return list(ALL_SOFTWARE.keys())


def get_display_name(software_key):
    '''Return the nice name of a software, e.g. "vs_code" -> "VS Code".'''
    if software_key in SOFTWARE_INFO:
        return SOFTWARE_INFO[software_key]["name"]
    return software_key


def get_shortcuts(software, difficulty=None):
    '''Return a list of Shortcut objects for one software (default argument: all difficulties).'''
    rows = ALL_SOFTWARE.get(software, [])
    if difficulty is not None and difficulty != "all":
        # filter() + lambda keep only the rows with the wanted difficulty
        rows = list(filter(lambda row: row["difficulty"] == difficulty, rows))
    shortcuts = []
    for row in rows:
        shortcuts.append(make_shortcut(software, row))
    return shortcuts


def combine_shortcuts(*software_names, difficulty=None):
    '''Combine the shortcuts of any number of software into one list (*args, PPT 1.4).'''
    combined = []
    for name in software_names:
        combined.extend(get_shortcuts(name, difficulty))
    return combined


def count_items_recursive(data):
    '''Recursive function (PPT 1.4): count shortcut dictionaries inside nested dicts/lists.

    Base case : a dictionary that has a "keys" field is ONE shortcut -> return 1.
    Recursive : for a dictionary or a list, add up the counts of everything inside it.'''
    if isinstance(data, dict) and "keys" in data:
        return 1
    if isinstance(data, dict):
        children = list(data.values())
    elif isinstance(data, list):
        children = data
    else:
        return 0
    total = 0
    for child in children:
        total = total + count_items_recursive(child)
    return total


def count_all_shortcuts():
    '''Return the total number of shortcuts of all software.'''
    return count_items_recursive(ALL_SOFTWARE)


def get_software_by_section():
    '''Return a dictionary: section name -> list of software keys in that section.'''
    groups = {}
    for section in SECTIONS:
        groups[section] = []
    for software_key, info in SOFTWARE_INFO.items():
        if software_key in ALL_SOFTWARE:
            groups[info["section"]].append(software_key)
    return groups
