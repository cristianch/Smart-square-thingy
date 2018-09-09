from game_area import *
from time import sleep


area_width = 700
area_height = 700

step_size = 4
sleep_after_step = True
step_duration = 0.001

smooth = True
smoothness_factor = 20

remove_inactive_players = True

generations = 50
mutation_factor = 70

no_of_steps = 350
no_of_players = 30
starting_position = 450, 450
target_position = 40, 40

obstacles = [
    {'x': 200, 'y': 200, 'w': 10, 'h': 200},
    {'x': 300, 'y': 300, 'w': 100, 'h': 10}
]

ga = GameArea()

ga.obstacles = obstacles
ga.step_size = step_size
ga.no_of_players = no_of_players
ga.no_of_steps = no_of_steps
ga.start_pos = starting_position
ga.mutation_factor = mutation_factor
ga.smooth = smooth
ga.smoothness_factor = smoothness_factor
ga.remove_inactive = remove_inactive_players

ga.create_canvas(area_width, area_height)

ga.canvas.update()

for gen in range(generations):
    for i in range(no_of_steps):
        ga.move_players(i)
        if sleep_after_step:
            sleep(step_duration)

    if ga.new_generation() == 'fail':
        print('The entire generation has failed. Better luck next time...')
        break
    ga.canvas.itemconfig(ga.text_area, text='Generation ' + str(gen + 1) + ' of ' + str(generations))
    ga.canvas.update()

mainloop()
