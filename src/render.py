import pygame
import math

from vector import distance
from raycast import rays_final


def render(surface, player, rays):
    draw_background(surface)
    draw_walls(surface, player, rays)


def maps(value, l1, r1, l2, r2, inverse=False):
    lspan, rspan = r1 - l1, r2 - l2
    value = (value - l1) / lspan
    value = l2 + (value * rspan)
    return value if not inverse else r2 - value


def draw_wall(surface, player, ray1, ray2):
    surf_w, surf_h = surface.get_size()
    step = surf_w / (2 * player.FOV)  # 1 degree = step pixels
    x1, x2 = ray1[2] * step, ray2[2] * step

    deg1 = math.cos(math.radians(abs(player.FOV - ray1[2])))
    deg2 = math.cos(math.radians(abs(player.FOV - ray2[2])))

    d1 = distance(ray1[0].p1, ray1[0].p2) * deg1
    d2 = distance(ray2[0].p1, ray2[0].p2) * deg2

    h1 = maps(d1, 0, surf_h, 0, surf_h * 0.45, True)
    h2 = maps(d2, 0, surf_h, 0, surf_h * 0.45, True)

    color = (int(maps((d1 + d2) / 2, 0, surf_h, 0, 255, True)),) * 3
    points = ((x1, surf_h/2 + h1), (x1, surf_h/2 - h1), \
              (x2, surf_h/2 - h2), (x2, surf_h/2 + h2))

    pygame.draw.polygon(surface, pygame.Color(*color), points)


def draw_walls(surface, player, rays):
    # FIXME Sometimes walls are opague or non existent.
    index = 0
    while index < len(rays) - 1:
        if any(wall in rays[index + 1][1] for wall in rays[index][1]):
            draw_wall(surface, player, rays[index], rays[index + 1])
        elif index < len(rays) - 2:
            if any(wall in rays[index + 2][1] for wall in rays[index][1]):
                draw_wall(surface, player, rays[index], rays[index + 2])
        index += 1


def draw_background(surface):
    color_floor = pygame.Color('darkgrey')
    color_sky   = pygame.Color('grey')
    w, h = surface.get_size()
    pygame.draw.rect(surface, color_sky,   pygame.Rect(0, 0, w, h // 2))
    pygame.draw.rect(surface, color_floor, pygame.Rect(0, h // 2, w, h))
