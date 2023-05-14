#G4M3Object.py
# Game Object Class: This class will extend BaseObject and will be the parent class for all the actual game entities like Player, Alien, and Bullet.

from B453Object import B453Object

class G4M3Object(B453Object):
    def __init__(self, x, y):
        super().__init__(x, y)

# You'll probably also want to update your game to handle other events, like keyboard or mouse input. For example, to make the player move when the arrow keys are pressed, you could add something like this in your event processing loop:

# python
# ```
# if event.type == pygame.KEYDOWN:  # A key was pressed
#     if event.key == pygame.K_LEFT:  # The left arrow key was pressed
#         self.player.move(-1, 0)
#     elif event.key == pygame.K_RIGHT:  # The right arrow key was pressed
#         self.player.move(1, 0)
#     elif event.key == pygame.K_UP:  # The up arrow key was pressed
#         self.player.move(0, -1)
#     elif event.key == pygame.K_DOWN:  # The down arrow key was pressed
#         self.player.move(0, 1)
# ```
# This is just a simple example and there are many ways to handle input in Pygame, but this should be enough to get you started.
