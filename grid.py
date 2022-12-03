import pygame
#TILER
#set tile size
TILE_SIZE = 64
#each digit represents a tile, and the number represents the image that will loaded for that tile
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
#set variables for the different images to load as tiles
grass = pygame.image.load("images/grass.png")
yardline = pygame.image.load("images/yardline.png")
endzone = pygame.image.load("images/endzone.png")

#save vars to a list that corrolates with the numbers on the grid
ground_type = [grass, yardline, endzone]

#get rect for the tiles, all tiles are same size so I only need to do this once
tile_rect = grass.get_rect()

def draw_background(bg_size):
    """Function that draws the game"""
    bg = pygame.Surface(bg_size)
    # draw each tile onto our background
    for r, grid_list in enumerate(grid):
        for c, grid_element in enumerate(grid_list):
            # blit the correct tile onto our screen
            bg.blit(ground_type[grid_element], (c*TILE_SIZE, r*TILE_SIZE))
    #return bg so it can be called in the game
    return bg