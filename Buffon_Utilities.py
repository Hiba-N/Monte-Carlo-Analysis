import random
import math


def sample_uniform(a, b):
    return random.uniform(a, b) 


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


def simulated_touch_probability(needle_length, wood_length, total_tosses):
    """
    simulates a needle being thrown randomely n times with
    (a) random needle center 
    (b) random needle angle
    finds total times needle touches wood edge
    """
    total_touches = 0

    for _index in range(total_tosses):
        random_mid_needle_distance = sample_uniform(0, wood_length/2) #(a)
        random_needle_angle = sample_uniform(0, math.pi / 2)  #(b)
        touched = touches_line(random_mid_needle_distance, random_needle_angle, needle_length)

        if touched:
            total_touches+= 1

    return total_touches/total_tosses



def theoretical_touch_probability(needle_length, wood_length):
    """
    calculates probability using formulas on https://en.wikipedia.org/wiki/Buffon's_needle_problem#Without_integrals
    """
    if needle_length <= wood_length: #for when needle is smaller or equal to wood width
        return (2*needle_length)/(wood_length*math.pi)

    if needle_length > wood_length: #neede is longer than wood width
        return (
            (2 * needle_length) / (wood_length * math.pi)
            - (2 / (wood_length * math.pi)) * (
                math.sqrt(needle_length**2 - wood_length**2)
                + wood_length * math.asin(wood_length / needle_length)
            )
            + 1
        )


#function to calculate pi based of simulated probability
def pi_estimator(probability, needle_length, wood_length):
    return ((2*needle_length)/(wood_length*probability))