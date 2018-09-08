from game_area import *


class Player:
    active = True
    canvas_object = None

    def __init__(self, canvas_object):
        self.canvas_object = canvas_object

    def kill(self):
        self.active = False




