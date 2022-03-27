import pygame


class SpriteSheet:
    def __init__(self, file):
        self.file = file
        self.sheet = pygame.image.load(file).convert()

    def get_image(self, x, y, w, h, scale):
        sprite = pygame.Surface((w, h))
        colorkey = self.sheet.get_at((0, 0))
        sprite.set_colorkey(colorkey)
        sprite.blit(self.sheet, (0, 0), (x, y, w, h))
        return pygame.transform.scale(sprite, (w * scale, h * scale))
