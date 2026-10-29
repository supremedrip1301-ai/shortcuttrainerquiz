'''
test_core.py - simple tests with plain assert statements (no pytest needed).

Run from the project folder:   python tests/test_core.py
Every test function prints "ok" when it passes. A failed assert stops the script.
'''

import os
import queue
import sys
import tempfile

# NOTE (advanced): this file is inside the "tests" folder, so the project folder is added
# to sys.path to be able to import the "core" and "data" packages.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from core import key_utils, quiz_engine, stats, storage      # noqa: E402
from core.key_listener import TkKeyReader                    # noqa: E402
from core.models import Player                               # noqa: E402
from data.shortcuts import count_all_shortcuts, count_items_recursive   # noqa: E402


class FakeTkEvent:
    '''A tiny object that looks like a Tkinter key event (keysym, keycode, state).'''

    def __init__(self, keysym, keycode, state=0):
        '''Store the three values a real Tkinter event has.'''
        self.keysym = keysym
        self.keycode = keycode
        self.state = state


def read_combos(event_queue):
    '''Return the list of "combo" messages waiting in a queue.'''
    combos = []
    while not event_queue.empty():
        kind, value = event_queue.get()
        if kind == "combo":
            combos.append(value)
    return combos


def test_key_names():
    '''Tkinter keysyms and Windows virtual-key codes (event.keycode) -> canonical names.'''
    assert key_utils.name_from_tk_event("Control_L", 17) == "Ctrl"
    assert key_utils.name_from_tk_event("Alt_R", 18) == "Alt"
    assert key_utils.name_from_tk_event("Shift_R", 16) == "Shift"
    assert key_utils.name_from_tk_event("Win_L", 91) == "Win"
    assert key_utils.name_from_tk_event("Prior", 33) == "PageUp"
    assert key_utils.name_from_tk_event("a", 65) == "A"            # Ctrl+A: keycode is still 65
    assert key_utils.name_from_tk_event("KP_End", 97) == "Numpad 1"
    assert key_utils.name_from_tk_event("equal", 187) == "="
    assert key_utils.name_from_tk_event("slash", 191) == "/"
    assert key_utils.name_from_tk_event("exclam", 49) == "1"       # Shift+1 is still the 1 key
    print("ok  test_key_names")


def test_normalise_and_match():
    '''Canonical order, Shift as a modifier, Plus equivalence and chords.'''
    assert key_utils.normalize_combo_text("shift+ctrl+n") == "Ctrl+Shift+N"
    assert key_utils.normalize_combo_text("Win+Ctrl+D") == "Ctrl+Win+D"
    assert key_utils.build_combo({"Shift", "Ctrl"}, "N") == "Ctrl+Shift+N"
    assert key_utils.combos_match("Ctrl+Plus", "Ctrl+=")
    assert key_utils.combos_match("Ctrl++", "Ctrl+=")
    assert key_utils.combos_match("Ctrl+Numpad +", "Ctrl+=")
    assert not key_utils.combos_match("Ctrl+N", "Ctrl+Shift+N")
    assert key_utils.combos_match("ctrl+k, ctrl+c", "Ctrl+K, Ctrl+C")
    assert not key_utils.combos_match("Ctrl+K", "Ctrl+K, Ctrl+C")
    assert key_utils.split_step("Ctrl+Numpad +") == ["Ctrl", "Numpad +"]
    assert key_utils.format_combo_for_display("Ctrl+K, Ctrl+C") == "Ctrl + K  then  Ctrl + C"
    assert key_utils.is_system_combo("Shift+Win+S")
    assert key_utils.is_system_combo("Alt+Tab")
    assert not key_utils.is_system_combo("Ctrl+C")
    print("ok  test_normalise_and_match")


def test_chord_tracker():
    '''The first step of a chord is remembered for 1.5 seconds.'''
    tracker = key_utils.ChordTracker(1.5)
    finished, text = tracker.add_step("Ctrl+K", "Ctrl+K, Ctrl+C", now=100.0)
    assert finished is False and text == "Ctrl+K"
    finished, text = tracker.add_step("Ctrl+C", "Ctrl+K, Ctrl+C", now=101.0)
    assert finished is True and text == "Ctrl+K, Ctrl+C"
    # too slow: the first step is forgotten and the new combo is judged alone
    tracker.add_step("Ctrl+K", "Ctrl+K, Ctrl+C", now=200.0)
    finished, text = tracker.add_step("Ctrl+C", "Ctrl+K, Ctrl+C", now=205.0)
    assert finished is True and text == "Ctrl+C"
    # a normal single combo finishes at once
    finished, text = tracker.add_step("Ctrl+S", "Ctrl+S", now=300.0)
    assert finished is True and text == "Ctrl+S"
    print("ok  test_chord_tracker")


