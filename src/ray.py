import pygame

from line import Line
from vector import vtoa


class Ray(Line):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)


    def angle(self):
        return vtoa(self.p1, self.p2)


    def update(self, pos):
        self.p1 = pos


    def draw(self, surface, color='black', width=1, dot=True):
        super().draw(surface, color=color, width=width)
        if dot: pygame.draw.circle(surface, pygame.Color('black'), self.p2, 4)
