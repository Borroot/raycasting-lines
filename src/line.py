import pygame
import math

from vector import dis
from intersect import *


class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.p1 == other.p1 and self.p2 == other.p2
        return NotImplemented


    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


    def __str__(self):
        return "{{{0}, {1}}}".format(self.p1, self.p2)


    def __repr__(self):
        return self.__str__()


    def collides_closest(self, lines):
        """ Find the closest line which collides with this one in its
        extension, so a collision in segment 2. """
        closest_line, closest_point = None, None
        closest_dist = math.inf
        for line in lines:
            point = intersect_segment2(*self.p1, *self.p2, *line.p1, *line.p2)
            if point:  # there is an intersection in segment 2
                if (newdis := dis(self.p1, point)) < closest_dist:
                    closest_dist = newdis
                    closest_line, closest_point = line, point
        return closest_line, closest_point


    def collides_segments(self, line):
        return intersect_segments(*self.p1, *self.p2, *line.p1, *line.p2)


    def collides_segments_list(self, lines):
        for line in lines:
            if intersect_segments(*self.p1, *self.p2, *line.p1, *line.p2):
                return True
        return False


    def draw2d(self, surface, color='black', width=5):
        pygame.draw.line(surface, pygame.Color(color), self.p1, self.p2, width)
