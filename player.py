from game_area import *
from random import uniform


class Player:
    is_active = True
    canvas_object = None
    directions = []

    def __init__(self, canvas_object, steps=400):
        self.canvas_object = canvas_object
        self.directions = [uniform(0, 360) for i in range(steps)]

    def kill(self):
        self.is_active = False

    def clone(self, canvas_object):
        new_player = Player(canvas_object)
        new_player.directions = self.directions

        return new_player

    def mutate(self, mutation_factor=15):
        mutations = [uniform(-mutation_factor, mutation_factor) for i in range(len(self.directions))]
        self.directions = [d + m for d, m in zip(self.directions, mutations)]




