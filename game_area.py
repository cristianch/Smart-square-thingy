from tkinter import *
from player import *
from utils import *


class GameArea:
    canvas = None
    obstacles = []

    players = []
    no_of_players = 1
    start_pos = 480, 480
    player_size = 10
    mutation_factor = 20

    step_size = 0.01
    no_of_steps = 400

    target_position = 40, 40
    target_size = 10

    def create_canvas(self, width=500, height=500):
        master = Tk()

        canvas = Canvas(master, width=width, height=height)
        self.canvas = canvas

        self.create_players(self.start_pos[0], self.start_pos[1], self.player_size)

        self.create_target()

        self.obstacles += edge_rectangles_coords(width, height)
        for o in self.obstacles:
            self.create_obstacle(o['x'], o['y'], o['w'], o['h'])

        canvas.pack()

    def create_obstacle(self, x, y, width, height):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill='red')

    def create_target(self):
        self.canvas.create_oval(self.target_position[0], self.target_position[1],
                                self.target_position[0] + self.target_size, self.target_position[1] + self.target_size,
                                fill='yellow')

    def create_players(self, x=480, y=480, width=10):
        for i in range(self.no_of_players):
            player = Player(self.canvas.create_rectangle(x, y, x + width, y + width, fill='green'), steps=self.no_of_steps)
            self.players.append(player)

    def move_player(self, player, angle, distance):
        x_diff, y_diff = get_movement_vector(angle, distance)

        x1, y1, x2, y2 = self.canvas.coords(player.canvas_object)
        self.canvas.coords(player.canvas_object, x1 - x_diff, y1 - y_diff, x2 - x_diff, y2 - y_diff)
        self.canvas.update()

    def move_players(self, step):
        for player in self.players:
            if player.is_active:
                self.move_player(player, player.directions[step], self.step_size)
        self.check_collisions()

    def check_collisions(self):
        for player in self.players:
            for obstacle in self.obstacles:
                player_coords = self.canvas.coords(player.canvas_object)
                obstacle_coords = (
                    obstacle['x'], obstacle['y'], obstacle['x'] + obstacle['w'], obstacle['y'] + obstacle['h'])
                if collision(player_coords, obstacle_coords):
                    player.kill()
                    self.canvas.itemconfig(player.canvas_object, fill='black')

    def find_best_player(self):
        best_player = None
        best_score = 0

        for player in self.players:
            if player.is_active:
                x_player, y_player, u, u, = self.canvas.coords(player.canvas_object)
                score = 1 / distance(x_player, y_player, self.target_position[0], self.target_position[1])

                if score > best_score:
                    best_score = score
                    best_player = player

        return best_player

    def mark_best_player(self, fill='blue'):
        self.canvas.itemconfig(self.find_best_player().canvas_object, fill=fill)

    def clone_player(self, player, x, y, width, fill='green'):
        return player.clone(self.canvas.create_rectangle(x, y, x + width, y + width, fill=fill))

    def new_generation(self):
        best_player = self.find_best_player()

        if not best_player:
            return 'fail'

        self.mark_best_player()

        for player in self.players:
            if not player == best_player:
                player.kill()
                self.canvas.itemconfig(player.canvas_object, fill='black')

        self.players = [self.clone_player(best_player, self.start_pos[0], self.start_pos[1], self.player_size) for i in
                        range(self.no_of_players + 1)]

        for i in range(self.no_of_players):
            self.players[i].mutate(self.mutation_factor)
