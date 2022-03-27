import pygame.sprite
from Spritesheet import SpriteSheet
sprite_sheet = SpriteSheet('img/Enemy/dino/sheets/DinoSprites - mort.png')


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.get_image(0, 0, 24, 24, 4)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 100:
            self.move_direction *= -1
            self.move_counter *= -1
            self.image = pygame.transform.flip(self.image, True, False)


dino_group = pygame.sprite.Group()
