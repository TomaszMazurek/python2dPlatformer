import os
import pathlib

import pygame
from Spritesheet import SpriteSheet

tile_size = 50
p = pathlib.Path(os.getcwd())
base_path = p.parts[0]
for i in range(1, len(p.parts)):
    base_path += '\\' + p.parts[i]
    if p.parts[i] == 'python2dPlatformer':
        break


def get_image(image_path):
    return pygame.image.load(os.path.normpath(os.path.join(base_path, 'img', image_path)))


def get_spritesheet(image_path):
    return SpriteSheet(os.path.normpath(os.path.join(base_path, 'img', image_path)))


def get_tiles(size):
    image_paths = ['dirt.jpg', 'dirt_grass.jpg', 'dirt_grass_TL.jpg', 'dirt_grass_TR.jpg',
                   'Enemy/dino/sheets/DinoSprites - mort.png', 'World/lava.jfif', 'World/exit.png', 'World/coin.png',
                   'dirt_grass.jpg', 'dirt_grass.jpg']
    ss = {4: [0, 0, 24, 24, 4], 7: [15, 30, 150, 150, 1]}
    resize = {8: (tile_size, tile_size // 2), 9: (tile_size, tile_size // 2)}
    tiles = []
    for i in range(0, len(image_paths)):
        if ss.get(i):
            sprite_sheet = get_spritesheet(image_paths[i])
            params = ss.get(i)
            sprite_tile = sprite_sheet.get_image(params[0], params[1], params[2], params[3], params[4])
            print('sprite_tile', sprite_tile)
            tiles.append(pygame.transform.scale(sprite_tile, (size, size)))
        else:
            transform_size = (size, size)
            if resize.get(i):
                transform_size = resize.get(i)
            print('transform size: ', transform_size)
            tiles.append(pygame.transform.scale(get_image(image_paths[i]), transform_size))

    return tiles
