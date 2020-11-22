import pygame

from line import Line
from vector import add, mul, vtoa


class Ray(Line):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)


    def angle(self):
        return vtoa(self.p1, self.p2)


    def update(self, pos):
        self.p1 = pos


    def draw2d(self, surface):
        pygame.draw.line(surface, pygame.Color('black'), self.p1, self.p2, 1)
