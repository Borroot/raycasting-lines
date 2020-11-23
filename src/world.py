from constants import *
from player import Player
from vector import div
from levels import *
from render import render
from raycast import rays_final
from wall import border_walls, random_walls


class World:

    def __init__(self, size):
        # self.walls = random_walls(size, 5) # + border_walls(size)
        self.walls = LEVEL1
        self.player = Player(div(size, 2), self.walls)


    def update(self, move=None, turn=None):
        self.player.update(move=move, turn=turn)


    def draw(self, surface):
        self.player.draw(surface)
        for ray, _, _ in rays_final(self.player.rays, self.walls):
            ray.draw(surface)
        for wall in self.walls:
            wall.draw(surface)


    def render(self, surface):
        render(surface, self.player, self.walls)
