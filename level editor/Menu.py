import pygame

from Screen import canvas, world_width, tile_size

dirt_img = pygame.image.load('../img/dirt.jpg')


class Menu:
    def __init__(self):
        self.tiles = [pygame.transform.scale(dirt_img, (tile_size, tile_size))
]

    def update(self):
        canvas.blit(self.tiles[0], (world_width, 0))



