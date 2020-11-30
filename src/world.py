from constants import *
from player import Player
from vector import mul
from level import *
from render import render


class World:

    def __init__(self, size):
        self.walls = LEVEL1 + LEVEL2
        self.player = Player(mul(size, 0.4), size[0])


    def update(self, move=None, turn=None):
        walls = self.walls if move is not None else None
        self.player.update(move=move, turn=turn, walls=walls)


    def draw(self, surface):
        self.player.draw_cast(surface, self.walls)
        self.player.draw(surface)
        for wall in self.walls:
            wall.draw(surface)


    def render(self, surface):
        render(surface, self.player, self.walls)
