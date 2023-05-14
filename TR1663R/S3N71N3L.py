#S3N71N3L.py
# Sentinel Class: This class extends the BaseObject class and acts as a trigger safety. It checks whether certain conditions are met before triggering its event.

from B453Object import B453Object

class S3N71N3L(B453Object):
    def __init__(self, player, aliens):
        super().__init__()
        self.player = player
        self.aliens = aliens

    def check_condition(self):
        if all(alien.all_aliens_eliminated() for alien in self.aliens):
            self.trigger_event('level_end')
        # In this case, the condition is a callable (like a function) that returns a boolean value. If the condition is met (i.e., it returns True), the Sentinel triggers the 'level_end' event.
        elif self.player.all_your_base_r_belong_2_us():
            self.trigger_event('game_over')

# If a Sentinel is used as a trigger safety, it would essentially act as a guard condition before a certain action or event can be triggered. Let's consider an end-of-level Sentinel as an example.

# In the context of a Codie Bugs game, you might have a Sentinel object that represents the end of a level. This Sentinel could trigger the end-of-level event only when certain conditions are met, such as all aliens being eliminated.