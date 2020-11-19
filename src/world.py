from constants import *
from player import Player
from vector import div
from line import border_lines, random_lines


class World:

    def __init__(self, size):
        self.lines = border_lines(size) + random_lines(size, 5)
        self.player = Player(div(size, 2), self.lines)


    def update(self, move=None, turn=None):
        self.player.update(move=move, turn=turn)


    def draw(self, surface):
        self.player.draw(surface)
        for line in self.lines:
            line.draw(surface)
