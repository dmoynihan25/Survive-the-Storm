import pygame
from pygame.sprite import Sprite

TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

class Drink(Sprite):
    def __init__(self):

        self.image = pygame.image.load("images/drink.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)
        self.rect = self.image.get_rect()


        # Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #set where the player starts on the screen
        self.y = (WINDOW_HEIGHT / 2) - (self.rect.height / 2)
        self.x = (WINDOW_WIDTH / 2) - (self.rect.width / 2)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen_rect = self.screen.get_rect()

    def update(self):
        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)