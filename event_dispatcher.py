class EventDispatcher:
    def __init__(self):
        self.events = {}

    def subscribe(self, name, callback):
        try:
            self.events[name].append(callback)
        except KeyError:
            self.events[name] = [callback]

    def dispatch(self, name, **params):
        if self.events[name] is not None:
            for callback in self.events[name]:
                callback(**params)


game_dispatcher = EventDispatcher()
