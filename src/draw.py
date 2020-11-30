import pygame

from constants import *


def draw_initialize():
    pygame.init()
    pygame.display.set_caption("Wolfenstein")

    surf_root = pygame.display.set_mode(SIZE_WHOLE)
    surf_west = pygame.Surface(SIZE_PART)
    surf_east = pygame.Surface(SIZE_PART)
    return surf_root, surf_west, surf_east


def draw_text(surface, font, color, text, pos):
    surface.blit(font.render(text, 0, pygame.Color(color)), pos)


def draw_fps(clock, surface):
    font = pygame.font.SysFont('Verdana', 15, bold=True)
    fps = str(round(clock.get_fps()))
    pos = (surface.get_size()[0] - 20, 2)
    draw_text(surface, font, 'coral', fps, pos)


def draw_background(*surfs):
    for surf in surfs:
        surf.fill(pygame.Color('white'))


def draw_world(state, surf_root, surf_west, surf_east):
    draw_background(surf_root, surf_west, surf_east)

    state['world'].draw(surf_east)
    state['world'].render(surf_west)

    surf_root.blit(surf_west, PLACE_WEST)
    surf_root.blit(surf_east, PLACE_EAST)


def draw_loop(state):
    surf_root, surf_west, surf_east = draw_initialize()
    clock = pygame.time.Clock()
    while state['alive']:
        clock.tick(FPS)
        draw_world(state, surf_root, surf_west, surf_east)
        draw_fps(clock, surf_root)
        pygame.display.update()

    pygame.quit()
