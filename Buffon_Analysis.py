

import Buffon_Utilities
import sys


def main(args):

    try:
        needle_length = float(args[1])
        wood_length = float(args[2])

    except:
        print("Error, incorrect command line argument.") #catching string and any other invalid args that may come through
        return

    theoretical_probability = Buffon_Utilities.theoretical_touch_probability(needle_length, wood_length)
    print("The theoretical probability of the needle touching the edge of the wood is", 
          theoretical_probability)

    simulated_probability = Buffon_Utilities.simulated_touch_probability(needle_length, wood_length, 1000)
    print("The simulated probability of the needle touching the edge of the wood is", 
          simulated_probability)

    pi_estimate = Buffon_Utilities.pi_estimator(simulated_probability, needle_length, wood_length)
    print("The value of π based off the needle touching the edge of the wood is", 
          pi_estimate)

main(sys.argv) #fetching command line number argument
