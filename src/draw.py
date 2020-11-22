import pygame

from constants import *


def draw_initialize():
    pygame.init()
    pygame.display.set_caption("Wolfenstein")

    surf_root = pygame.display.set_mode(SIZE_WHOLE)
    surf_west = pygame.Surface(SIZE_PART)
    surf_east = pygame.Surface(SIZE_PART)
    return surf_root, surf_west, surf_east


def draw_background(*surfs):
    for surf in surfs:
        surf.fill(pygame.Color('white'))


def draw_world(state, surf_root, surf_west, surf_east):
    draw_background(surf_root, surf_west, surf_east)

    state['world'].draw2d(surf_west)
    state['world'].draw3d(surf_east)

    surf_root.blit(surf_west, PLACE_WEST)
    surf_root.blit(surf_east, PLACE_EAST)

    pygame.display.update()


def draw_loop(state):
    surf_root, surf_west, surf_east = draw_initialize()
    clock = pygame.time.Clock()
    while state['alive']:
        clock.tick(FPS)
        draw_world(state, surf_root, surf_west, surf_east)
    pygame.quit()
