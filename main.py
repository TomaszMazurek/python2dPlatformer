import pygame
from Game import screen, canvas, screen_height, screen_width, tile_size, draw_text, font_score
import Player
from Coin import Coin, coin_group, coin_sfx
from Exit import exit_group
from Platform import platform_group
from World import World, sun_img, sky_img
from Enemy import dino_group
from Lava import lava_group
from Button import Button

import pickle
from os import path


clock = pygame.time.Clock()
fps = 60
run = True
main_menu = True
game_over = 0
level = 1
max_levels = 3
score = 0


restart_img = pygame.image.load('img/reset_btn.png')
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/close_btn.png')

if path.exists(f'levels/lvl{level}'):
    pickle_in = open(f'levels/lvl{level}', 'rb')
    world_data = pickle.load(pickle_in)

world = World(world_data, tile_size)

#function to reset level
def reset_level(level):
    player.reset(100, screen_height - 130)
    dino_group.empty()
    lava_group.empty()
    exit_group.empty()
    platform_group.empty()

    #load in level data and create world
    if path.exists(f'levels/lvl{level}'):
        pickle_in = open(f'levels/lvl{level}', 'rb')
        world_data = pickle.load(pickle_in)

    world = World(world_data, tile_size)

    return world


player = Player.Player(100, screen_height - 200)

#create buttons
restart_button = Button(screen_width // 2 - 100, screen_height // 2 - 240, pygame.transform.scale(restart_img, (200, 80)))
start_button = Button(screen_width // 2 - 100, screen_height // 2 - 240, pygame.transform.scale(start_img, (200, 80)))
exit_button = Button(screen_width // 2 - 100, screen_height // 2 - 160, pygame.transform.scale(exit_img, (200, 80)))

#create dummy coin for showing the score
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

if __name__ == '__main__':
    while run:
        clock.tick(fps)
        canvas.fill((255, 255, 255))
        canvas.blit(sky_img, (0, 0))
        canvas.blit(pygame.transform.scale(sun_img, (tile_size * 4, tile_size * 4)), (100, 100))


        if main_menu:
            screen.blit(canvas, (0, 0))
            if start_button.draw():
                main_menu = False
            if exit_button.draw():
                run = False

        else:
            world.draw()

            if game_over == 0:
                dino_group.update()
                platform_group.update()
                # update score
                # check if a coin has been collected
                if pygame.sprite.spritecollide(player, coin_group, True):
                    score += 1
                    coin_sfx.play()
                draw_text('  ' + str(score), font_score, (255, 0, 0), tile_size - 10,  5)

            dino_group.draw(canvas)
            lava_group.draw(canvas)
            exit_group.draw(canvas)
            coin_group.draw(canvas)
            platform_group.draw(canvas)

            game_over = player.update(world, game_over)

            if game_over == -1:
                if restart_button.draw():
                    player.reset(100, screen_height - 130)
                    game_over = 0
                if exit_button.draw():
                    run = False

            elif game_over == 1:
                level += 1
                if level <= max_levels:
                    world_data = []
                    game_over = 0
                else:
                    if restart_button.draw():
                        level = 1
                        world_data = []
                world = reset_level(level)
            screen.blit(canvas, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()


