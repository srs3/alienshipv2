class Settings():
    """ A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """ Initialize the game's settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed_factor = 6.0

        # bullet settings
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien settings
        self.alien_height = 40
        self.alien_width = 40






