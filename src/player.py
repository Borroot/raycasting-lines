import pygame

from intersect import intersect_segments, intersect_closest
from line import Line
from ray import Ray
from vector import atov, add, mul


class Player:

    AMPLIFIER_MOVE = 5
    AMPLIFIER_FOV  = 5

    FOV = 60
    SCALE = 2


    def __init__(self, pos, width):
        self.pos = pos
        self.angle = 0
        self.width = width

        self.rays = [None] * (self.width // Player.SCALE)
        self.create_rays()


    def create_rays(self):
        west = add(self.pos, atov((self.angle + Player.FOV) % 360))
        east = add(self.pos, atov(self.angle))

        self.rays[ 0] = Ray(self.pos, west)
        self.rays[-1] = Ray(self.pos, east)

        stepx = (east[0] - west[0]) / len(self.rays)
        stepy = (east[1] - west[1]) / len(self.rays)

        for index in range(1, len(self.rays) - 1):
            pos = add(west, (index * stepx, index * stepy))
            self.rays[index] = Ray(self.pos, pos)


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


    def draw_cast(self, surface, walls):
        for ray in self.rays:
            line, point = intersect_closest(ray, walls)
            if line is not None and point is not None:
                pygame.draw.circle(surface, pygame.Color('black'), point, 3)