def test_key_repeat_and_release():
    '''Holding a key down (auto-repeat) gives only ONE combo; released keys leave the set.'''
    events = queue.Queue()
    reader = TkKeyReader(events)
    reader.handle_press(FakeTkEvent("Control_L", 17))
    reader.handle_press(FakeTkEvent("k", 75, key_utils.TK_CTRL_MASK))
    reader.handle_press(FakeTkEvent("k", 75, key_utils.TK_CTRL_MASK))      # auto-repeat
    assert read_combos(events) == ["Ctrl+K"]
    reader.handle_release(FakeTkEvent("k", 75, key_utils.TK_CTRL_MASK))
    reader.handle_press(FakeTkEvent("c", 67, key_utils.TK_CTRL_MASK))
    assert read_combos(events) == ["Ctrl+C"]
    reader.handle_release(FakeTkEvent("c", 67))
    reader.handle_release(FakeTkEvent("Control_L", 17))
    assert reader.held_keys == set()
    print("ok  test_key_repeat_and_release")


def test_tk_fallback():
    '''The Tkinter key reader reads modifiers from the event.state bits.'''
    events = queue.Queue()
    reader = TkKeyReader(events)
    reader.handle_press(FakeTkEvent("Control_L", 17))
    reader.handle_press(FakeTkEvent("s", 83, key_utils.TK_CTRL_MASK | key_utils.TK_SHIFT_MASK))
    reader.handle_press(FakeTkEvent("F4", 115, key_utils.TK_ALT_MASK))
    assert read_combos(events) == ["Ctrl+Shift+S", "Alt+F4"]
    print("ok  test_tk_fallback")


def test_question_generation():
    '''4 unique options, exactly one correct, no repeated question in one quiz.'''
    for mode in ("action", "shortcut", "mixed"):
        questions = quiz_engine.generate_questions(["vs_code", "ms_excel"], 30, "all", mode)
        assert len(questions) == 30
        seen = set()
        for q in questions:
            assert len(q.options) == 4
            assert len(set([o.lower() for o in q.options])) == 4
            correct_text = q.get_correct_answer_text()
            assert q.options[q.correct_index] == correct_text
            assert q.options.count(correct_text) == 1
            key = (q.shortcut.software, q.shortcut.keys)
            assert key not in seen
            seen.add(key)
    press = quiz_engine.generate_questions(["windows_general"], 50, "all", "press")
    assert all([q.shortcut.mode == "press" for q in press])
    daily_one = [q.shortcut.keys for q in quiz_engine.generate_daily_questions()]
    daily_two = [q.shortcut.keys for q in quiz_engine.generate_daily_questions()]
    assert daily_one == daily_two and len(daily_one) == 10
    print("ok  test_question_generation")


def test_grade_and_points():
    '''Grade (slide if-elif-else) and the scoring rules.'''
    assert quiz_engine.get_grade(100) == "A+"
    assert quiz_engine.get_grade(90) == "A"
    assert quiz_engine.get_grade(85) == "B"
    assert quiz_engine.get_grade(70) == "C"
    assert quiz_engine.get_grade(60) == "D"
    assert quiz_engine.get_grade(59.9) == "F"
    assert quiz_engine.calculate_points(True, 5, 1, False) == 15
    assert quiz_engine.calculate_points(True, 5, 1, True) == 12
    assert quiz_engine.calculate_points(False, 9, 0, False) == 0
    assert quiz_engine.calculate_points(True, 0, 5, False) == 30      # streak bonus
    print("ok  test_grade_and_points")


def test_sessions():
    '''Lives mode ends the quiz; the summary counts correctly; Speed Run adds questions.'''
    questions = quiz_engine.generate_questions(["youtube"], 5, "all", "action")
    session = quiz_engine.QuizSession(questions, "action", ["youtube"], 20, lives_mode=True)
    for i in range(3):
        session.current_question().check_option((session.current_question().correct_index + 1) % 4)
        session.record_answer(False)
        session.next_question()
    assert session.is_finished() and session.lives == 0
    session.finish()
    summary = session.get_summary()
    assert summary["total"] == 3 and summary["wrong"] == 3 and summary["grade"] == "F"
    speed = quiz_engine.SpeedRunSession(["gmail"])
    start_count = len(speed.questions)
    for i in range(start_count - 1):
        speed.next_question()
    assert len(speed.questions) > start_count
    assert isinstance(speed, quiz_engine.TimedQuizSession)
    print("ok  test_sessions")


