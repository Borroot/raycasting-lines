import pygame
import random


def random_point(size):
    return random.randrange(size[0]), random.randrange(size[1])


def random_lines(size, num):
    return [Line(random_point(size), random_point(size)) for _ in range(num)]


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def draw(self, surface):
        pygame.draw.line(surface, pygame.Color('black'), self.p1, self.p2, 3)
