import pygame
import math

from vector import distance
from raycast import rays_final


def render(surface, player, rays):
    draw_background(surface)
    draw_walls(surface, player, rays)  # FIXME The incorrect order of the walls breaks stuff.


def maps(value, l1, r1, l2, r2, inverse=False):
    lspan, rspan = r1 - l1, r2 - l2
    value = (value - l1) / lspan
    value = l2 + (value * rspan)
    return value if not inverse else r2 - value


def draw_wall(surface, player, ray1, ray2):
    surf_w, surf_h = surface.get_size()
    step = surf_w / (2 * player.FOV)  # 1 degree = step pixels
    x1, x2 = ray1[2] * step, ray2[2] * step

    perpdis1 = distance(ray1[0].p1, ray1[0].p2)
    perpdis2 = distance(ray2[0].p1, ray2[0].p2)

    h1 = maps(perpdis1, 0, surf_h , 0, surf_h / 2, True)
    h2 = maps(perpdis2, 0, surf_h , 0, surf_h / 2, True)
    color = (int(maps((perpdis1 + perpdis2) / 2, 0, surf_h, 0, 255, True)),) * 3

    points = ((x1, surf_h/2 + h1), (x1, surf_h/2 - h1), \
              (x2, surf_h/2 - h2), (x2, surf_h/2 + h2))

    pygame.draw.polygon(surface, pygame.Color(*color), points)


def next_wall(index, rays):
    """ Check the next few rays with the exact same angle if there is one with
    a wall in common with the current ray. """
    next_index = index + 1
    next_angle = rays[next_index][2]
    while next_index < len(rays) and next_angle == rays[next_index][2]:
        if any(wall in rays[next_index][1] for wall in rays[index][1]):
            return next_index
        next_index += 1
    return False


def draw_walls(surface, player, rays):
    index = 0
    while index < len(rays) - 1:
        if (next_index := next_wall(index, rays)):
            draw_wall(surface, player, rays[index], rays[next_index])
        index += 1


def draw_background(surface):
    color_floor = pygame.Color('darkgrey')
    color_sky   = pygame.Color('grey')
    w, h = surface.get_size()
    pygame.draw.rect(surface, color_sky,   pygame.Rect(0, 0, w, h // 2))
    pygame.draw.rect(surface, color_floor, pygame.Rect(0, h // 2, w, h))
