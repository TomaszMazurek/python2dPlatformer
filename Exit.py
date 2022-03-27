import pygame
from Game import tile_size


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/World/exit.png')
        img_left = pygame.transform.flip(img, True, False)
        self.image = pygame.transform.scale(img_left, (tile_size, int(tile_size * 1.7)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


exit_group = pygame.sprite.Group()