def test_player_and_counting():
    '''Player XP / level / private PIN, and the recursive counter.'''
    player = Player("Asha", pin="1234")
    assert player.add_xp(60, 50) is True and player.get_level() == 2
    assert player.check_pin("1234") and not player.check_pin("0000")
    try:
        print(player.__pin)
        assert False, "private attribute should not be reachable"
    except AttributeError:
        pass
    assert count_items_recursive({"a": [{"keys": "A"}, {"keys": "B"}], "b": [{"keys": "C"}]}) == 3
    assert count_all_shortcuts() >= 600
    print("ok  test_player_and_counting")


def test_storage_and_stats():
    '''Save and load everything in a temporary folder.'''
    with tempfile.TemporaryDirectory() as folder:
        assert storage.load_players(folder) == {}
        assert storage.load_settings(folder)["theme"] == "dark"
        assert stats.get_player_summary("Ravi", folder)["quizzes"] == 0
        player = Player("Ravi", "#e74c3c", 120, "77")
        storage.save_player(player, folder)
        loaded = storage.load_players(folder)["Ravi"]
        assert loaded.get_xp() == 120 and loaded.check_pin("77")
        settings = storage.load_settings(folder)
        settings["theme"] = "light"
        storage.save_settings(settings, folder)
        assert storage.load_settings(folder)["theme"] == "light"
        questions = quiz_engine.generate_questions(["figma"], 4, "all", "action")
        session = quiz_engine.QuizSession(questions, "action", ["figma"])
        for q in session.questions:
            q.check_option(q.correct_index)
            session.record_answer(True, 10)
            session.next_question()
        session.finish()
        summary = session.get_summary()
        storage.add_history("Ravi", summary, None, folder)
        assert len(storage.load_history("Ravi", folder)) == 1
        assert stats.get_player_summary("Ravi", folder)["avg_accuracy"] == 100.0
        assert stats.get_leaderboard_rows("All", "figma", folder)[0]["player"] == "Ravi"
        assert storage.update_mistake("Ravi", "figma", "V", False, folder) is False
        storage.update_mistake("Ravi", "figma", "V", False, folder)
        assert storage.load_mistakes("Ravi", folder)[0]["wrong_count"] == 2
        assert storage.update_mistake("Ravi", "figma", "V", True, folder) is False
        assert storage.update_mistake("Ravi", "figma", "V", True, folder) is True
        assert storage.load_mistakes("Ravi", folder) == []
        storage.unlock_achievement("Ravi", "first_steps", folder)
        storage.unlock_achievement("Ravi", "first_steps", folder)
        assert list(storage.load_achievements("Ravi", folder).keys()) == ["first_steps"]
        badges = stats.check_new_achievements(loaded, summary, {}, folder)
        assert "first_steps" in badges
    print("ok  test_storage_and_stats")


def test_damaged_files():
    '''Damaged or empty save files must not crash the app.'''
    with tempfile.TemporaryDirectory() as folder:
        with open(os.path.join(folder, "history.csv"), "w", encoding="utf-8") as f:
            f.write("this is not\na real,,,csv file\n")
        with open(os.path.join(folder, "players.csv"), "w", encoding="utf-8") as f:
            f.write("")
        with open(os.path.join(folder, "mistakes.csv"), "w", encoding="utf-8") as f:
            f.write("player,software,keys,wrong_count,last_seen\nRavi,figma,V,abc,\n")
        assert stats.get_player_summary("Ravi", folder)["quizzes"] == 0
        assert stats.get_accuracy_trend("Ravi", 20, folder) == ([], [])
        assert storage.load_players(folder) == {}
        assert storage.load_mistakes("Ravi", folder)[0]["wrong_count"] == 0
    print("ok  test_damaged_files")


if __name__ == "__main__":
    test_key_names()
    test_normalise_and_match()
    test_chord_tracker()
    test_key_repeat_and_release()
    test_tk_fallback()
    test_question_generation()
    test_grade_and_points()
    test_sessions()
    test_player_and_counting()
    test_storage_and_stats()
    test_damaged_files()
    print("\nALL TESTS PASSED")
