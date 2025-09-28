# Toolbox
Toolbox is a Python and pygame based library to easily access to the math and canvas rendering needed for creative coding.
It can be used for making fast sketches and visual representations.

## How to use it
To use it simply duplicate the [`template.py`](template.py) file and write your code in the `init`, `tick` and `draw` functions.
The `init` function is runned once at the program start, `tick` and `draw` are called 60 times per second (you can also change the tick rate and frame rate indipendently to make rendering laster/slower and to make simulations where time is sped up or slowed down.

## Modules
There are several modules which give you easy to access functions for rendering and doing math, the most important ones are:
+ **canvas** (`from toolbox.canvas import *`): has all the functions for creating and customizing a canvas and for running the program
+ **math utils** (`from toolbox.math.math_utils import *`): contains some useful math functions like `clamp`, `lerp` and `random`
+ **vector math** (`from toolbox.math.vector_math import *`): provides vector math functions and a class for 2 and 3 float vectors
+ **graphics** (`from toolbox.gfx.graphics import *`): wraps pygame rendering functions for drawing points, lines and polygons for an easier access and a cleaner syntax

## Used technologies:
- **Python**\
Programming language\
Version: *3.13.5*\
Home page: https://www.python.org/

- **pygame**\
Python Game Development\
Version: *2.6.1*\
Home page: https://www.pygame.org

## About
Made by G3Dev
v1.0 b28092025-0
