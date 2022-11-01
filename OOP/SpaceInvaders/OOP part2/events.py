import pygame
import sys

class Events:
    def check_keys(self, game_ship):
        # Main loop
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    game_ship.moving_left = True
                if event.key == pygame.K_SPACE:
                    game_ship.fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    game_ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    game_ship.moving_left = False




