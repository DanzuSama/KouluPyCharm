import pygame
import bullet


class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.settings = game.settings

        # bullet
        self.game = game
        self.bullets = pygame.sprite.Group()

        # asetetaan
        self.moving_right = False
        self.moving_left = False

        self.x = float(self.rect.x)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed


        # self.rect.x = self.x

    def fire_bullet(self):
        
        new_bullet = bullet.Bullet(self, self.game)  # self = ship
        self.bullets.add(new_bullet)  # lisätään ryhmään

    def update_bullet(self):
        self.bullets.update()

