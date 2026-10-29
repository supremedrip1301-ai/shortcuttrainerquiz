'''
key_listener.py - detects real key presses with Tkinter's own key events (PPT 3.4).

The quiz screen binds <KeyPress> and <KeyRelease> (widget.bind(event, handler)) and
passes every event object to TkKeyReader. The reader turns the events into small
messages (tuples) and puts them into a queue.Queue:
    ("raw", "You Entered Control_L")   the key exactly as Tkinter reports it
    ("held", ["Ctrl", "K"])            the keys that are held down right now
    ("combo", "Ctrl+K")                a finished combo (modifiers + one main key)
The quiz screen reads the queue every 30 ms with after() (QuizScreen.poll_keys).
'''

from core import key_utils


class TkKeyReader:
    '''Reads Tkinter <KeyPress> / <KeyRelease> events and sends key messages into a queue.'''

    def __init__(self, event_queue):
        '''event_queue is a queue.Queue that the quiz screen reads with after().'''
        self.event_queue = event_queue
        self.held_keys = set()          # set of key names held down right now

    def reset_held(self):
        '''Forget all held keys (used at the start of every question).'''
        self.held_keys.clear()

    def handle_press(self, event):
        '''Turn one Tkinter KeyPress event into queue messages.'''
        self.event_queue.put(("raw", "You Entered " + event.keysym))
        name = key_utils.name_from_tk_event(event.keysym, event.keycode)
        if name == "":
            return
        if name in self.held_keys and not key_utils.is_modifier(name):
            return                          # auto-repeat while the key is held: ignore
        self.held_keys.add(name)
        self.event_queue.put(("held", sorted(self.held_keys)))
        if key_utils.is_modifier(name):
            return
        # modifiers come from the event.state bit masks (+ the Win key from our own set)
        modifiers = key_utils.modifiers_from_tk_state(event.state)
        if "Win" in self.held_keys:
            modifiers.add("Win")
        self.event_queue.put(("combo", key_utils.build_combo(modifiers, name)))

    def handle_release(self, event):
        '''Remove a released key from the set of held keys.'''
        name = key_utils.name_from_tk_event(event.keysym, event.keycode)
        if name in self.held_keys:
            self.held_keys.remove(name)
        self.event_queue.put(("held", sorted(self.held_keys)))
