'''
check_data.py - standalone checker for all shortcut data files.

Run it from the project folder:   python data/check_data.py

It checks that
  * every shortcut has the required fields with allowed values,
  * every key name is one of the allowed canonical names and in canonical order,
  * there is no duplicate key combo inside the same software,
  * Win-key and other system combos use mode "mcq",
and then prints a count table. If something is wrong it exits with an error.
'''

import os
import sys

# NOTE (advanced): this script lives inside the "data" folder, so Python would not find
# the "core" and "data" packages. Adding the project folder to sys.path fixes that.
PROJECT_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_FOLDER)

from core import key_utils                                     # noqa: E402
from data.shortcuts import ALL_SOFTWARE, SOFTWARE_INFO, count_all_shortcuts   # noqa: E402

REQUIRED_FIELDS = ("keys", "action", "category", "difficulty", "mode")
ALLOWED_DIFFICULTY = ("easy", "medium", "hard")
ALLOWED_MODES = ("press", "mcq")
MAX_ACTION_LENGTH = 60


def check_keys(keys):
    '''Return a list of problems with one key-combo text (empty list = OK).'''
    problems = []
    if keys != key_utils.normalize_combo_text(keys):
        problems.append("not canonical, should be '" + key_utils.normalize_combo_text(keys) + "'")
    for step in key_utils.combo_to_key_list(keys):
        main_keys = 0
        for name in step:
            if name not in key_utils.ALLOWED_KEY_NAMES:
                problems.append("unknown key name '" + name + "'")
            if not key_utils.is_modifier(name):
                main_keys = main_keys + 1
        # a step needs exactly one main key; only a lonely modifier like "Win" is also OK
        if main_keys != 1 and not (main_keys == 0 and len(step) == 1):
            problems.append("every step needs exactly one main key")
    return problems


def check_one_shortcut(row):
    '''Return a list of problems for one shortcut dictionary.'''
    problems = []
    for field in REQUIRED_FIELDS:
        if field not in row or str(row[field]).strip() == "":
            problems.append("missing field '" + field + "'")
    if len(problems) > 0:
        return problems
    problems.extend(check_keys(row["keys"]))
    if row["difficulty"] not in ALLOWED_DIFFICULTY:
        problems.append("bad difficulty '" + row["difficulty"] + "'")
    if row["mode"] not in ALLOWED_MODES:
        problems.append("bad mode '" + row["mode"] + "'")
    if len(row["action"]) > MAX_ACTION_LENGTH:
        problems.append("action longer than " + str(MAX_ACTION_LENGTH) + " characters")
    if key_utils.is_system_combo(row["keys"]) and row["mode"] != "mcq":
        problems.append("system combo must use mode 'mcq'")
    return problems


def check_software(software_key, rows):
    '''Check all shortcuts of one software. Returns a list of error lines.'''
    errors = []
    seen_keys = set()        # set: fast check for duplicates
    for number, row in enumerate(rows, start=1):
        for problem in check_one_shortcut(row):
            errors.append(software_key + " #" + str(number) + " " + str(row.get("keys")) + ": " + problem)
        keys = key_utils.normalize_combo_text(str(row.get("keys", "")))
        if keys in seen_keys:
            errors.append(software_key + " #" + str(number) + " " + keys + ": duplicate key combo")
        seen_keys.add(keys)
    return errors


def count_row(rows):
    '''Return the numbers (total, easy, medium, hard, press, mcq) for one software.'''
    easy = len([r for r in rows if r.get("difficulty") == "easy"])
    medium = len([r for r in rows if r.get("difficulty") == "medium"])
    hard = len([r for r in rows if r.get("difficulty") == "hard"])
    press = len([r for r in rows if r.get("mode") == "press"])
    mcq = len([r for r in rows if r.get("mode") == "mcq"])
    return len(rows), easy, medium, hard, press, mcq


def print_table():
    '''Print a count table for every software and the grand total.'''
    print("%-24s %6s %5s %6s %5s %6s %5s" % ("Software", "Total", "Easy", "Medium", "Hard", "Press", "MCQ"))
    print("-" * 64)
    for software_key, rows in ALL_SOFTWARE.items():
        total, easy, medium, hard, press, mcq = count_row(rows)
        print("%-24s %6d %5d %6d %5d %6d %5d" % (software_key, total, easy, medium, hard, press, mcq))
    print("-" * 64)
    print("TOTAL SHORTCUTS:", count_all_shortcuts(), "in", len(ALL_SOFTWARE), "software")


def main():
    '''Run every check, print the table and exit with code 1 if anything is wrong.'''
    errors = []
    for software_key in SOFTWARE_INFO:
        if software_key not in ALL_SOFTWARE:
            errors.append(software_key + ": data file is missing or has no SHORTCUTS list")
    for software_key, rows in ALL_SOFTWARE.items():
        errors.extend(check_software(software_key, rows))
    print_table()
    if len(errors) > 0:
        print("\nPROBLEMS FOUND:", len(errors))
        for line in errors:
            print("  -", line)
        sys.exit("Data check FAILED. Please fix the problems listed above.")
    print("\nData check PASSED. All shortcuts look correct.")


if __name__ == "__main__":
    main()
