import math
import random
from rw_header import alpha, time_step, pi

def Step():
    rand1 = 0.0
    while rand1 == 0.0:
        rand1 = random.random()
    rand2 = random.random()
    return math.sqrt(-4.0 * alpha * time_step * math.log(rand1)) * math.cos(2.0 * pi * rand2)
