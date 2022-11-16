import pygame
from pygame.sprite import Sprite

class Player1(Sprite):
    def __init__(self, screen):
        self.image = pygame.image.load("images/player1.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.screen = screen
        