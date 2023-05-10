import random

# assume available_directions is an array of 4 booleans
# indicating which directions are available

available_directions = [True, True, False, True]

# create a list of available directions
options = [i for i in range(4) if available_directions[i]]

# choose a random direction from the available options
print(options)


