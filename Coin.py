import pygame
import pygame.sprite
from Spritesheet import SpriteSheet

sprite_sheet = SpriteSheet('img/World/coin.png')

from Game import tile_size


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = sprite_sheet.get_image(15, 30, 150, 150, 1)
        self.image = pygame.transform.scale(img, (tile_size // 1.25, tile_size // 1.25))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


coin_group = pygame.sprite.Group()
coin_sfx = pygame.mixer.Sound('sfx/coin.wav')
coin_sfx.set_volume(0.5)
