import pygame
import threading

from constants import *
from world import World
from player import Player


alive = True
world = World(SIZE_PART)


def draw_init():
    pygame.init()
    pygame.display.set_caption("Wolfenstein")

    surf_root = pygame.display.set_mode(SIZE_WHOLE)
    surf_west = pygame.Surface(SIZE_PART)
    surf_east = pygame.Surface(SIZE_PART)
    return surf_root, surf_west, surf_east


def draw_world(world, surf_root, surf_west, surf_east):
    surf_root.fill(pygame.Color('white'))
    surf_west.fill(pygame.Color('white'))
    surf_east.fill(pygame.Color('white'))

    world.draw2d(surf_west)

    surf_root.blit(surf_west, PLACE_WEST)
    surf_root.blit(surf_east, PLACE_EAST)

    pygame.display.update()


def draw_loop():
    global alive, world
    surf_root, surf_west, surf_east = draw_init()

    clock = pygame.time.Clock()
    while alive:
        clock.tick(FPS)
        draw_world(world, surf_root, surf_west, surf_east)

    pygame.quit()


def update_init():
    pass


def update_move(world):
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        world.update(move=MOVE_NORTH)
    if pressed[pygame.K_d]:
        world.update(move=MOVE_EAST)
    if pressed[pygame.K_a]:
        world.update(move=MOVE_WEST)
    if pressed[pygame.K_s]:
        world.update(move=MOVE_SOUTH)

    if pressed[pygame.K_j]:
        world.update(turn=TURN_WEST)
    if pressed[pygame.K_k]:
        world.update(turn=TURN_EAST)


def update_loop(thread_draw):
    global alive, world
    update_init()

    clock = pygame.time.Clock()
    while alive:
        clock.tick(UPS)
        update_move(world)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    world = World(SIZE_PART)
                if event.key == pygame.K_q:
                    stop(thread_draw)

            if event.type == pygame.QUIT:
                stop(thread_draw)


def stop(thread_draw):
    global alive
    alive = False
    thread_draw.join()


def main():
    thread_draw = threading.Thread(target=draw_loop)
    thread_draw.start()
    update_loop(thread_draw)


if __name__ == '__main__':
    main()
