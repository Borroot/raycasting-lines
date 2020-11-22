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


    def collides_segment1(self, line):
        return intersect_segment1(*self.p1, *self.p2, *line.p1, *line.p2)


    def collides_segment2(self, line):
        return intersect_segment2(*self.p1, *self.p2, *line.p1, *line.p2)


    def collides_segments(self, line):
        return intersect_segments(*self.p1, *self.p2, *line.p1, *line.p2)


    def draw2d(self, surface):
        raise NotImplementedError
