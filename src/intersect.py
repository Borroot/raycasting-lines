import math

from vector import sub, dot, dis


def intersect_segment2_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """Check if line ((x1,y1), (x2,y2)) intersects with line ((x3, y3), (x4,
    y4)) within just the segment of the second line. """
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0: return False
    t =  ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    if not (t >= 0 and 0 <= u <= 1): return False
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def intersect_segments_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """Check if line ((x1,y1), (x2,y2)) intersects with line ((x3, y3), (x4,
    y4)) within the segments of both lines. """
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0: return False
    t =  ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    return 0 <= t <= 1 and 0 <= u <= 1


def intersect_sameside_points(x1, y1, x2, y2, *points):
    """ Check if all points are on the same side of the line defined by two
    coordinates ((x1,y1), (x2,y2)). """
    orthogonal = (y2 - y1, -(x2 - x1))
    start = (x1, y1)
    sign = lambda x: (1, -1)[x < 0]
    signs = [sign(dot(sub((p[0], p[1]), start), orthogonal)) for p in points]
    return all(signs[0] == element for element in signs)


def intersect_segments(line, lines):
    return any(intersect_segments_points(*line.p1, *line.p2, *l.p1, *l.p2)
           for l in lines)


def intersect_sameside(line, lines):
    """ Lines collide with exactly one and the same endpoint with this line,
    see if the other endpoints are on the same side. """
    all_points = sum([[l.p1, l.p2] for l in lines[1:]], [])
    points = list({lines[0].p1, lines[0].p2}.symmetric_difference(all_points))
    return intersect_sameside_points(*line.p1, *line.p2, *points)


def intersect_closest(line, lines):
    """ Find the closest line which collides with the given line on in its
    extension, so a collision in segment 2. """
    closest_line, closest_point = None, None
    closest_dist = math.inf
    for l in lines:
        point = intersect_segment2_points(*line.p1, *line.p2, *l.p1, *l.p2)
        if point:  # there is an intersection in segment 2
            if (newdis := dis(line.p1, point)) < closest_dist:
                closest_dist = newdis
                closest_line, closest_point = l, point
    return closest_line, closest_point
