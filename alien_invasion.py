import sys, pygame
from settings import Settings
from ship import Ship
from ugly_elf import UglyElf


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
        self.elf = UglyElf(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            self._check_events()

            # custom: 1 : try block to handle quitting game from keyboard
            try:
                self._update_screen()
            except Exception as exp:
                print(f"\nException Stopped running")
                sys.exit(-1)
            else:
                self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.elf.blitme()
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make game instance and run game
    # custom: 1: try block
    ai = AlienInvasion()
    ai.run_game()
