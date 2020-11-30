import math


def add(vector1, vector2):
    return tuple(sum(x) for x in zip(vector1, vector2))


def sub(vector1, vector2):
    return tuple(x - y for x, y in zip(vector1, vector2))


def prod(vector1, vector2):
    return tuple(x * y for x, y in zip(vector1, vector2))


def mul(vector, scalar):
    return tuple(x * scalar for x in vector)


def dot(vector1, vector2):  # dot product
    return sum(x * y for x, y in zip(vector1, vector2))


def dist_fast(vector1, vector2):  # euclidean without sqrt for perfomance
    return sum((x - y) ** 2 for x, y in zip(vector1, vector2))


def dist_slow(vector1, vector2):  # euclidean with sqrt
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(vector1, vector2)))


def atov(angle):  # angle to vector on unit circle
    return (math.cos(math.radians(angle)), -math.sin(math.radians(angle)))
