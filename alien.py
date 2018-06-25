import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):

        """initialise the alien and set it's starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute"""
        self.image = pygame.image.load('Images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (ai_settings.alien_width, ai_settings.alien_height))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen, adding a space to the left_
        # equal to the height and a space on the top equal to the width

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien on the screen at its current location"""
        self.screen.blit(self.image, self.rect)




