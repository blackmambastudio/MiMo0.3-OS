

class EventBus:
    def __init__(self, socket):
        self.socket = socket
        self.topics = {}

    def add(self, topic, callback):
        self.topics[topic] = callback

    def emit(self, topic, params=None):
        self.topics[topic](params)
