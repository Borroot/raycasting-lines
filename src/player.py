import pygame

from intersect import intersect_segments, intersect_closest
from line import Line
from ray import Ray
from constants import *
from vector import add, mul, atov


class Player:

    AMPLIFIER_MOVE = 2
    AMPLIFIER_FOV  = 4

    FOV = 60
    SCALE = 5


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


    def move(self, move, walls):
        angle_offset = 0
        if move == MOVE_EAST or move == MOVE_WEST:
            angle_offset = 90 if move == MOVE_WEST else -90
        elif move == MOVE_SOUTH:
            angle_offset = -180

        move_vector = atov(self.angle + 30 + angle_offset)
        newpos = add(self.pos, mul(move_vector, Player.AMPLIFIER_MOVE))
        if not intersect_segments(Line(self.pos, newpos), walls):
            self.pos = newpos
            for ray in self.rays: ray.update(newpos)


    def update(self, move=None, turn=None, walls=None):
        if move is not None and walls is not None:
            self.move(move, walls)
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
            if line is not None:
                pygame.draw.circle(surface, pygame.Color('black'), point, 3)
