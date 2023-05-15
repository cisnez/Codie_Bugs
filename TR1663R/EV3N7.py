#EV3N7.py
# Event Class: Represents an event that can be triggered during the game, such as a player losing a life or an alien being hit.

class EV3N7:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data

    def get_type(self):
        return self.event_type

    def get_data(self):
        return self.data
