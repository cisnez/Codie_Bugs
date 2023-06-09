#G4M3.py
# This is the main Game class that manages the overall game. It initializes the game, creates and manages all game objects, handles user input, updates the game state, and defines the conditions for the game to end.

# Note: This Game class has a Sentinel as an attribute. It creates a new Sentinel when a level starts and defines the condition that must be met for the play to end.

# The event processing loop is the run() method of the G4M3 class.

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
from TR1663R.EV3N7 import EV3N7

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
        self.player.add_listener('game_over', self)
        self.player.add_listener('life_lost', self)
        self.player_speed = 15

        # Aliens start moving to the left
        self.alien_direction = -1  

        # Call a new Sentinel 
        self.level_end_sentinel = S3N71N3L(self.player, self.aliens)
        self.level_end_sentinel.add_listener('game_over', self)
        self.level_end_sentinel.add_listener('level_end', self)

    # The start_level method is called within the handle_event function when the life_lost and next_level events occur. It also initializes the level_end_sentinel.
    def start_level(self):
        print("You are starting a level!\nGet ready for the next push!")
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
        self.level_end_sentinel.add_listener('game_over', self)
        self.level_end_sentinel.add_listener('level_end', self)

    class GameOverException(Exception):
        pass
    # The handle_event function has events like alien_hit, power_up, bullet_fired, and player_move which are placeholders with pass in their body. These do not currently do anything.
    # These placeholders are represented to help guide development of new features.
    def handle_event(self, event):
        event_type = event.get_type()
        if event_type == 'life_lost':
            print("A life was lost!")
            # Start the same level again
            self.start_level()
        elif event_type == 'game_over':
            print("Game over!")
            self.game_over = True
            raise G4M3.GameOverException()
        elif event_type == 'level_end':
            print("Next level!")
            # Start the next level
            self.start_level()
        elif event_type == 'alien_hit':
            print("Alien was hit!")
            # Implement your 'alien_hit' logic here
            pass  
        elif event_type == 'power_up':
            print("Power up!")
            # Implement your 'power_up' logic here
            pass
        elif event_type == 'bullet_fired':
            print("Bullet fired!")
            # Implement your 'bullet_fired' logic here
            pass
        elif event_type == 'player_move':
            print("Player moved!")
            # Implement your 'player_move' logic here
            pass
        # add any other events as needed
        # elif event == 'another_event':
        #     do_something()

    # # 4.
    # You'll notice I've used the concept of listeners and events, and each game object is a "message" in its own right, having state and behavior. The queue could be used for handling the game loop, user input, or any other buffered sequence of actions. A "sentinel" could be a game object that represents some special condition or event in the game (like a power-up or an end-of-level marker). A "trigger" could be a specific game event or condition that triggers some action (like an alien reaching the bottom of the screen or the player's score reaching a certain value).

    # You'll probably also want to update your game to handle other events, like keyboard or mouse input. For example, to make the player move when the arrow keys are pressed, you could add something like this in your event processing loop:

    # First, let's add a basic game loop to your G4M3 class:
    # When a Pygame window is open, it needs to process system events regularly in order to let the operating system know that it is still responsive. System events include things like mouse movements, button clicks, and also signals that the window should close (like when you click the 'X' button on the window frame). If these events are not processed regularly, the operating system will consider the window unresponsive.
    # To process these events, you need to call pygame.event.pump() or pygame.event.get() regularly.
    #   pygame.event.pump() - function internally processes Pygame events. It handles window-related events such as resizing, minimizing, etc. If you do not call pump() function and are not using get() or poll(), your game window might become unresponsive.
    #   pygame.event.get() - function typically used in the game loop to continuously check for events. Unlike event.pump(), event.get() not only processes Pygame events but also retrieves them so you can handle the events in your game code. In most cases, you would use get() instead of pump() because you usually want to handle events, not just process them.
    def run(self):
        try:
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
        except G4M3.GameOverException:
            print("The game has ended. Thanks for playing!")
        finally:
            pygame.quit()
    # This run method will keep the game running, constantly updating and drawing the game state. We're using a simple time.sleep call to delay each frame and control the game speed. This is a simple way to achieve this, but a real game might use a more complex method to control frame rate.

    # Next, we need to implement the update_game_state and draw_game_state methods. These will be responsible for moving all game objects and checking for collisions (update_game_state), and for drawing all game objects to the screen (draw_game_state). For now, these methods can be very simple:
    
    # Responsible for moving all game objects and checking for collisions (update_game_state)
    def update_game_state(self):
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
                    # Remove alien that hit the player
                    if alien in self.aliens:
                        try:
                            self.aliens.remove(alien)
                        except ValueError:
                            print("Tried to remove an alien that was not in the list.")

        # Move bullets and check for collisions
        for bullet in self.bullets:
            bullet.move()
            for alien in self.aliens:
                if bullet.collides_with(alien):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    break

    # Responsible for drawing all game objects to the Pygame display surface (draw_game_state). 
    # Pygame provides several methods for drawing shapes, images, and text. 
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

    # This is a very simple implementation of the game loop and game state updates. In a real game, you would likely use a game library or framework to handle drawing graphics, moving game objects with physics, and handling user input.

# Finally, you'll need to create an instance of your G4M3 class and call its run method to start the game:
if __name__ == '__main__':
    try:
        game = G4M3()
        game.start_level()
        game.run()
    finally:
        pygame.quit()
