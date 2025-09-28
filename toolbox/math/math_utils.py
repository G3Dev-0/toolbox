from random import random as randf
from random import randint as randi

### GENERIC MATH FUNCTIONS

def clamp(value:float, min_value:float, max_value:float) -> float:
    """
    clamps the given value between the given min and max values,
    then returnes the clamped value
    """
    return min(max_value, max(min_value, value))

def lerp(a:float, b:float, t:float):
    """
    linear interpolation function between a and b with respect to t a [0.0, 1.0] ranged value
    """
    return a + (b - a) * t

def random(a:None|float|int|bool=None, b:None|int|float=None) -> float|int|bool|None:
    """
    returns a random float in the range [0.0, 1.0] if a and b are both None

    returns a random float in the range [a, b] (including both end points)
    if a and b are both floats
    
    returns a random integer in the range [a, b] (including both end points)
    if a and b are both integers

    returns a random integer in the range [0, b) (including 0 but excluding b)
    if a is None and b is an integer

    returns a random boolean with 50 % chance of being True or False
    if a is a boolean (either True or False) and b is None

    returns a random boolean with (b * 100) % chance of being True
    if a is a boolean (either True or False) and b is a float (from 0.0 to 1.0) representing the True chance
    """
    if a == b == None:
        return randf()
    elif type(a) == type(b) == float:
        return a + randf() * (b - a)
    elif type(a) == type(b) == int:
        return randi(a, b)
    elif a == None and type(b) == int:
        return randi(0, b - 1)
    elif type(a) == bool and b == None:
        return randf() < 0.5
    elif type(a) == bool and type(b) == float:
        return randf() < b
    else:
        print("[Error]: Invalid parameters for random(a, b) function")
        return None