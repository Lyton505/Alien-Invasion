import sys, pygame


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        pygame.init()

        # custom :2 lines: getting screen size of monitor
        self.screenInfoObject = pygame.display.Info()
        self.x_height, self.y_width = (self.screenInfoObject.current_h,
                                       self.screenInfoObject.current_w)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Incredible Alien Invasion Game")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # custom: 1 : try block to handle quitting game from keyboard
            try:
                # make the most recently drawn screen visible
                pygame.display.flip()
            except KeyboardInterrupt as kbInter:
                print(f"\nKeyboard interrupt. Stopped running")
                sys.exit(0)


if __name__ == '__main__':
    # Make game instance and run game
    # custom: 1: try block
    ai = AlienInvasion()
    ai.run_game()

