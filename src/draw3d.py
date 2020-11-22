import pygame


    # Create list of rays (including the line(s!) they intersect with!).
    #  1. Add rays (if they intersect somewhere) for fov rays.
    #  2. For every other ray.
    #   2a. Add ray.
    #   2b. Add ray for closest intersection of ray and line, but further
    #       than the original endpoint intersection with the line(s).


def draw3d(surface, player, walls):
    draw3d_background(surface)


def draw3d_background(surface):
    color_floor = pygame.Color('darkgrey')
    color_sky   = pygame.Color('grey')
    w, h = surface.get_size()
    pygame.draw.rect(surface, color_sky,   pygame.Rect(0, 0, w, h // 2))
    pygame.draw.rect(surface, color_floor, pygame.Rect(0, h // 2, w, h))
