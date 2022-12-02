import pygame
from pygame.sprite import Sprite

#set important settings, same from other classes

TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

class Player2(Sprite):
    def __init__(self):
        #load image and get the rect for it
        self.image = pygame.image.load("images/player2.png")
        self.rect = self.image.get_rect()

        # Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #set where the player starts on the screen
        self.y = 384
        self.x = 0
        # set the screen settings for the player
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        #player speed
        self.speed = .2
        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # check to see if we can move the characters if the flag is on and conditions are met
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
        # limit the speed range so it does not go negative
        if self.speed <= 0:
            self.speed = .04
        if self.speed > .3:
            self.speed = .3

    def draw(self):
        """Function to draw the player"""
        self.screen.blit(self.image, self.rect)