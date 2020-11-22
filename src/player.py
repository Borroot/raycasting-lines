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
        self.rays = [None, None]

        self.update_fov_rays()
        self.init_rays()


    def init_rays(self):
        """ Create a ray for every unique endpoint from walls and add
        information to every ray about which wall(s) it intersects with. """
        for wall in self.walls:
            for endpoint in [wall.p1, wall.p2]:
                ray = Ray(self.pos, endpoint)
                if ray in (firsts := list(map(lambda x: x[0], self.rays))):
                    index = firsts.index(ray)
                    self.rays[index][1].append(wall)
                else:
                    self.rays.append((ray, [wall]))


    def update_fov_ray(self, sign):
        new = mul(atov(sign * Player.FOV + self.angle), 100)
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


    def ray_in_fov(self, ray, west, east):
        """ Determine if the given ray is in the west and east fov. """
        angle = ray.angle()
        return (east > west and (angle < west or angle > east)) or \
               (west > east and east < angle < west)


    def ray_obstructed(self, ray, walls):
        """ See if ray is cut off by any wall apart from the given ones. """
        return any(ray.collides_segments(wall) for wall in self.walls \
               if wall not in walls)


    def ray_visible(self, ray, walls, west, east):
        """ Check if the ray is completely visible from the player. """
        return self.ray_in_fov(ray, west, east) and \
               not self.ray_obstructed(ray, walls)


    def visible_rays(self):
        """ Create a list of all the visible rays in the fov. """
        west, east = self.rays[0][0].angle(), self.rays[1][0].angle()
        rays = [*self.rays[:2]]
        for ray, walls in self.rays[2:]:
            if self.ray_visible(ray, walls, west, east):
                rays.append((ray, walls))
        return rays


    def draw2d(self, surface):
        for ray, _ in self.visible_rays(): ray.draw2d(surface)
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
