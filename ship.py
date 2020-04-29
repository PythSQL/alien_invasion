import pygame
 
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates the ships position."""
        if self.moving_right and self.moving_up and self.rect.right < self.screen_rect.right and self.y > 0:
            self.x += self.settings.ship_speed
            self.y -= self.settings.ship_speed
        elif self.moving_right and self.moving_down and self.rect.right < self.screen_rect.right and self.rect.bottom < self.screen_rect.bottom:
            self.x += self.settings.ship_speed
            self.y += self.settings.ship_speed
        elif self.moving_left and self.moving_up and self.rect.left > 0 and self.y > 0:
            self.x -= self.settings.ship_speed
            self.y -= self.settings.ship_speed
        elif self.moving_left and self.moving_down and self.rect.left > 0 and self.rect.bottom < self.screen_rect.bottom:
            self.x -= self.settings.ship_speed
            self.y += self.settings.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.moving_up and self.y > 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update the rec's position
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers the ship."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
