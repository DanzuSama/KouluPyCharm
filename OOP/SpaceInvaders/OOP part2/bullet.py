import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    total_number_of_bullet = 0  # class variable

    def __init__(self, ship, game):
        super().__init__()
        self.screen = game.screen
        self.rect = pygame.Rect(0, 0, game.settings.bullet_width, game.settings.bullet_height)
        self.rect.midtop = ship.rect.midtop
        self.y = float(self.rect.y)
        self.settings = game.settings

        Bullet.total_number_of_bullet += 1
        print(self.total_number_of_bullet)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)