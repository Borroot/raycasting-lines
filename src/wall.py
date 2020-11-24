import pygame
import random

from line import Line


class Wall(Line):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)


    def draw(self, surface):
        super().draw(surface, width=3)
