#EV3N7.py
# Event Class: This class extends the BaseObject class and acts as a trigger safety. It checks whether certain conditions are met before triggering its event.

class EV3N7:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data

    def get_type(self):
        return self.event_type

    def get_data(self):
        return self.data
