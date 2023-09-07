import sys, pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))

        pygame.display.set_caption("Incredible Alien Invasion Game")
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # custom: 1 : try block to handle quitting game from keyboard
            try:
                self.screen.fill(self.settings.bg_color)
                self.ship.blitme()
                # make the most recently drawn screen visible
                pygame.display.flip()
            except Exception as exp:
                print(f"\nException Stopped running")
                sys.exit(-1)
            else:
                self.clock.tick(60)


if __name__ == '__main__':
    # Make game instance and run game
    # custom: 1: try block
    ai = AlienInvasion()
    ai.run_game()
