import math

import pygame
from Screen import screen, canvas, tile_size, screen_height, world_width

sun_img = pygame.image.load('../img/sun.png')
sky_img = pygame.image.load('../img/sky.png')
dirt_img = pygame.image.load('../img/dirt.jpg')


class Grid:
    def __init__(self):
        self.image = sky_img
        self.rect = self.image.get_rect()
        self.clicked = False
        self.world = self.create_world()
        self.tile_list = self.create_world()
        self.action = False

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
        world_h = int(world_width/tile_size)
        for line in range(0, world_w):
            lst = [0] * world_h
            world.append(lst)

        return world

    def update(self):
        if pygame.mouse.get_pressed()[0] and not self.action:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                y = math.floor(pos[1] / tile_size)
                x = math.floor(pos[0] / tile_size)
                self.world[x][y] = 1
                img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                img_rect = img.get_rect()
                img_rect.x = x * tile_size
                img_rect.y = y * tile_size
                tile = (img, img_rect)
                self.tile_list[x][y] = tile
                self.action = True
            else:
                print('Out of grid: ', pos)
        elif pygame.mouse.get_pressed()[2] and not self.action:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                y = math.floor(pos[1] / tile_size)
                x = math.floor(pos[0] / tile_size)
                self.world[x][y] = 0
                self.tile_list[x][y] = None
                self.action = True
                self.set_background()
        elif not pygame.mouse.get_pressed()[0] and not pygame.mouse.get_pressed()[2]:
            self.action = False

        for row in self.tile_list:
            for column in row:
                if column:
                    canvas.blit(column[0], column[1])

        screen.blit(canvas, (0, 0))
        self.draw_grid()
