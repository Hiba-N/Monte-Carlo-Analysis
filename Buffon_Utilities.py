# 1) Create a file named Buffon_Utilities.py containing the following functions.

# 1a) Write a function which takes two arguments, a
#  and b
# , randomly samples from the uniform distribution between a
#  and b
# , and returns the sampled value.

import random
import math

#function to sample from a normal distribution given the range a - b
def sample_uniform(a, b):
    return random.uniform(a, b) 



# 1b) Write a function which, given x
#  and θ
#  and ℓ
#  (the length of the needle), returns a boolean indicating whether or not the needle is touching the edge of the board.


#function to check if needle touches line
def touches_line(mid_needle_distance, needle_angle, needle_length): 
    """
    using sin here we find the width that the titled needle covers.
    for example, if it is completely parallel to the wood, the angle is 0, sin(00) is 0, and width is 0
    if the needle is completely perpendicular to the wood, angle is 90, sin(90) is 1, and width = half needle length
    if width is less that half needle length it does not touch wood, ie false
    if width is equal or more than half needle length, it touched wood line ie true
    """

    if mid_needle_distance > ((needle_length / 2) * math.sin(needle_angle)): 
        return False
    else:
        return True



# 1c) Write a function which, given ℓ (length of needle)
# , t (length of wood)
# , and n
# , simulates the tossing of a needle n
#  times. It should return the number of times, out of n
# , that the needle touches the edge of the board.

def needle_simulator(needle_length, wood_length, total_tosses):
    """
    simulates a needle being thrown randomely n times with
    (a) random needle center 
    (b) random needle angle
    finds total times needle touches wood edge
    """
    total_touches = 0

    for _index in range(total_tosses):
        random_mid_needle_distance = sample_uniform(0, wood_length/2) #(a)
        random_needle_angle = sample_uniform(0, 90)  #(b)
        touched = touches_line(random_mid_needle_distance, random_needle_angle, needle_length)

        if touched:
            total_touches+= 1

    return total_touches





# 1d) Write a function which takes ℓ
#  and t
#  as arguments. Using the formulae given in the link above, the function should return the theoretical probability of a single needle toss touching a board edge.

# 1e) Write a function which takes a probability, ℓ
#  and t
#  as arguments. The function should return an estimate for the value of π
# . This will require rearranging the equation used in part 1d) above. Be sure to not copy-and-paste code!