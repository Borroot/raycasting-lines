import pygame


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


    def draw(self, surface, color='black', width=5):
        pygame.draw.line(surface, pygame.Color(color), self.p1, self.p2, width)
