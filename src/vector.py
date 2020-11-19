import math


def add(vector1, vector2):
    return tuple(sum(x) for x in zip(vector1, vector2))


def mul(vector, scalar):
    return tuple(x * scalar for x in vector)


def div(vector, scalar):
    return mul(vector, 1 / scalar)


def atov(angle):   # angle to vector on unit circle
    return (math.cos(math.radians(angle)), math.sin(math.radians(angle)))


def vtoa(vector):  # vector to angle on unit circle
    unit = magset(vector, 1)
    raise NotImplementedError("Please implement this function.")


def magget(vector):
    return math.sqrt(sum(element ** 2 for element in vector))


def magset(vector, magnitude, curr=None):
    curr = curr if curr is not None else magget(vector)
    return tuple(map(lambda x: x / (curr / magnitude), vector))


def maglim(vector, magnitude):
    curr = magget(vector)
    return magset(vector, magnitude, curr) if curr > magnitude else vector
