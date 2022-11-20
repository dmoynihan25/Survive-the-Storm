import pygame
from pygame.sprite import Sprite
from random import randint

TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE
fan_frequency = .005

class Fans(Sprite):
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
        #set where the player starts on the screen
        self.y = randint(0, WINDOW_HEIGHT)
        self.x = WINDOW_WIDTH






    def update(self):
        self.x -= self.speed
        #self.y += self.speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    #def draw(self):
        #self.screen.blit(self.screen, self.image, self.rect)