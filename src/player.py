import pygame

from ray import Ray
from vector import add, mul


class Player:

    MOVE_AMPLIFIER = 5
    FOV = 40


    def __init__(self, pos, lines):
        self.pos = pos
        self.angle = 0

        self.rays = []
        for line in lines:
            self.rays.extend([Ray(pos, line.p1), Ray(pos, line.p2)])


    def update(self, move=None, turn=None):
        if move is not None:
            self.pos = add(self.pos, mul(move, Player.MOVE_AMPLIFIER))
            for ray in self.rays: ray.update(self.pos)
        if turn is not None:
            self.angle += turn


    def draw(self, surface):
        for ray in self.rays: ray.draw(surface)
        pygame.draw.circle(surface, pygame.Color('black'), self.pos, 5)
