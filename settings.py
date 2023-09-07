import pygame


class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """Initialize game's settings"""
        # Screen settings
        # custom :2 lines: getting screen size of monitor
        # get monitor info
        self.screenInfoObject = pygame.display.Info()
        self.screen_height, self.screen_width = (self.screenInfoObject.current_h - 100,
                                                 self.screenInfoObject.current_w - 10)
        self.bg_color = (230, 230, 230)