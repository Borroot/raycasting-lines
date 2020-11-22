import pygame

from ray import Ray
from vector import add, mul, atov


class Player:

    AMPLIFIER_MOVE = 5
    AMPLIFIER_FOV  = 3
    FOV = 40


    def __init__(self, pos, walls):
        self.pos = pos
        self.angle = 0
        self.rays = [None, None]  # [(Ray, [Wall])]

        self.update_fov_rays()
        self.init_rays(walls)


    def init_rays(self, walls):
        """ Create a ray for every unique endpoint from walls and add
        information to every ray about which wall(s) it intersects with. """
        for wall in walls:
            for endpoint in [wall.p1, wall.p2]:
                ray = Ray(self.pos, endpoint)
                if ray in (firsts := list(map(lambda x: x[0], self.rays))):
                    index = firsts.index(ray)
                    self.rays[index][1].append(wall)
                else:
                    self.rays.append((ray, [wall]))


    def update_fov_ray(self, sign):
        new = mul(atov(sign * Player.FOV + self.angle), 30)
        return (Ray(self.pos, add(self.pos, new)), [])


    def update_fov_rays(self):
        self.rays[0] = self.update_fov_ray( 1)
        self.rays[1] = self.update_fov_ray(-1)


    def update(self, move=None, turn=None):
        if move is not None:
            self.pos = add(self.pos, mul(move, Player.AMPLIFIER_MOVE))
            self.update_fov_rays()
            for ray, _ in self.rays[2:]: ray.update(self.pos)
        if turn is not None:
            self.angle = (self.angle + turn * Player.AMPLIFIER_FOV) % 360
            self.update_fov_rays()


    def draw2d(self, surface):
        for ray, _ in self.rays[:2]: ray.draw2d(surface, width=2, dot=False)
        pygame.draw.circle(surface, pygame.Color('black'), self.pos, 5)
