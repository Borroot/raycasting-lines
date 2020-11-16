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

    surf_root  = pygame.display.set_mode(SIZE_WHOLE)
    surf_left  = pygame.Surface(SIZE_LEFT)
    surf_right = pygame.Surface(SIZE_RIGHT)
    return surf_root, surf_left, surf_right


def loop_draw():
    global alive, world
    surf_root, surf_left, surf_right = init_draw()

    clock = pygame.time.Clock()
    while alive:
        clock.tick(FPS)

        surf_left.fill(pygame.Color('white'))
        surf_right.fill(pygame.Color('white'))

        world.draw(surf_left)

        surf_root.blit(surf_left,  (  0, 0))
        surf_root.blit(surf_right, (800, 0))
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
