import pygame
from pygame.midi import time
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(0, 0, 100, 50)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.settings = game.settings
        self.image = pygame.image.load('images/alien.bmp').convert_alpha()

        self.game = game

    def update(self):
        self.rect.x += self.settings.alien_speed * 0.1

    def blit(self):
        self.screen.blit(self.image, self.rect)
