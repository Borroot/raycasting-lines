import pygame


class Player:

    def __init__(self, pos):
        self.pos = pos


    def draw(self, surface):
        pygame.draw.circle(surface, pygame.Color('black'), self.pos, 5)
