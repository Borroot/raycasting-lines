from constants import *
from player import Player
from vector import mul
from levels import *
from render import render


class World:

    def __init__(self, size):
        self.walls = LEVEL1
        self.player = Player(mul(size, 0.5), size[0])


    def update(self, move=None, turn=None):
        walls = self.walls if move is not None else None
        self.player.update(move=move, turn=turn, walls=walls)


    def draw(self, surface):
        self.player.draw(surface)
        for wall in self.walls:
            wall.draw(surface)

        from intersect import intersect_closest
        import pygame
        for index in range(len(self.player.rays)):
            line, point = intersect_closest(self.player.rays[index], self.walls)
            if line is not None:
                pygame.draw.circle(surface, pygame.Color('black'), point, 5)


    def render(self, surface):
        render(surface, self.player, self.walls)
