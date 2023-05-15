#AL13N.py
# Alien Class: Represents an alien in the game, handling its movements, collisions, and interactions with other game objects.

from G4M3Object import G4M3Object

class AL13N(G4M3Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        # Add a radius attribute for drawing the circle
        self.radius = 20 
        # Aliens start moving to the right
        self.direction = 1
        # Adjust to control the speed of the aliens
        self.speed = 20
        # Adjust to control how much the aliens move down after hitting a wall
        self.down_speed = 20

    def move(self, direction):
        self.x += self.speed * direction

    # Check if the alien has reached the bottom of the screen
    def has_reached_bottom(self):
        return self.y > 600
