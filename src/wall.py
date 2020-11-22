import pygame
import random

from line import Line


def border_walls(size):
    return [Wall((0,0), (size[0],0)), Wall((size[0],0), (size[0],size[1])), \
            Wall((size[0],size[1]), (0,size[1])), Wall((0,size[1]), (0,0))]


def random_point(size):
    return random.randrange(size[0]), random.randrange(size[1])


def random_walls(size, num):
    return [Wall(random_point(size), random_point(size)) for _ in range(num)]


class Wall(Line):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)


    def draw2d(self, surface):
        pygame.draw.line(surface, pygame.Color('black'), self.p1, self.p2, 3)
