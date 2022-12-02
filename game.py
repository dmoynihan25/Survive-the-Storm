import pygame
import sys
from grid import draw_background
from player1 import Player1
from player2 import Player2
from fan1 import FansRight
from fans_top import FansTop
from fans_bottom import FansBottom
from random import *
from power_up import Drink

#init pygame
pygame.init()

#set clock variable
clock = pygame.time.Clock()

#load sound file
file = 'impact1.mp3'
file2 = 'crowd.mp3'

#define grid and window size
TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE


#draw screen with background
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg = draw_background((WINDOW_WIDTH, WINDOW_HEIGHT))

#def player classes and fans
player1 = Player1()
player2 = Player2()
drink = Drink()
fans = pygame.sprite.Group()
#def font, special font
font = pygame.font.SysFont("Segoe UI", 24)


# initialize hit time for p1 and p2
hit_time = 0.0
hit_time2 = 0.0

#the bigger the value for this, the more people will spawn.
fan_frequency = .004
def _create_fan():
    """Create an alien, if conditions are right."""
    # Every tick a random numb between 0-1 is generated, if it is less than the assigned fan_freq value, a fan will spawn
    if random() < fan_frequency:
        #assign variables for fan functions
        fan_r = FansRight()
        fan_t = FansTop()
        fan_b = FansBottom()

        #add fans to each side
        fans.add(fan_r)
        fans.add(fan_t)
        fans.add(fan_b)


def _check_player1_fan_collisions():
    collisions = pygame.sprite.spritecollide(player1, fans, True)
    #allow hit time to be tracked
    global hit_time
    if collisions:
        # collision occurred, record hit time and slow player down
        hit_time = pygame.time.get_ticks()
        player1.speed *= .5
        impact = pygame.mixer.Sound(file)
        pygame.mixer.Sound.play(impact)
    if pygame.time.get_ticks() - hit_time >= 2000:
        # if slowing interval is over, speed player back up to full speed
        player1.speed = 0.2


def _check_player2_fan_collisions():
    collisions = pygame.sprite.spritecollide(player2, fans, True)
    global hit_time2
    #when false, I get a bunch of ouchs printed. Since I only want one hit to register, i am going to kill the fans.
    if collisions:
        # collision occurred, record hit time and slow player down
        hit_time2 = pygame.time.get_ticks()
        #half player speed
        player2.speed *= .5
        #play sound to indicated that player is injured
        impact = pygame.mixer.Sound(file)
        pygame.mixer.Sound.play(impact)
    if pygame.time.get_ticks() - hit_time2 >= 2000:
        # if slowing interval is over, speed player back up to full speed
        player2.speed = 0.2

def _check_player1_drink_collision():
    #check to see if the rects of the player and the drink have overlapped, does not kill power up
    collisions = pygame.sprite.collide_rect(player1, drink)
    if collisions:
        #if they are, add to player speed, player speed limited to three
        player1.speed += .1

def _check_player2_drink_collision():
    # check to see if the rects of the player and the drink have overlapped, does not kill power up
    collisions = pygame.sprite.collide_rect(player2, drink)
    if collisions:
        # if they are, add to player speed, player speed limited to three
        player2.speed += .1

#save score
score = 10000
def timer():
    """Function that starts with a score then subtracts as time goes"""
    global score
    #for every tick subtract 1 from the score
    score -= 1
    #display the score in the top left, changes every refresh, dynamic
    img = font.render(f'Score: {score/10}', True, (230, 230, 230))
    img_rect = img.get_rect()
    img_rect.topleft = screen.get_rect().topleft
    screen.blit(img, img_rect)
    pygame.display.flip()

def end_game_p1():
    """function that ends the game and displays who won: player1 version"""
    #allow the score to be displayed
    global score
    screen.fill((100, 200, 100))
    img = font.render(f'GAME OVER: Player 1 Survived. Score: {score/10}', True, (230, 230, 230))
    img_rect = img.get_rect()
    img_rect.center = screen.get_rect().center
    screen.blit(img, img_rect)
    pygame.display.flip()

def end_game_p2():
    global score
    """function that ends the game and displays who won: player2 version"""
    screen.fill((100, 200, 100))
    img = font.render(f'GAME OVER: Player 2 Survived. Score: {score}', True, (230, 230, 230))
    img_rect = img.get_rect()
    img_rect.center = screen.get_rect().center
    screen.blit(img, img_rect)
    pygame.display.flip()

#set flag for playing a continuos sound
playsound = True

#while loop that runs the game
while True:
    #a tick rate of 60 was VERY slow but this seemed to work
    clock.tick(1000)

    #since the flag is true, this if statement runs
    if playsound:
        #load and play the sound that is continuos
        #Finn Prescott helped me with this
        crowd = pygame.mixer.Sound(file2)
        pygame.mixer.Sound.play(crowd)
        #after the sound plays, set the flag to false to it does not run again, and the sound only plays once
        playsound = False

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
        #if the player reaches, display the end screen for player 1
        end_game_p1()
        continue
    if player2.rect.x == 768:
        # if the player reaches, display the end screen for player 1
        end_game_p2()
        continue
    #functions run while the while loop is true
    screen.blit(bg, bg.get_rect())
    player1.update()
    player1.draw()
    player2.update()
    player2.draw()
    _create_fan()
    drink.update()
    drink.draw()
    fans.update()
    fans.draw(screen)
    _check_player1_fan_collisions()
    _check_player2_fan_collisions()
    _check_player1_drink_collision()
    _check_player2_drink_collision()
    timer()
    #pygame.time.Clock.tick(60)

    pygame.display.set_caption("Survive the Storm")
    #monkeys flip the painting
    pygame.display.flip()