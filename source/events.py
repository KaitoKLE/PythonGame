class Event:
    def __init__(self, type, data):
        self._type = type
        self._data = data

    @property
    def type(self):
        return self._type

    @property
    def data(self):
        return self._data


class EventManager:
    def __init__(self):
        self._listeners = {}

    def register_listener(self, event_type, listener):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    def dispatch_event(self, event):
        for listener in self._listeners.get(event.type, []):
            listener.on_event(event)


# EXAMPLE OF USE:
# class DummyPlayer:
#     def __init__(self):
#         self._x = 0
#         self._y = 0
#
#     @property
#     def pos(self):
#         return self._x, self._y
#
#     def on_event(self, event):
#         if event.type == PlayerMove:
#             if event.data == "left":
#                 self._x -= 1
#             elif event.data == "right":
#                 self._x += 1
#
#
# if __name__ == "__main__":
#     event_manager = EventManager()
#     dummy_player = DummyPlayer()
#
#     print(dummy_player.pos)
#
#     event_manager.register_listener(PlayerMove, dummy_player)
#
#     # Simulate key press events
#     event_manager.dispatch_event(PlayerMove("left"))
#
#     print(dummy_player.pos)
