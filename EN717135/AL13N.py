#AL13N.py
# Alien Class:

from G4M3Object import G4M3Object

class AL13N(G4M3Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 20  # Add a radius attribute for drawing the circle
        self.direction = 1  # Aliens start moving to the right
        self.speed = 10  # Adjust to control the speed of the aliens
        self.down_speed = 10  # Adjust to control how much the aliens move down after hitting a wall

    def move(self, direction):
        self.x += self.speed * direction

    # Check if the alien has reached the bottom of the screen
    def has_reached_bottom(self):
        return self.y > 600
    
    # Check if there are any alien objects above the bottom of the display surface
    def all_aliens_eliminated(self):
        return self.y > 600
