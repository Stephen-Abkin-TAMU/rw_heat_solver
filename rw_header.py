import math
import random

pi = math.pi

class Glob:
    """
    Python version of

        struct glob {
            float location, value, U, Ux, Uxx;
            struct glob *prev, *next;
        };
    """
    def __init__(self, location=0.0, value=0.0):
        self.location = float(location)
        self.value = float(value)
        self.U = 0.0
        self.Ux = 0.0
        self.Uxx = 0.0
        self.prev = None
        self.next = None

# global variables
input_file = None
output_file = None

# domain params
left_end_exists = 0
rite_end_exists = 0
left_end = 0.0
rite_end = 0.0
left_symmetric = 1
rite_symmetric = 1

# simulation params
alpha = 0.1   # diffusivity constant
time_step = 0.01    # delta t
reaction_term_exists = 0
number_of_jumps = 0
number_of_globs = 0
max_time = 0.0

# random helper to emulate drand48()
def drand48():
    return random.random()
