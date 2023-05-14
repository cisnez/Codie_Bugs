#BULL37.py
# Bullet Class:

from G4M3Object import G4M3Object

class BULL37(G4M3Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 5  # Add a width attribute for drawing the rectangle
        self.height = 10  # Add a height attribute for drawing the rectangle

    def move(self):
        self.y -= 5  # Bullets move up the screen

    def collides_with(self, alien):
        # Check if the distance between the bullet's center and the alien's center is less than or equal to the alien's radius.
        distance = ((self.x - alien.x)**2 + (self.y - alien.y)**2)**0.5
        return distance <= alien.radius