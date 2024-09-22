import pygame

import sys

from setting import Settings
from ship import Ship
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()


        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()