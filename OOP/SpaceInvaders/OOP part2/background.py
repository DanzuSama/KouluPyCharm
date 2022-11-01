import math

import pygame
#https://coderslegacy.com/python/pygame-scrolling-background/
class Background:
    def __init__(self, game):
        self.bg_image = pygame.image.load('images/starfield.png').convert_alpha()
        self.rect = self.bg_image.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = self.rect.bg_image.height

        self.screen = game.screen

        self.screen_rect = game.screen.get_rect()




    def blit(self):
        pass

    def update(self):
        pass