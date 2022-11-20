import pygame
import sys
from grid import draw_background
from time import sleep
from player1 import Player1
from player2 import Player2
from fan1 import Fans
from random import *
from pygame.sprite import Sprite



pygame.init()

#define grid
TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE
fan_frequency = .005

#draw screen with background
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
player1 = Player1()
player2 = Player2()
fans = pygame.sprite.Group()
bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))


def _create_fan():
    """Create an alien, if conditions are right."""
    if random() < fan_frequency:
        fan = Fans()
        fans.add(fan)


#while loop that runs the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #check for keydown events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            #PLAYER 1 ON FLAGS
            if event.key == pygame.K_d:
                player1.moving_right = True
            elif event.key == pygame.K_a:
                player1.moving_left = True
            elif event.key == pygame.K_w:
                player1.moving_up = True
            elif event.key == pygame.K_s:
                player1.moving_down = True
            #PLAYER 2 ON FLAGS
            elif event.key == pygame.K_RIGHT:
                player2.moving_right = True
            elif event.key == pygame.K_LEFT:
                player2.moving_left = True
            elif event.key == pygame.K_UP:
                player2.moving_up = True
            elif event.key == pygame.K_DOWN:
                player2.moving_down = True

        #check for keyup events
        elif event.type == pygame.KEYUP:
            #PLAYER 1 OFF FLAGS
            if event.key == pygame.K_d:
                player1.moving_right = False
            elif event.key == pygame.K_a:
                player1.moving_left = False
            elif event.key == pygame.K_w:
                player1.moving_up = False
            elif event.key == pygame.K_s:
                player1.moving_down = False
            #PLAYER 2 OFF FLAGS
            elif event.key == pygame.K_RIGHT:
                player2.moving_right = False
            elif event.key == pygame.K_LEFT:
                player2.moving_left = False
            elif event.key == pygame.K_UP:
                player2.moving_up = False
            elif event.key == pygame.K_DOWN:
                player2.moving_down = False


    screen.blit(bg, bg.get_rect())
    player1.update()
    player1.draw()
    player2.update()
    player2.draw()
    _create_fan()
    fans.update()
    fans.draw(screen)

    pygame.display.set_caption("Survive the Storm")
    pygame.display.flip()