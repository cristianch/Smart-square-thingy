from math import sin, cos, radians


def get_movement_vector(angle, distance):
    x_diff = distance * sin(radians(angle))
    y_diff = distance * cos(radians(angle))
    return x_diff, y_diff
