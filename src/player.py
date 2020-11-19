import pygame

from ray import Ray
from vector import add, mul, atov


class Player:

    AMPLIFIER_MOVE = 5
    AMPLIFIER_FOV  = 3
    FOV = 40


    def __init__(self, pos, lines):
        self.pos = pos
        self.angle = 0

        self.rays = [0, 0]
        self.update_fov_rays()
        for line in lines:
            self.rays.extend([Ray(pos, line.p1), Ray(pos, line.p2)])


    def update_fov_ray(self, sign):
        # return Ray(self.pos, add(self.pos, atov(sign*Player.FOV + self.angle)))
        return Ray(self.pos, add(self.pos, mul(atov(sign*Player.FOV + self.angle), 100)))


    def update_fov_rays(self):
        self.rays[0] = self.update_fov_ray( 1)
        self.rays[1] = self.update_fov_ray(-1)


    def update(self, move=None, turn=None):
        if move is not None:
            self.pos = add(self.pos, mul(move, Player.AMPLIFIER_MOVE))
            self.update_fov_rays()
            for ray in self.rays[2:]: ray.update(self.pos)
        if turn is not None:
            self.angle = (self.angle + turn * Player.AMPLIFIER_FOV) % 360
            self.update_fov_rays()


    def fov_rays(self):
        west = self.rays[0].angle()
        east = self.rays[1].angle()
        rays = []
        for ray in self.rays[2:]:
            if   west > east and east < ray.angle() < west:
                rays.append(ray)
            elif east > west and west < ray.angle() > east:
                rays.append(ray)
        return rays


    def draw(self, surface):
        # for ray in self.rays: ray.draw(surface)
        for ray in self.fov_rays(): ray.draw(surface)  # FIXME
        pygame.draw.circle(surface, pygame.Color('black'), self.pos, 5)
