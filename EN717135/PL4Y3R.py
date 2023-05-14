#PL4Y3R.py
# Player Class:

from G4M3Object import G4M3Object
from EN717135.BULL37 import BULL37
import random

class PL4Y3R(G4M3Object):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        self.x += dx
        self.y += dy

    def shoot(self):
        # Return a new bullet instance that starts at the player's current location
        return BULL37(self.x, self.y)


    def all_your_base_r_belong_2_us(self):
        return self.x <= 0

# Please note that this is a simple demonstration. In a real game, you would want to add bounds checking to make sure the player doesn't move off the screen, and the player's movement would generally be controlled by the user's input, not random.

# As for exception handling, it would be useful if you could provide more context about what exceptions you expect to handle. Generally, you would want to wrap any part of the code that could raise an exception in a try/except block, and then handle the exception in a way that is appropriate for your specific application.