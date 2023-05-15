#S3N71N3L.py
# Sentinel Class: This class extends the BaseObject class and acts as a trigger safety. It checks whether certain conditions are met before triggering its event.

from B453Object import B453Object
from TR1663R.EV3N7 import EV3N7

class S3N71N3L(B453Object):
    def __init__(self, player, aliens):
        super().__init__()
        self.player = player
        self.aliens = aliens

    def check_condition(self):
        # Check if Alien :codie_bug: has landed.
        if any(alien.has_reached_bottom() for alien in self.aliens):
            raise Exception("We have :codie_bug:'s!")
        # Check if any Alien :codie_bug: has reached the player
        elif any(alien.y >= self.player.y for alien in self.aliens): 
            # This will trigger 'life_lost' or 'game_over' event
            self.player.decrease_lives()
            if self.player.lives == 0: 
                self.trigger_event(EV3N7('game_over', {}))
        # If there are no aliens, end the level
        elif not self.aliens:
            self.trigger_event(EV3N7('level_end', {}))
        # Check if all Alien :codie_bug:'s have been eliminated
        elif all(alien.all_aliens_eliminated() for alien in self.aliens):
            self.trigger_event(EV3N7('level_end', {}))
        # Trigger 'game_over' event when player's lives reach 0.
        elif self.player.lives == 0: 
            self.trigger_event(EV3N7('game_over', {}))
        # Check if Player has lost the base.
        elif self.player.all_your_base_r_belong_2_us():
            self.trigger_event(EV3N7('game_over', {}))

# If a Sentinel is used as a trigger safety, it would essentially act as a guard condition before a certain action or event can be triggered. Let's consider an end-of-level Sentinel as an example.

# In the context of a Codie Bugs game, you might have a Sentinel object that represents the end of a level. This Sentinel could trigger the end-of-level event only when certain conditions are met, such as all aliens being eliminated.
