# Shortcut Trainer Quiz

A keyboard-shortcut learning quiz in **Python and Tkinter**, built as an MCA mini project (Python Programming, 26CAH-606) at Chandigarh University by **Anshul Kaushik (26MCI10329)** and **Pankaj Kumar (26MCI10317)**. The app teaches the shortcuts of **Windows 11 and 20 popular programs** – **1,325 shortcuts in 21 software** – through MCQ quizzes, real key-press practice, flashcards and statistics.

## Quiz Modes

1. **Guess the Action** – see a shortcut as key caps, choose what it does from 4 answers (keys 1–4 work too).
2. **Guess the Shortcut** – see an action, choose the right key combination.
3. **Mixed MCQ** – both kinds of questions mixed.
4. **Press the Keys** – really press the shortcut; chords like `Ctrl+K, Ctrl+C` are supported.
5. **Speed Run** – 60 seconds, as many correct answers as possible.
6. **Daily Challenge** – the same 10 questions for everyone on the same day.
7. **Revise Weak Shortcuts** – questions from the shortcuts you got wrong most often.
8. **Review Mistakes** – replay the wrong answers of the last quiz.

## Features

- **Real key detection:** Tkinter `<KeyPress>` / `<KeyRelease>` events; held keys light up on an on-screen keyboard.
- **Smart wrong options:** distractors come from similar shortcuts (same category, same modifiers).
- **Scoring:** 10 points + seconds left, −3 for a hint, +20 for every 5 correct answers in a row; grades A+ to F.
- **Motivation:** XP and levels, daily streak, Lives mode (3 hearts) and 18 achievement badges.
- **Learn mode:** searchable cheat sheet (export to .txt) and flashcards.
- **Statistics:** pandas + NumPy analysis and Matplotlib charts inside the window; leaderboard.
- **Themes:** dark and light theme, feedback sounds, full screen with F11.
- **Safe storage:** six CSV files in `saves/`; missing or damaged files never crash the app.

## Where key detection is used

| File | Function | Role |
|------|----------|------|
| `core/key_listener.py` | `TkKeyReader.handle_press()` | Turns Tkinter key events into held keys and finished combos |
| `core/key_utils.py` | `normalize_combo_text()` | Writes every combo in one canonical form, e.g. `Ctrl+Shift+N` |
| `core/key_utils.py` | `combos_match()` | Compares combos as sets of keys (`Ctrl+Plus` = `Ctrl+=`) |
| `core/key_utils.py` | `ChordTracker.add_step()` | Waits 1.5 s for the second step of a chord |
| `core/quiz_engine.py` | `get_wrong_options()` | Uses `combos_match()` so no wrong option equals the answer |

## Run locally

Requires **Python 3.10 or higher** (Tkinter is included with Python on Windows).

```
git clone https://github.com/supremedrip1301-ai/shortcuttrainerquiz.git
cd shortcuttrainerquiz
pip install -r requirements.txt
python main.py
```

`requirements.txt` installs **matplotlib, numpy and pandas**. Progress is saved in the `saves/` folder (created on first start).

## Tests

```
python tests/test_core.py       # 11 test functions -> ALL TESTS PASSED
python data/check_data.py       # validates all 1,325 shortcuts
```

## Project structure

```
main.py            App controller and window
config.py          colours, fonts, timer defaults, file names
core/              quiz_engine, key_utils, key_listener, models, stats, storage, sound
ui/                11 screens + widgets (key caps, timer bar, on-screen keyboard)
data/shortcuts/    one Python file of shortcuts per software (21 files)
tests/             test_core.py
```
