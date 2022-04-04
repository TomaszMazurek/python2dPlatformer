import math
import pygame
from Screen import screen, canvas, tile_size, screen_height, world_width
from File import File
from img.utils import get_tiles, resize

sun_img = pygame.image.load('../img/sun.png')
sky_img = pygame.image.load('../img/sky.png')
dirt_img = pygame.image.load('../img/dirt.jpg')


class Grid:
    def __init__(self):
        self.image = sky_img
        self.rect = self.image.get_rect()
        self.clicked = False
        self.world = self.create_world()
        self.world_tile_list = self.create_world()
        self.tile_list = get_tiles(tile_size)
        self.action = False
        self.selected_tile = 0

        self.set_background()

    def set_background(self):
        canvas.fill((255, 255, 255))
        canvas.blit(self.image, (0, 0))
        canvas.blit(pygame.transform.scale(sun_img, (tile_size * 4, tile_size * 4)), (100, 100))

    def draw_grid(self):
        grid_range = int(world_width/tile_size)
        for line in range(0, grid_range):
            pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (world_width, line * tile_size))
            pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


    def create_world(self):
        world = []
        world_w = int(world_width/tile_size)
        world_h = int(screen_height/tile_size)
        for line in range(0, world_h):
            lst = [0] * world_w
            world.append(lst)

        return world


    def update_world_tile_list(self):
        world_tile_list = self.create_world()
        for line in range(0, len(world_tile_list)):
            for tile in range(0, len(world_tile_list[line])):
                tile_id = self.world[line][tile]
                if tile_id > 0:
                        img = self.tile_list[tile_id - 1]
                        img_rect = img.get_rect()
                        img_rect.x = tile * tile_size
                        img_rect.y = line * tile_size
                        if resize.get(tile_id - 1):
                            img_rect.y = img_rect.y + (tile_size // 2)
                        new_tile = (img, img_rect)
                        world_tile_list[line][tile] = new_tile

        self.world_tile_list = world_tile_list
        self.set_background()


    def update(self):
        if pygame.mouse.get_pressed()[0] and not self.action:
            pos = pygame.mouse.get_pos()
            x = math.floor(pos[0] / tile_size)
            y = math.floor(pos[1] / tile_size)
            if self.rect.collidepoint(pos):
                self.world[y][x] = self.selected_tile + 1
                img = self.tile_list[self.selected_tile]
                img_rect = img.get_rect()
                img_rect.x = x * tile_size
                img_rect.y = y * tile_size
                if resize.get(self.selected_tile):
                    img_rect.y = img_rect.y + (tile_size // 2)
                tile = (img, img_rect)
                self.world_tile_list[y][x] = tile
            else:
                if pos[1] > (screen_height - tile_size):
                    File.save_file(self.world)
                elif pos[1] > (screen_height - tile_size * 2):
                    self.world = File.load_file()
                    self.update_world_tile_list()
                else:
                    self.selected_tile = y
            self.action = True
        elif pygame.mouse.get_pressed()[2] and not self.action:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                x = math.floor(pos[0] / tile_size)
                y = math.floor(pos[1] / tile_size)
                self.world[y][x] = 0
                self.world_tile_list[y][x] = None
                self.action = True
                self.set_background()
        elif not pygame.mouse.get_pressed()[0] and not pygame.mouse.get_pressed()[2]:
            self.action = False

        for row in self.world_tile_list:
            for column in row:
                if column:
                    canvas.blit(column[0], column[1])

        screen.blit(canvas, (0, 0))
        self.draw_grid()
