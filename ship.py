import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initialise the starting position of the ship"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get it's rect

        self.image = pygame.image.load('Images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (35, 70))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # ship movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update ret object from self.center
        self.rect.centerx = self.center



    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

