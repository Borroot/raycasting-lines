import pygame

from intersect import intersect_segments
from line import Line
from ray import Ray
from vector import add, mul


class Player:

    AMPLIFIER_MOVE = 5
    AMPLIFIER_FOV  = 5

    FOV = 60
    SCALE = 2


    def __init__(self, pos, width):
        self.pos = pos
        self.angle = 0
        self.width = width

        self.rays = [0] * (self.width // Player.SCALE)
        self.create_rays()


    def create_rays(self):
        for index in range(len(self.rays) - 1, -1, -1):  # west to east
            angle = (self.angle + Player.FOV * (index / len(self.rays))) % 360
            self.rays[index] = (Ray(self.pos, angle))


    def update(self, move=None, turn=None, walls=None):
        if move is not None and walls is not None:
            newpos = add(self.pos, mul(move, Player.AMPLIFIER_MOVE))
            if not intersect_segments(Line(self.pos, newpos), walls):
                self.pos = newpos
                for ray in self.rays: ray.update(newpos)
        if turn is not None:
            self.angle = (self.angle + turn * Player.AMPLIFIER_FOV) % 360
            self.create_rays()


    def draw(self, surface):
        self.rays[ 0].draw(surface, width=2)
        self.rays[-1].draw(surface, width=2)
        pygame.draw.circle(surface, pygame.Color('black'), self.pos, 5)
