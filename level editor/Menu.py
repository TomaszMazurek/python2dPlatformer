from Screen import canvas, world_width, tile_size
from img.utils import get_tiles


class Menu:
    def __init__(self):
        self.tiles = get_tiles(tile_size - 6)

    def update(self):
        for i in range(0, len(self.tiles)):
            canvas.blit(self.tiles[i], (world_width, (tile_size * i + 3)))
