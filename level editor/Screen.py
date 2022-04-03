import pygame
pygame.init()

tile_size = 50
menu_width = tile_size
world_width = 1600
screen_width = world_width + menu_width
screen_height = 850

screen = pygame.display.set_mode((screen_width, screen_height))
canvas = pygame.Surface((screen_width, screen_height))

