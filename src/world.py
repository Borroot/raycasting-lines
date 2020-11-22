from constants import *
from player import Player
from vector import div
from wall import border_walls, random_walls


class World:

    def __init__(self, size):
        self.walls = random_walls(size, 5) # + border_walls(size)
        self.player = Player(div(size, 2), self.walls)


    def update(self, move=None, turn=None):
        self.player.update(move=move, turn=turn)


    def draw2d(self, surface):
        self.player.draw2d(surface)
        for wall in self.walls:
            wall.draw2d(surface)


    def draw3d(self, surface):
        self.player.draw3d(surface)
