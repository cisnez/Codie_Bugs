#G4M3.py
# Game Class: This class would manage the overall game, including creating and managing all the game objects, handling user input, and updating the game state.
# 2 Game Class: The Game class might have a Sentinel as an attribute. It could create this Sentinel when a new level starts and define the condition that must be met for the level to end.

# The event processing loop is located in the run method of the G4M3 class:

import time

# To integrate Pygame into your existing game, you would typically start by initializing Pygame and creating a display surface in your G4M3 class
import pygame

from B453Object import B453Object
from G4M3Object import G4M3Object
# This syntax directly imports the specified classes from their respective modules. It allows you to use the class names directly in your code without having to reference the module name explicitly. For example, you can use AL13N() instead of EN717135.AL13N.AL13N().
from EN717135.AL13N import AL13N
from EN717135.BULL37 import BULL37
from EN717135.PL4Y3R import PL4Y3R
from TR1663R.S3N71N3L import S3N71N3L

class G4M3(B453Object):
    def __init__(self):
        super().__init__()
        pygame.init()
        # Game On!
        self.game_over = False

        # Create a display surface of 800x600 pixels
        self.screen = pygame.display.set_mode((800, 600))  

        # Call Aliens, Bullets, and Players
        self.aliens = []
        self.bullets = []
        # Initialize player at the bottom center of the screen
        self.player = PL4Y3R((800 - 50) / 2, 600 - 50)
        self.player_speed = 5

        # Aliens start moving to the left
        self.alien_direction = -1  

        # Call Sentinel
        self.level_end_sentinel = None

        
    def start_new_level(self):
        print("You eliminated all the codie bugs!\nGet ready for the next push!")
        # Clear bullets
        self.bullets = []
        # Create aliens in rows
        self.aliens = []
        # Creates 5 rows of aliens
        for row in range(5):
            # Creates 10 aliens per row
            for col in range(10):
                # Spacing aliens by 60 pixels and offsetting them by 50 pixels from the edge
                self.aliens.append(AL13N(col * 60 + 50, row * 60 + 50)) 
        
        # Create level end Sentinel
        self.level_end_sentinel = S3N71N3L(self.player, self.aliens)
        self.level_end_sentinel.add_listener(self)

    def handle_event(self, event):
        if event == 'level_end':
            print("Level completed!")
            # start a new level after the current one is completed
            self.start_new_level()
        elif event == 'game_over':
            print("Game over!")
            self.game_over = True
            # Additional game over logic here

    # Other game methods omitted for brevity

    # # 4.
    # You'll notice I've used the concept of listeners and events, and each game object is a "message" in its own right, having state and behavior. The queue could be used for handling the game loop, user input, or any other buffered sequence of actions. A "sentinel" could be a game object that represents some special condition or event in the game (like a power-up or an end-of-level marker). A "trigger" could be a specific game event or condition that triggers some action (like an alien reaching the bottom of the screen or the player's score reaching a certain value).
    #
    # Please note that this is a very basic skeleton structure. A real game would require more sophisticated handling of game physics, graphics rendering, user input, sound, and more. You'd also want to add more game-specific logic to the methods of these classes, and you may need to add more methods and classes

    # # 2.
    # In this case, the Sentinel's condition is the all_aliens_eliminated method, which checks whether there are any aliens left. If all aliens are eliminated, the Sentinel triggers its event, and the game responds accordingly.

    # This is a simplified example and a real game might have more complex conditions and responses. It's also worth noting that the handle_event method could handle various different events, and you might want to use something more sophisticated than string comparison for the event types.

    # First, let's add a basic game loop to your G4M3 class:
    # When a Pygame window is open, it needs to process system events regularly in order to let the operating system know that it is still responsive. System events include things like mouse movements, button clicks, and also signals that the window should close (like when you click the 'X' button on the window frame). If these events are not processed regularly, the operating system will consider the window unresponsive.
    # To process these events, you need to call pygame.event.pump() or pygame.event.get() regularly. 
    def run(self):
        while not self.game_over:
            # Get the state of all keyboard keys
            keys = pygame.key.get_pressed() 
            # If 'a' or the left arrow key is pressed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:  
                self.player.move(-self.player_speed, 0)
            # If 'd' or the right arrow key is pressed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]: 
                self.player.move(self.player_speed, 0)
            # If 'space' or 'w' or the up arrow key is pressed
            if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
                self.player.should_shoot()

            # Process system events
            for event in pygame.event.get():  
                # The 'X' button was clicked
                if event.type == pygame.QUIT:  
                    return
                # This will keep your window responsive and also allow you to close the window by clicking the 'X' button.
            self.update_game_state()
            self.draw_game_state()
            self.level_end_sentinel.check_condition()
            time.sleep(0.1)
    # This run method will keep the game running, constantly updating and drawing the game state. We're using a simple time.sleep call to delay each frame and control the game speed. This is a simple way to achieve this, but a real game might use a more complex method to control frame rate.

    # Next, we need to implement the update_game_state and draw_game_state methods. These will be responsible for moving all game objects and checking for collisions (update_game_state), and for drawing all game objects to the screen (draw_game_state). For now, these methods can be very simple:
    def update_game_state(self):
        # Not move the player by default
        self.player.move(0, 0) 

        # Add a new bullet to the list for every call to player.shoot
        new_bullet = self.player.shoot()
        if new_bullet is not None:
            self.bullets.append(new_bullet)

        # check if there are any aliens left
        if self.aliens:
            rightmost_alien_x = max(alien.x for alien in self.aliens)
            leftmost_alien_x = min(alien.x for alien in self.aliens)
            if rightmost_alien_x + self.aliens[0].speed > 800 or leftmost_alien_x - self.aliens[0].speed < 0:
                self.alien_direction *= -1
                for alien in self.aliens:
                    alien.y += alien.down_speed

            for alien in self.aliens:
                alien.move(self.alien_direction)
                # Alien has reached the player
                if alien.y >= self.player.y:
                    # Decrease player's lives
                    self.player.decrease_lives()

        # Move bullets and check for collisions
        for bullet in self.bullets:
            bullet.move()
            for alien in self.aliens:
                if bullet.collides_with(alien):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    break

    def draw_game_state(self):
        # Clear the screen by filling it with black
        self.screen.fill((0, 0, 0)) 

        # Draw the player as a white rectangle
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.player.x, self.player.y, 50, 50))  

         # Draw aliens
        for alien in self.aliens:
            pygame.draw.circle(self.screen, (0, 255, 0), (alien.x, alien.y), alien.radius)
    
        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height))
        
        # Update the display
        pygame.display.flip()  
    #     In your draw_game_state method, you would draw your game objects onto the Pygame display surface. Pygame provides several methods for drawing shapes, images, and text. 

    # This is a very simple implementation of the game loop and game state updates. In a real game, you would likely use a game library or framework to handle drawing graphics, moving game objects with physics, and handling user input.

# Finally, you'll need to create an instance of your G4M3 class and call its run method to start the game:
if __name__ == '__main__':
    try:
        game = G4M3()
        game.start_new_level()
        game.run()
    finally:
        pygame.quit()
