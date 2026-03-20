# 1) Create a file named Buffon_Utilities.py containing the following functions.

# 1a) Write a function which takes two arguments, a
#  and b
# , randomly samples from the uniform distribution between a
#  and b
# , and returns the sampled value.

import random

def sample_uniform(a, b):
    return random.uniform(a, b)



# 1b) Write a function which, given x
#  and θ
#  and ℓ
#  (the length of the needle), returns a boolean indicating whether or not the needle is touching the edge of the board.

# 1c) Write a function which, given ℓ
# , t
# , and n
# , simulates the tossing of a needle n
#  times. It should return the number of times, out of n
# , that the needle touches the edge of the board.

# 1d) Write a function which takes ℓ
#  and t
#  as arguments. Using the formulae given in the link above, the function should return the theoretical probability of a single needle toss touching a board edge.

# 1e) Write a function which takes a probability, ℓ
#  and t
#  as arguments. The function should return an estimate for the value of π
# . This will require rearranging the equation used in part 1d) above. Be sure to not copy-and-paste code!