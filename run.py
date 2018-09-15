from game_area import *
from time import sleep

# Size of the window and game area
area_width = 800
area_height = 600

step_size = 6  # How far the squares go in one step
sleep_after_step = True  # Set to true to add a small time interval between steps
step_duration = 0.001  # Only applicable if 'sleep_after_step' is set to true

smooth = True  # If true then angle difference between two consecutive steps will be limited for 1st generation
smoothness_factor = 30  # Limit for angle difference between two consecutive steps, if 'smooth' is true

remove_inactive_players = True  # Remove inactive squares after each generation (recommended)

generations = 100

# Maximum mutation i.e. angle difference between s[i] and p[i] for s[i] = step i of current square
# and p[i] step i of current square's parent
mutation_factor = 50

no_of_steps = 200
no_of_players = 35  # Number of players per generation
starting_position = 450, 450  # All new players spawn here
target_position = 40, 40

# Obstacles should be set in the format
# {'x': top-left-corner-x, 'y': top-left-corner-y, 'w': width, 'h': height}
obstacles = [
    {'x': 200, 'y': 200, 'w': 10, 'h': 200},
    {'x': 300, 'y': 300, 'w': 100, 'h': 10},
    {'x': 500, 'y': 400, 'w': 10, 'h': 150}
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

    # Print generation number to the top left of the window
    ga.canvas.itemconfig(ga.text_area, text='Generation ' + str(gen + 1) + ' of ' + str(generations))
    ga.canvas.update()

mainloop()
