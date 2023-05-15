#G4M3Object.py
# Extends the Base Object class and acts as a parent class for specific game entities like the Player, Alien, and Bullet.

from B453Object import B453Object

class G4M3Object(B453Object):
    def __init__(self, x, y):
        super().__init__(x, y)
