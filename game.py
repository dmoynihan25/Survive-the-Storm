import pygame
import sys
from grid import draw_background
from time import time
from player1 import Player1
from player2 import Player2
from fan1 import FansRight
from fans_top import FansTop
from random import *
from pygame.sprite import Sprite



pygame.init()

file = 'impact1.mp3'

#define grid
TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE


#draw screen with background
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
player1 = Player1()
player2 = Player2()
fans = pygame.sprite.Group()
bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.SysFont(None, 24)

fan_frequency = .004

def _create_fan():
    """Create an alien, if conditions are right."""
    if random() < fan_frequency:
        fan_r = FansRight()
        fan_t = FansTop()


        fans.add(fan_r)
        fans.add(fan_t)
        #fans.add(fan_b)

hit_time = 0

def _check_player1_fan_collisions():
    collisions = pygame.sprite.spritecollide(player1, fans, True)
    if collisions:
        hit_time = pygame.time.get_ticks()
        player1.speed -= .07
    if pygame.time.get_ticks() - hit_time >= 2000:
        player1.speed += .07

        #player1.speed = player1.speed / 1.5
        #pygame.mixer.music.load(file)
        #pygame.mixer.music.play()
        #pygame.event.wait()

def _check_player2_fan_collisions():
    collisions = pygame.sprite.spritecollide(player2, fans, True)
    #when false, I get a bunch of ouchs printed. Since I only want one hit to register, i am going to kill the fans.
    if collisions:
        player2.speed = player2.speed / 1.5
        #pygame.mixer.music.load(file)
        #pygame.mixer.music.play()
        #pygame.event.wait()

def end_game_p1():
    #function that ends the game and displays who won: player1 version
    screen.fill((100, 200, 100))
    img = font.render(f'GAME OVER: Payer 1 Survived', True, (230, 230, 230))
    img_rect = img.get_rect()
    img_rect.center = screen.get_rect().center
    screen.blit(img, img_rect)
    pygame.display.flip()
def end_game_p2():
    #function that ends the game and displays who won: player2 version
    screen.fill((100, 200, 100))
    img = font.render('GAME OVER: Payer 2 Survived', True, (230, 230, 230))
    img_rect = img.get_rect()
    img_rect.center = screen.get_rect().center
    screen.blit(img, img_rect)
    pygame.display.flip()



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
    #if statement that checks for player x to see if they made it to the endzone
    if player1.rect.x == 768:
        end_game_p1()
        continue
    if player2.rect.x == 768:
        end_game_p2()
        continue

    screen.blit(bg, bg.get_rect())
    player1.update()
    player1.draw()
    player2.update()
    player2.draw()
    _create_fan()
    fans.update()
    fans.draw(screen)
    _check_player1_fan_collisions()
    _check_player2_fan_collisions()

    pygame.display.set_caption("Survive the Storm")
    pygame.display.flip()