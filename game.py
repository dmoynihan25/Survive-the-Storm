import pygame
import sys
from grid import grid
from time import sleep
from player1 import Player1


pygame.init()

#define grid
TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

grass = pygame.image.load("images/grass.png")
yardline = pygame.image.load("images/yardline.png")
endzone = pygame.image.load("images/endzone.png")

ground_type = [grass, yardline, endzone]

tile_rect = grass.get_rect()

#draw screen with background
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
player1 = Player1()

w_loc = 0
h_loc = 0
#draw each tile onto our background
for row in grid:
    for i in row:
        #blit the correct tile onto the screen
        screen.blit(ground_type[i], (w_loc, h_loc))
        w_loc += TILE_SIZE
    h_loc += TILE_SIZE
    w_loc = 0
#while loop that runs the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #check for keydown events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_d:
                player1.moving_right = True
            elif event.key == pygame.K_a:
                player1.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player1.moving_right = False
            elif event.key == pygame.K_a:
                player1.moving_left = False


    player1.update()
    
    player1.draw()
    pygame.display.set_caption("Survive the Storm")
    pygame.display.flip()