import math

def E_reaction(t, x):
    a = 0.1
    theta = math.sqrt(2.0) * (0.5 - a)
    xi = x + theta * t
    z = -xi / math.sqrt(2.0)
    u = 1.0 / (1.0 + math.exp(z))
    return (-3.0 * (u ** 2.0) + 2.0 * (a + 1.0) * u - a)
