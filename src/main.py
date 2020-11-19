import pygame
import threading

from constants import *
from world import World
from player import Player


alive = True
world = World()


def init_draw():
    pygame.init()
    pygame.display.set_caption("Wolfenstein")

    surf_root = pygame.display.set_mode(SIZE_WHOLE)
    surf_west = pygame.Surface(SIZE_WEST)
    surf_east = pygame.Surface(SIZE_EAST)
    return surf_root, surf_west, surf_east


def loop_draw():
    global alive, world
    surf_root, surf_west, surf_east = init_draw()

    clock = pygame.time.Clock()
    while alive:
        clock.tick(FPS)

        surf_west.fill(pygame.Color('white'))
        surf_east.fill(pygame.Color('white'))

        world.draw(surf_west)

        surf_root.blit(surf_west, PLACE_WEST)
        surf_root.blit(surf_east, PLACE_EAST)
        pygame.display.update()

    pygame.quit()


def init_update():
    pass


def loop_update(thread_draw):
    global alive, world
    init_update()

    clock = pygame.time.Clock()
    while alive:
        clock.tick(UPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
                thread_draw.join()


def main():
    thread_draw = threading.Thread(target=loop_draw)
    thread_draw.start()
    loop_update(thread_draw)


if __name__ == '__main__':
    main()
