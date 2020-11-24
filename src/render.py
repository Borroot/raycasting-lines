import pygame
import math

from vector import dis, distance
from raycast import rays_final


def render(surface, player, rays):
    draw_background(surface)
    draw_walls(surface, player, rays)


def maps(value, l1, r1, l2, r2, inverse=False):
    lspan, rspan = r1 - l1, r2 - l2
    value = (value - l1) / lspan
    value = value * rspan
    return l2 + value if not inverse else r2 - value


def draw_wall(surface, player, ray1, ray2):
    surf_w, surf_h = surface.get_size()
    step = surf_w / (2 * player.FOV)
    x1, x2 = int(ray1[2] * step), int(ray2[2] * step)

    deg1 = math.cos(math.radians(abs(player.FOV - ray1[2])))
    deg2 = math.cos(math.radians(abs(player.FOV - ray2[2])))

    d1 = int(distance(ray1[0].p1, ray1[0].p2) * deg1)
    d2 = int(distance(ray2[0].p1, ray2[0].p2) * deg2)

    for x in range(x1, x2):
        r1x, r1y, r2x, r2y = *ray1[0].p2, *ray2[0].p2
        newx = maps(x, x1, x2, min(r1x, r2x), max(r1x, r2x), r1x > r2x)
        newy = maps(x, x1, x2, min(r1y, r2y), max(r1y, r2y), r1y > r2y)
        degr = maps(x, x1, x2, deg1, deg2)
        dist = int(distance(ray1[0].p1, (newx, newy)) * degr)

        # dist = maps(x, x1, x2, min(d1, d2), max(d1, d2), d1 > d2)

        height = maps(dist, 0, surf_h, 0, surf_h / 2, True)
        color = (int(maps(dist, 0, surf_h, 0, 255, True)),) * 3
        line = ((x, surf_h / 2 + height), (x, surf_h / 2 - height))
        pygame.draw.line(surface, pygame.Color(*color), *line)


def draw_walls(surface, player, rays):
    index = 0
    while index < len(rays) - 1:
        # FIXME Opague walls.
        if any(wall in rays[index + 1][1] for wall in rays[index][1]):
            draw_wall(surface, player, rays[index], rays[index + 1])
        elif index < len(rays) - 2:
            if any(wall in rays[index + 2][1] for wall in rays[index][1]):
                draw_wall(surface, player, rays[index], rays[index + 2])
        index += 1


def draw_background(surface):
    color_floor = pygame.Color(0, 153, 51)
    color_sky   = pygame.Color(0, 153, 204)
    w, h = surface.get_size()
    pygame.draw.rect(surface, color_sky,   pygame.Rect(0, 0, w, h // 2))
    pygame.draw.rect(surface, color_floor, pygame.Rect(0, h // 2, w, h))
