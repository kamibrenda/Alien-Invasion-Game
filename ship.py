import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize he ship and set its stating position."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 

        #Store a decimal value for the ships centre.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """"Update the ship's position based on the movement  flag."""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
            self.rect.centerx += 1

        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx -= 1

        #Update rect object from self.centre.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        