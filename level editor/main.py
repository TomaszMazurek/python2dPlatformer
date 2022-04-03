import pygame
from Grid import Grid
from Menu import Menu

run = True
clock = pygame.time.Clock()
fps = 60

world_grid = Grid()
tile_menu = Menu()

if __name__ == '__main__':
    while run:
        clock.tick(fps)

        tile_menu.update()
        world_grid.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
