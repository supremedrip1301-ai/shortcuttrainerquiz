'''
stats.py - statistics with NumPy and pandas, data for the charts, leaderboard and badges.

pandas reads history.csv exactly like the slide example:  penguins = pd.read_csv("penguins.csv")
'''

import os

import numpy as np
import pandas as pd

import config
from core import storage
from data.shortcuts import get_display_name


# ---------------------------------------------------------------- reading with pandas

def load_history_dataframe(player_name=None, folder=config.SAVES_DIR):
    '''Read history.csv into a pandas DataFrame. Missing or empty file -> empty DataFrame.'''
    path = os.path.join(folder, config.HISTORY_FILE)
    try:
        # dtype=str for text columns, so a player called "123" is not read as a number
        history = pd.read_csv(path, dtype={"player": str, "software_list": str, "mode": str})
        if player_name is not None:
            history = history[history["player"] == player_name]
        # damaged numbers become NaN and are then replaced by 0
        for column in ("accuracy", "score", "time_taken"):
            history[column] = pd.to_numeric(history[column], errors="coerce").fillna(0)
    except (OSError, ValueError, KeyError):
        # missing file, empty file (EmptyDataError is a ValueError) or damaged file
        return pd.DataFrame(columns=storage.HISTORY_FIELDS)
    return history


def load_software_dataframe(player_name, folder=config.SAVES_DIR):
    '''Read software_results.csv for one player into a DataFrame.'''
    path = os.path.join(folder, config.SOFTWARE_RESULTS_FILE)
    try:
        results = pd.read_csv(path, dtype={"player": str, "software": str})
        results = results[results["player"] == player_name]
        for column in ("total", "correct"):
            results[column] = pd.to_numeric(results[column], errors="coerce").fillna(0)
    except (OSError, ValueError, KeyError):
        return pd.DataFrame(columns=storage.SOFTWARE_RESULT_FIELDS)
    return results


# ---------------------------------------------------------------- player statistics

def get_player_summary(player_name, folder=config.SAVES_DIR):
    '''Return a dictionary with total quizzes, average accuracy, best score and favourite software.'''
    history = load_history_dataframe(player_name, folder)
    summary = {"quizzes": len(history), "avg_accuracy": 0.0, "best_score": 0,
               "favourite": "-", "total_time": 0}
    if len(history) == 0:
        return summary
    accuracy = np.array(history["accuracy"], dtype=float)      # NumPy array
    scores = np.array(history["score"], dtype=float)
    summary["avg_accuracy"] = round(float(np.mean(accuracy)), 1)
    summary["best_score"] = int(np.max(scores))
    summary["total_time"] = int(np.sum(np.array(history["time_taken"], dtype=float)))
    results = load_software_dataframe(player_name, folder)
    if len(results) > 0:
        # value_counts() counts how often each software was played; the first one is the favourite
        favourite_key = results["software"].value_counts().index[0]
        summary["favourite"] = get_display_name(favourite_key)
    return summary


def get_accuracy_trend(player_name, last=20, folder=config.SAVES_DIR):
    '''Return two lists (quiz numbers, accuracy values) for the last N quizzes.'''
    history = load_history_dataframe(player_name, folder)
    history = history.tail(last)
    y_values = list(np.array(history["accuracy"], dtype=float))
    x_values = list(range(1, len(y_values) + 1))
    return x_values, y_values


def get_accuracy_per_software(player_name, folder=config.SAVES_DIR):
    '''Return a dictionary: software display name -> accuracy % over all quizzes.'''
    results = load_software_dataframe(player_name, folder)
    if len(results) == 0:
        return {}
    totals = results.groupby("software")[["total", "correct"]].sum()
    accuracy = {}
    for software, row in totals.iterrows():
        if row["total"] > 0:
            accuracy[get_display_name(software)] = round(row["correct"] * 100 / row["total"], 1)
    return accuracy


