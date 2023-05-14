#PL4Y3R.py
# Player Class:

from G4M3Object import G4M3Object
from EN717135.BULL37 import BULL37

class PL4Y3R(G4M3Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.shoot_bullet = False
        # Player starts with 3 lives
        self.lives = 3 

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            self.trigger_event('game_over')
        else:
            self.trigger_event('level_end')

    def move(self, dx, dy):
        self.x = (self.x + dx) % 800
        self.y = (self.y + dy) % 600

    def shoot(self):
        if self.shoot_bullet:
            self.shoot_bullet = False
            # Return a new bullet instance that starts at the player's current location
            return BULL37(self.x, self.y)
        else:
            return None

    def should_shoot(self):
        self.shoot_bullet = True

    # check whether the player has moved off the right side of the screen.
    def all_your_base_r_belong_2_us(self):
        return self.x <= 0 or self.x >= 800

# Please note that this is a simple demonstration. In a real game, you would want to add bounds checking to make sure the player doesn't move off the screen, and the player's movement would generally be controlled by the user's input, not random.

# As for exception handling, it would be useful if you could provide more context about what exceptions you expect to handle. Generally, you would want to wrap any part of the code that could raise an exception in a try/except block, and then handle the exception in a way that is appropriate for your specific application.