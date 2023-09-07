import pygame


class UglyElf:
    """Ugly elf character that randomly appears out of nowhere"""

    def __init__(self, ai_game):
        """Initialize elf and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/klaowner.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = (20,30)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
