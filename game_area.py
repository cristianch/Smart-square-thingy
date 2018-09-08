from tkinter import *
from player import *
from utils import *


class GameArea:

    canvas = None
    obstacles = []
    players = []
    step_size = 0.01

    def create_canvas(self, width=500, height=500):
        master = Tk()

        canvas = Canvas(master, width=width, height=height)
        self.canvas = canvas

        self.create_players()
        for o in self.obstacles:
            self.create_obstacle(o['x'], o['y'], o['w'], o['h'])

        canvas.pack()

    def create_obstacle(self, x, y, width, height):
        self.canvas.create_rectangle(x, y, x+width, y+height, fill='red')

    def create_players(self, x=480, y=480, width=10, count=1):
        for i in range(count):
            player = Player(self.canvas.create_rectangle(x, y, x+width, y+width, fill='green'))
            self.players.append(player)

    def move_player(self, player, angle, distance=step_size):
        x_diff, y_diff = get_movement_vector(angle, distance)

        x1, y1, x2, y2 = self.canvas.coords(player.canvas_object)
        self.canvas.coords(player.canvas_object, x1-x_diff, y1-y_diff, x2-x_diff, y2-y_diff)
        self.canvas.update()

    def move_players(self):
        for player in self.players:
            self.move_player(player, 90.3)

