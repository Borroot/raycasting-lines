from constants import *
from player import Player
from line import random_lines
from vector import div


class World:

    def __init__(self, lines=[]):
        self.lines = lines if lines != [] else random_lines(SIZE_PART, 5)
        self.player = Player(div(SIZE_PART, 2), self.lines)


    def update(self, move=None, turn=None):
        self.player.update(move=move, turn=turn)


    def draw(self, surface):
        self.player.draw(surface)
        for line in self.lines:
            line.draw(surface)
