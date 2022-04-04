import math

import pygame

from Screen import canvas, world_width, tile_size, screen_height
from img.utils import get_tiles, get_image


class Menu:
    def __init__(self):
        self.tiles = get_tiles(tile_size - 6)

    def update(self):
        for i in range(0, len(self.tiles)):
            canvas.blit(self.tiles[i], (world_width, (tile_size * i + 3)))

        save_btn = pygame.transform.scale(get_image('save.png'), (tile_size, tile_size))
        canvas.blit(save_btn, (world_width, screen_height - tile_size))

        save_btn = pygame.transform.scale(get_image('load.png'), (tile_size, tile_size))
        canvas.blit(save_btn, (world_width, screen_height - tile_size * 2))
