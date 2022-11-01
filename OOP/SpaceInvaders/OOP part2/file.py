import pygame
import sys
import test
from ship import Ship
from settings import Settings
from events import Events
from alien import Alien

class SpaceInvaders:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.bg_image = pygame.image.load('images/starfield.png').convert_alpha()
        self.ship = Ship(self)
        #new code
        self.aliens = pygame.sprite.Group()
        self.aliens = Alien(self)

        #end
        self.events = Events()

    def run(self):
        while True:
            self.events.check_keys(self.ship)
            self.screen.blit(self.bg_image, self.screen.get_rect())
            #self.screen.fill(self.settings.bg_color)
            self.ship.blit()
            self.ship.update()
            self.aliens.blit()
            self.aliens.update()


            self.ship.bullets.update()

            for b in self.ship.bullets: # draw bullets
                b.draw_bullet() # draw bullet
            pygame.display.flip()


if __name__ == '__main__':
    game = SpaceInvaders()
    game.run()
