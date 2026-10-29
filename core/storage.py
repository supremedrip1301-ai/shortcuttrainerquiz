'''
storage.py - saving and loading everything in CSV files (csv module + normal file handling).

Files (inside the "saves" folder):
    players.csv           one row per player
    history.csv           one row per finished quiz
    mistakes.csv          how often a player got each shortcut wrong
    settings.csv          app settings (key, value)
    achievements.csv      unlocked badges
    software_results.csv  correct answers per software in each quiz

Every load function handles a missing or empty file and returns default values,
so the app never crashes on the first start. Every function has a "folder"
default argument; the tests pass a temporary folder instead.
'''

import csv
import datetime
import os

import config
from core.models import Player

PLAYER_FIELDS = ["name", "avatar", "xp", "pin", "streak", "last_played", "quizzes",
                 "best_streak", "fixed_count", "created"]
HISTORY_FIELDS = ["date_time", "player", "mode", "software_list", "total", "correct", "wrong",
                  "skipped", "score", "accuracy", "grade", "time_taken"]
MISTAKE_FIELDS = ["player", "software", "keys", "wrong_count", "last_seen"]
SETTING_FIELDS = ["key", "value"]
ACHIEVEMENT_FIELDS = ["player", "badge_id", "date"]
SOFTWARE_RESULT_FIELDS = ["date_time", "player", "software", "total", "correct"]


# ---------------------------------------------------------------- basic helpers

def ensure_folder(folder=config.SAVES_DIR):
    '''Create the saves folder if it does not exist yet.'''
    os.makedirs(folder, exist_ok=True)


