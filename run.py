from game_area import *

step_size = 0.01
obstacles = [
    {'x': 200, 'y': 200, 'w': 10, 'h': 100}
]

ga = GameArea()

ga.obstacles = obstacles
ga.step_size = step_size

ga.create_canvas()

ga.canvas.update()

while True:
    ga.move_players()

mainloop()
