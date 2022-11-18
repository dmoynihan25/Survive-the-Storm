import pygame
from pygame.sprite import Sprite

TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

class Player1(Sprite):
    def __init__(self):
        self.image = pygame.image.load("images/player1.png")
        self.rect = self.image.get_rect()

        # Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.speed = 1

        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        # Update rect object from self.x
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)
        