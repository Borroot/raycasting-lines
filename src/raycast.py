from intersect import *
from ray import Ray


def ray_fov_angle(ray, west, east):
    """ Angle difference between the west fov ray and the given ray. """
    if west > east:
        return round(west - ray.angle(), 5)
    if east > west:
        offset = 360 - east
        return round((west + offset) - ((ray.angle() + offset) % 360), 5)


def ray_in_fov(ray, west, east):
    """ Determine if the given ray is in the west and east fov. """
    angle = ray.angle()
    return (east > west and (angle < west or angle > east)) or \
           (west > east and east < angle < west)


def ray_obstructed(ray, walls):
    """ See if ray is cut off by any wall apart from his own. """
    return any(intersect_segments(ray[0], [wall]) for wall in walls \
           if wall not in ray[1])


def ray_visible(ray, walls, west, east):
    """ Check if the ray is completely visible from the player. """
    return ray_in_fov(ray[0], west, east) and not ray_obstructed(ray, walls)


def rays_visible(rays, walls):
    """ Create a list of all the visible rays in the fov. """
    west, east = rays[0][0].angle(), rays[1][0].angle()
    return [ray for ray in rays[2:] if ray_visible(ray, walls, west, east)]


def rays_collide_fov(rays, walls):
    """ If an fov ray collides add a new ray with towards that point. """
    newrays = []
    for rayfov in rays[:2]:
        line, point = intersect_closest(rayfov[0], walls)
        if line is not None and point is not None:
            newrays.append((Ray(rayfov[0].p1, point), [line]))
    return newrays


def rays_collide_endpoint(rays, walls):
    """ Create a list of all the visible rays in the fov, plus rays which go
    through the endpoints and collide further. """
    visible = rays_visible(rays, walls)
    newrays = []
    for ray, ray_walls in visible:
        newrays.append((ray, ray_walls))
        if len(ray_walls) < 2 or intersect_sameside(ray, ray_walls):
            leftover_walls = [wall for wall in walls if wall not in ray_walls]
            line, point = intersect_closest(ray, leftover_walls)
            if line is not None and point is not None:
                newrays.append((Ray(ray.p1, point), [line]))
    return newrays


def rays_final(rays, walls):
    """ Filter out only the rays which are necessary for rendering. """
    final = rays_collide_fov(rays, walls) + rays_collide_endpoint(rays, walls)
    west, east = rays[0][0].angle(), rays[1][0].angle()
    final = [ray + (ray_fov_angle(ray[0], west, east),) for ray in final]
    final.sort(key=lambda ray: ray[2])  # sort based on angle, west -> east
    return final