def get_best_accuracy_per_software(player_name, folder=config.SAVES_DIR):
    '''Return a dictionary: software key -> best accuracy % in one quiz (for the home cards).'''
    best = {}
    for row in storage.load_software_results(player_name, folder):
        total = storage.to_int(row["total"])
        if total == 0:
            continue
        accuracy = round(storage.to_int(row["correct"]) * 100 / total)
        if accuracy > best.get(row["software"], -1):
            best[row["software"]] = accuracy
    return best


def get_overall_accuracy(player_name, folder=config.SAVES_DIR):
    '''Return the accuracy over all answered questions of a player (0 if none).'''
    rows = storage.load_history(player_name, folder)
    total = sum([storage.to_int(row["total"]) for row in rows])
    correct = sum([storage.to_int(row["correct"]) for row in rows])
    if total == 0:
        return 0.0
    return round(correct * 100 / total, 1)


# ---------------------------------------------------------------- leaderboard

def get_leaderboard_rows(mode="All", software="All", folder=config.SAVES_DIR):
    '''Return the history rows sorted by score, highest first (sorted + lambda, PPT 1.4).'''
    rows = storage.load_history(None, folder)
    if mode != "All":
        rows = [row for row in rows if row["mode"] == mode]
    if software != "All":
        rows = [row for row in rows if software in row["software_list"].split("|")]
    for row in rows:
        row["score"] = storage.to_int(row["score"])
    return sorted(rows, key=lambda row: row["score"], reverse=True)


# ---------------------------------------------------------------- achievements

def get_software_accuracy(summary, *software_keys):
    '''Return (total, accuracy) in this quiz for the given software keys (*args).'''
    total = 0
    correct = 0
    for key in software_keys:
        if key in summary["per_software"]:
            total = total + summary["per_software"][key][0]
            correct = correct + summary["per_software"][key][1]
    if total == 0:
        return 0, 0.0
    return total, correct * 100 / total


def software_badge_earned(summary, *software_keys):
    '''True if this quiz had 10+ questions of these software with 90%+ accuracy.'''
    total, accuracy = get_software_accuracy(summary, *software_keys)
    return total >= 10 and accuracy >= 90


def check_new_achievements(player, summary, unlocked, folder=config.SAVES_DIR):
    '''Return a list of badge ids that this quiz has just unlocked.'''
    history = storage.load_history(player.name, folder)
    played_software = set()
    for row in storage.load_software_results(player.name, folder):
        played_software.add(row["software"])
    total = summary["total"]
    rules = {
        "first_steps": len(history) >= 1,
        "on_fire": player.best_streak >= 10,
        "perfectionist": total >= 20 and summary["accuracy"] >= 100,
        "speed_demon": summary["mode"] == "speed" and summary["correct"] >= 25,
        "windows_wizard": software_badge_earned(summary, "windows_general", "windows_file_explorer"),
        "photoshop_pro": software_badge_earned(summary, "adobe_photoshop"),
        "blender_master": software_badge_earned(summary, "blender"),
        "coder": software_badge_earned(summary, "vs_code"),
        "office_hero": software_badge_earned(summary, "ms_word", "ms_excel", "ms_powerpoint"),
        "polyglot": len(played_software) >= 10,
        "daily_habit": player.streak >= 7,
        "comeback": player.fixed_count >= 20,
        "key_master": summary["mode"] == "press" and summary["correct"] >= 10,
        "early_bird": summary["mode"] == "daily",
        "marathon": len(history) >= 25,
        "level_5": player.get_level() >= 5,
        "no_hints": total >= 10 and summary["hints_used"] == 0 and summary["grade"] in ("A", "A+"),
        "survivor": summary["lives_mode"] and total >= 10 and summary["lives_left"] == config.LIVES,
    }
    new_badges = []
    for badge_id, earned in rules.items():
        if earned and badge_id not in unlocked:
            new_badges.append(badge_id)
    return new_badges
