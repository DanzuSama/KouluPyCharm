import sys
from ship import Ship

import pygame


class Settings:

    def __init__(self):
        # Screen settings
        self.caption = 'Space Invaders'
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1

        #bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 255)

        #alien settings
        self.alien_speed = 1

