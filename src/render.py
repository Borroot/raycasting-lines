import pygame
import math

from intersect import intersect_closest
from abstract import maps
from player import Player
from line import Line
from vector import dist_fast, dist_slow


def render(surface, player, walls):
    draw_background(surface)
    draw_walls(surface, player, walls)


def draw_segment(surface, line, angle):
    surf_w, surf_h = surface.get_size()
    x = int(angle * (surf_w / Player.FOV)) - Player.SCALE

    degrees = math.cos(math.radians(abs(Player.FOV / 2 - angle)))
    dist = dist_slow(line.p1, line.p2) * degrees
    height = maps(dist, 0, surf_h, surf_h / 2, 0)

    color = (int(maps(dist ** 2, 0, surf_h ** 2, 255, 0)),) * 3
    rect = pygame.Rect(x, surf_h / 2 - height, Player.SCALE + 1, int(2*height))

    pygame.draw.rect(surface, pygame.Color(*color), rect)


def draw_walls(surface, player, walls):
    for index in range(len(player.rays)):
        line, point = intersect_closest(player.rays[index], walls)
        if line is not None and point is not None:
            angle = (Player.FOV-(player.rays[index].angle-player.angle)) % 360
            draw_segment(surface, Line(player.pos, point), angle)


def draw_background(surface):
    color_floor = pygame.Color(0, 153, 51)
    color_sky = pygame.Color(0, 153, 204)
    w, h = surface.get_size()
    pygame.draw.rect(surface, color_sky,   pygame.Rect(0, 0, w, h // 2))
    pygame.draw.rect(surface, color_floor, pygame.Rect(0, h // 2, w, h))
