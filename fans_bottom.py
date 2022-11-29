import pygame
from pygame.sprite import Sprite
from random import randint
import math

TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE
fan_frequency = .005

class FansBottom(Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/fan1.png")
        self.rect = self.image.get_rect()

        self.speed = .2

        # Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.theta = randint(255, 285)
        #set where the player starts on the screen
        self.y = 512
        self.x = randint(0, WINDOW_WIDTH)


    def get_radians(self):
        return self.theta * math.pi / 180


    def update(self):
        self.x += self.speed * math.cos(self.get_radians())
        self.y += self.speed * math.sin(self.get_radians())

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y