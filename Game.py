import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

screen_width = 1600
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
canvas = pygame.Surface((screen_width, screen_height))
tile_size = 50

#define font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 50)

#define colours
white = (255, 255, 255)
blue = (0, 0, 255)

#load sounds
pygame.mixer.music.load('sfx/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)


def draw_text(text, _font, text_col, x, y):
    img = _font.render(text, True, text_col)
    canvas.blit(img, (x, y))
