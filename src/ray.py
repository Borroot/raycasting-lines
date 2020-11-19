import pygame

from vector import add, mul, atov


class Ray:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def update(self, pos):
        self.p1 = pos


    def draw(self, surface):
        pygame.draw.line(surface, pygame.Color('black'), self.p1, self.p2, 1)