def read_rows(file_name, folder=config.SAVES_DIR):
    '''Read a CSV file and return a list of dictionaries. Missing file -> empty list.'''
    path = os.path.join(folder, file_name)
    try:
        with open(path, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []
    except (OSError, csv.Error) as error:
        print("Could not read", path, "-", error)
        return []


def write_rows(file_name, fields, rows, folder=config.SAVES_DIR):
    '''Write all rows into a CSV file (the old content is replaced).'''
    ensure_folder(folder)
    path = os.path.join(folder, file_name)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def append_row(file_name, fields, row, folder=config.SAVES_DIR):
    '''Add one row at the end of a CSV file (the header is written for a new file).'''
    ensure_folder(folder)
    path = os.path.join(folder, file_name)
    is_new = not os.path.exists(path) or os.path.getsize(path) == 0
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def to_int(text, default=0):
    '''Turn text from a CSV file into a whole number; damaged values give the default.'''
    try:
        return int(float(text))
    except (TypeError, ValueError):
        return default


def now_text():
    '''Return the current date and time as text, e.g. "2026-10-18 14:05:09".'''
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------- players

def load_players(folder=config.SAVES_DIR):
    '''Return a dictionary: player name -> Player object.'''
    players = {}
    for row in read_rows(config.PLAYERS_FILE, folder):
        try:
            players[row["name"]] = Player(row["name"], row["avatar"], row["xp"], row["pin"],
                                          row["streak"], row["last_played"], row["quizzes"],
                                          row["best_streak"], row["fixed_count"], row["created"])
        except (KeyError, ValueError):
            continue                     # skip a damaged row instead of crashing
    return players


def save_player(player, folder=config.SAVES_DIR):
    '''Add or update one player in players.csv.'''
    players = load_players(folder)
    players[player.name] = player
    rows = []
    for p in players.values():
        rows.append(p.to_dict())
    write_rows(config.PLAYERS_FILE, PLAYER_FIELDS, rows, folder)


def delete_rows_of_player(file_name, fields, player_name, folder=config.SAVES_DIR):
    '''Remove every row of one player from a CSV file.'''
    rows = read_rows(file_name, folder)
    kept = [row for row in rows if row.get("player") != player_name]
    write_rows(file_name, fields, kept, folder)


def reset_player_progress(player, folder=config.SAVES_DIR):
    '''Reset XP, streaks, history, mistakes and badges of one player (name and PIN stay).'''
    fresh = Player(player.name, player.avatar, 0, player.get_pin_for_saving())
    save_player(fresh, folder)
    delete_rows_of_player(config.HISTORY_FILE, HISTORY_FIELDS, player.name, folder)
    delete_rows_of_player(config.MISTAKES_FILE, MISTAKE_FIELDS, player.name, folder)
    delete_rows_of_player(config.ACHIEVEMENTS_FILE, ACHIEVEMENT_FIELDS, player.name, folder)
    delete_rows_of_player(config.SOFTWARE_RESULTS_FILE, SOFTWARE_RESULT_FIELDS, player.name, folder)
    return fresh


# ---------------------------------------------------------------- settings

def load_settings(folder=config.SAVES_DIR):
    '''Return the settings dictionary (defaults are used for missing keys).'''
    settings = dict(config.DEFAULT_SETTINGS)       # copy, so the defaults are not changed
    for row in read_rows(config.SETTINGS_FILE, folder):
        if "key" in row and row["key"] in settings:
            settings[row["key"]] = row["value"]
    # numbers must really be numbers, otherwise the default value is used
    for key in ("seconds", "questions"):
        if not str(settings[key]).isdigit():
            settings[key] = config.DEFAULT_SETTINGS[key]
    return settings


def save_settings(settings, folder=config.SAVES_DIR):
    '''Write the settings dictionary into settings.csv.'''
    rows = []
    for key, value in settings.items():
        rows.append({"key": key, "value": value})
    write_rows(config.SETTINGS_FILE, SETTING_FIELDS, rows, folder)


# ---------------------------------------------------------------- history

def add_history(player_name, summary, mode_label=None, folder=config.SAVES_DIR):
    '''Save one finished quiz into history.csv and software_results.csv.'''
    if mode_label is None:
        mode_label = summary["mode_name"]
    date_time = now_text()
    row = {"date_time": date_time, "player": player_name, "mode": mode_label,
           "software_list": "|".join(summary["software_list"]),
           "total": summary["total"], "correct": summary["correct"], "wrong": summary["wrong"],
           "skipped": summary["skipped"], "score": summary["score"],
           "accuracy": summary["accuracy"], "grade": summary["grade"],
           "time_taken": summary["time_taken"]}
    append_row(config.HISTORY_FILE, HISTORY_FIELDS, row, folder)
    for software, numbers in summary["per_software"].items():
        result = {"date_time": date_time, "player": player_name, "software": software,
                  "total": numbers[0], "correct": numbers[1]}
        append_row(config.SOFTWARE_RESULTS_FILE, SOFTWARE_RESULT_FIELDS, result, folder)


def load_history(player_name=None, folder=config.SAVES_DIR):
    '''Return the history rows (all players, or only one player).'''
    rows = read_rows(config.HISTORY_FILE, folder)
    if player_name is None:
        return rows
    return [row for row in rows if row.get("player") == player_name]


def load_software_results(player_name, folder=config.SAVES_DIR):
    '''Return the software_results rows of one player.'''
    rows = read_rows(config.SOFTWARE_RESULTS_FILE, folder)
    return [row for row in rows if row.get("player") == player_name]


def daily_done_today(player_name, today=None, folder=config.SAVES_DIR):
    '''True if the player already finished today's Daily Challenge.'''
    if today is None:
        today = datetime.date.today()
    for row in load_history(player_name, folder):
        if row.get("mode") == "Daily Challenge" and row.get("date_time", "").startswith(str(today)):
            return True
    return False


# ---------------------------------------------------------------- mistakes (weak shortcuts)

def update_mistake(player_name, software, keys, was_correct, folder=config.SAVES_DIR):
    '''Wrong answer -> wrong_count + 1. Correct answer -> wrong_count - 1 (simple spaced repetition).

    Returns True when a weak shortcut was "fixed" (its count went down to 0).'''
    rows = read_rows(config.MISTAKES_FILE, folder)
    found = None
    for row in rows:
        if row["player"] == player_name and row["software"] == software and row["keys"] == keys:
            found = row
            break
    fixed = False
    if found is None:
        if was_correct:
            return False                 # never wrong before, nothing to remember
        found = {"player": player_name, "software": software, "keys": keys, "wrong_count": 0}
        rows.append(found)
    count = to_int(found["wrong_count"])
    if was_correct:
        count = count - 1
        if count <= 0:
            fixed = True
            rows.remove(found)           # no longer a weak shortcut
    else:
        count = count + 1
    found["wrong_count"] = count
    found["last_seen"] = now_text()
    write_rows(config.MISTAKES_FILE, MISTAKE_FIELDS, rows, folder)
    return fixed


def load_mistakes(player_name, folder=config.SAVES_DIR):
    '''Return the weak shortcuts of one player, the most wrong first.'''
    rows = [row for row in read_rows(config.MISTAKES_FILE, folder) if row.get("player") == player_name]
    for row in rows:
        row["wrong_count"] = to_int(row["wrong_count"])
    return sorted(rows, key=lambda row: row["wrong_count"], reverse=True)


# ---------------------------------------------------------------- achievements

def load_achievements(player_name, folder=config.SAVES_DIR):
    '''Return a dictionary: badge id -> date unlocked, for one player.'''
    unlocked = {}
    for row in read_rows(config.ACHIEVEMENTS_FILE, folder):
        if row.get("player") == player_name:
            unlocked[row["badge_id"]] = row["date"]
    return unlocked


def unlock_achievement(player_name, badge_id, folder=config.SAVES_DIR):
    '''Save a newly unlocked badge (only once).'''
    if badge_id in load_achievements(player_name, folder):
        return
    row = {"player": player_name, "badge_id": badge_id, "date": str(datetime.date.today())}
    append_row(config.ACHIEVEMENTS_FILE, ACHIEVEMENT_FIELDS, row, folder)
