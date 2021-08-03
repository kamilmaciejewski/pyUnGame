import math


def calculate_distance(a: tuple, b: tuple):
    dist = math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    return dist
