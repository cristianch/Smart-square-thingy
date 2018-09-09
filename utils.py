from math import sin, cos, radians, sqrt


def get_movement_vector(angle, distance):
    x_diff = distance * sin(radians(angle))
    y_diff = distance * cos(radians(angle))
    return x_diff, y_diff


# True if two rectangles are colliding; takes their coord tuples as params
def collision(coords1, coords2):
    c1 = {'x_top_left': coords1[0], 'y_top_left': coords1[1], 'x_bot_right': coords1[2], 'y_bot_right': coords1[3]}
    c2 = {'x_top_left': coords2[0], 'y_top_left': coords2[1], 'x_bot_right': coords2[2], 'y_bot_right': coords2[3]}

    if c1['x_top_left'] > c2['x_bot_right'] or c1['x_bot_right'] < c2['x_top_left']:
        return False

    if c1['y_top_left'] > c2['y_bot_right'] or c1['y_bot_right'] < c2['y_top_left']:
        return False

    return True


# For an area of given width and height, generate coords for the edges of the area
# We need this to create obstacles on the edges so players can't leave the game area
def edge_rectangles_coords(width, height):
    top = {'x': 0, 'y': 0, 'w': width, 'h': 1}
    bottom = {'x': 0, 'y': height+2, 'w': width, 'h': 1}
    left = {'x': 0, 'y': 0, 'w': 1, 'h': height}
    right = {'x': width+2, 'y': 0, 'w': 1, 'h': height}

    return [top, bottom, left, right]


def distance(x1, y1, x2, y2):
    return sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
