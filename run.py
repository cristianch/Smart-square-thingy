from game_area import *
from time import sleep

step_size = 1
sleep_after_step = False
step_duration = 0.001

generations = 50
mutation_factor = 45

no_of_steps = 5000
no_of_players = 10
starting_position = 450, 450
target_position = 40, 40

obstacles = [
    {'x': 200, 'y': 200, 'w': 10, 'h': 200}
]

ga = GameArea()

ga.obstacles = obstacles
ga.step_size = step_size
ga.no_of_players = no_of_players
ga.no_of_steps = no_of_steps
ga.start_pos = starting_position
ga.mutation_factor = mutation_factor

ga.create_canvas()

ga.canvas.update()

for gen in range(generations):
    for i in range(no_of_steps):
        ga.move_players(i)
        if sleep_after_step:
            sleep(step_duration)

    if ga.new_generation() == 'fail':
        print('The entire generation has failed. Better luck next time...')
        break
    ga.canvas.update()

mainloop()
