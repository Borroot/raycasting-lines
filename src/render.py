import pygame

from raycast import rays_final


def render(surface, player, walls):
    draw_background(surface)
    rays = rays_final(player.rays, walls)
    # TODO Use the rays_final() function to draw a 3d image.


def draw_background(surface):
    color_floor = pygame.Color('darkgrey')
    color_sky   = pygame.Color('grey')
    w, h = surface.get_size()
    pygame.draw.rect(surface, color_sky,   pygame.Rect(0, 0, w, h // 2))
    pygame.draw.rect(surface, color_floor, pygame.Rect(0, h // 2, w, h))
