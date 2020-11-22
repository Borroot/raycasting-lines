def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    return denominator if denominator != 0 else False


def intersect_t(x1, y1, x2, y2, x3, y3, x4, y4):
    if (den := intersect(x1, y1, x2, y2, x3, y3, x4, y4)):
        return ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return False


def intersect_u(x1, y1, x2, y2, x3, y3, x4, y4):
    if (den := intersect(x1, y1, x2, y2, x3, y3, x4, y4)):
        return -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    return False


def intersect_segment1(*args):
    if (t := intersect_t(*args)):
        return 0 <= t <= 1
    return False


def intersect_segment2(*args):
    if (u := intersect_u(*args)):
        return 0 <= u <= 1
    return False


def intersect_segments(x1, y1, x2, y2, x3, y3, x4, y4):
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0: return False
    t =  ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    return 0 <= t <= 1 and 0 <= u <= 1


def intersect_point(x1, y1, x2, y2, x3, y3, x4, y4):
    if (t := intersect_t(x1, y1, x2, y2, x3, y3, x4, y4)):
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return False
