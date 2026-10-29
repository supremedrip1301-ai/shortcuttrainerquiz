'''
sound.py - short feedback sounds with winsound.Beep (Windows only).

If winsound is missing (other systems) or sound is turned off, the functions
simply do nothing, so the app never crashes because of sound.
'''

import threading

try:
    import winsound
except ImportError:
    winsound = None


def beep(frequency, duration):
    '''Play one beep (frequency in Hz, duration in milliseconds). Errors are ignored.'''
    if winsound is None:
        return
    try:
        winsound.Beep(frequency, duration)
    except RuntimeError:
        pass                 # no sound device: stay silent


def play_tones(tones, enabled=True):
    '''Play a list of (frequency, duration) tones one after another.'''
    if not enabled or winsound is None:
        return

    def run():
        '''Play every tone in the list.'''
        for frequency, duration in tones:
            beep(frequency, duration)

    # NOTE (advanced): winsound.Beep waits until the sound is finished. In a GUI that would
    # freeze the window, so the beeps are played in a small background thread.
    threading.Thread(target=run, daemon=True).start()


def play_correct(enabled=True):
    '''Happy rising sound for a correct answer.'''
    play_tones([(880, 90), (1320, 120)], enabled)


def play_wrong(enabled=True):
    '''Low sound for a wrong answer.'''
    play_tones([(330, 220)], enabled)


def play_tick(enabled=True):
    '''Very short tick for the last seconds of the timer.'''
    play_tones([(1000, 40)], enabled)


def play_achievement(enabled=True):
    '''Little melody when a badge is unlocked.'''
    play_tones([(784, 90), (988, 90), (1175, 160)], enabled)
