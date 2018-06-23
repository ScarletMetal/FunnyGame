class EventDispatcher:
    def __init__(self):
        self.events = {}

    def subscribe(self, name, callback):
        if self.events[name] is None:
            self.events[name] = []
        self.events[name].append(callback)

    def dispatch(self, name, **params):
        if self.events[name] is not None:
            for callback in self.events[name]:
                callback(params)
