import pygame
from pygame.sprite import Sprite

TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE

class Player2(Sprite):
    def __init__(self):
        self.image = pygame.image.load("images/player2.png")
        self.rect = self.image.get_rect()

        # Store a decimal value for the ships horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #set where the player starts on the screen
        self.y = 448
        self.x = 0

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen_rect = self.screen.get_rect()
        self.speed = .2

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
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

    def draw(self):
        self.screen.blit(self.image, self.rect)