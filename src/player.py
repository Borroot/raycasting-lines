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

        self.walls = walls
        self.rays = [0, 0]
        self.update_fov_rays()
        for wall in walls:
            self.rays.extend([Ray(pos, wall.p1), Ray(pos, wall.p2)])

        # TODO Remove all the duplicate rays.
        # TODO Add a list to every ray showing with which line(s) they collide.


    def update_fov_ray(self, sign):
        new = mul(atov(sign * Player.FOV + self.angle), 100)
        return Ray(self.pos, add(self.pos, new))


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


    def visible_rays(self):  # in fov and not obstructed
        west = self.rays[0].angle()
        east = self.rays[1].angle()
        rays = [*self.rays[:2]]
        for ray in self.rays[2:]:
            if (west > east and east < ray.angle() < west) or \
               (east > west and (ray.angle() < west or ray.angle() > east)):
                rays.append(ray)
        # TODO Filter out rays which are obstructed.
        return rays


    def draw2d(self, surface):
        for ray in self.visible_rays(): ray.draw2d(surface)
        pygame.draw.circle(surface, pygame.Color('black'), self.pos, 5)


    def draw3d(self, surface):
        # Create list of rays (including the line(s!) they intersect with!).
        #  1. Add rays (if they intersect somewhere) for fov rays.
        #  2. For every other ray.
        #   2a. Add ray.
        #   2b. Add ray for closest intersection of ray and line, but further
        #       than the original endpoint intersection with the line(s).
        #  3.
        pass
