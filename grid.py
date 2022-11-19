import pygame

TILE_SIZE = 64
grid = [
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2 ],
]

grass = pygame.image.load("images/grass.png")
yardline = pygame.image.load("images/yardline.png")
endzone = pygame.image.load("images/endzone.png")

ground_type = [grass, yardline, endzone]

tile_rect = grass.get_rect()

def draw_background(bg_size):
    bg = pygame.Surface(bg_size)
    # draw each tile onto our background
    for r, grid_list in enumerate(grid):
        for c, grid_element in enumerate(grid_list):
            # blit the correct tile onto our screen
            bg.blit(ground_type[grid_element], (c*TILE_SIZE, r*TILE_SIZE))
    return bg