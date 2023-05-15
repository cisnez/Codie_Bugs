#G4M3Object.py
# Game Object Class: This class will extend the Base Object and will be the parent class for all the actual game entities like Player, Alien, and Bullet.

from B453Object import B453Object

class G4M3Object(B453Object):
    def __init__(self, x, y):
        super().__init__(x, y)
