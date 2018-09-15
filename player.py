from game_area import *
from utils import *
from random import uniform
from itertools import starmap


class Player:
    is_active = True
    canvas_object = None
    directions = []

    def __init__(self, canvas_object, steps=400, smooth=False, smoothness_factor=20):
        self.canvas_object = canvas_object
        if smooth:
            self.directions = random_angle_array_smooth(steps, smoothness_factor)
        else:
            self.directions = random_angle_array(steps)

    def kill(self):
        self.is_active = False

    def clone(self, canvas_object):
        new_player = Player(canvas_object)
        new_player.directions = self.directions

        return new_player

    def mutate(self, mutation_factor=15):
        # Mutate each step by a random angle, no more than the mutation factor
        mutations = [uniform(-mutation_factor, mutation_factor) for i in self.directions]
        self.directions = [d + m for d, m in zip(self.directions, mutations)]




