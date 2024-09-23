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
            self._update_screen()
            self.clock.tick(60)
    '''We are wainting for closing the game'''
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    '''We are filling screen and using blitme to display PC'''

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
