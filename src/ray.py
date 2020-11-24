import pygame

from line import Line
from vector import vtoa, atov, add, mul, sub


class Ray(Line):

    AMPLIFIER_DRAW = 30


    def __init__(self, p1, p2):
        super().__init__(p1, p2)


    def angle(self):
        return vtoa(self.p1, self.p2)


    def update(self, pos):
        self.p2 = add(sub(self.p2, self.p1), pos)
        self.p1 = pos


    def draw(self, surface, color='black', width=1):
        towards = add(self.p1, mul(sub(self.p2, self.p1), Ray.AMPLIFIER_DRAW))
        pygame.draw.line(surface, pygame.Color(color), self.p1, towards, width)
