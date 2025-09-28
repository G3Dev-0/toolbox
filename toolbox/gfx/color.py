from toolbox.math.math_utils import clamp

class color:
    def __init__(self, r:float|int, g:float|int, b:float|int):
        """
        takes in either [0.0, 1.0] ranged floats or [0, 255] ranged integers
        """
        if type(r) == type(g) == type(b) == float:
            r = clamp(r, 0.0, 1.0)
            g = clamp(g, 0.0, 1.0)
            b = clamp(b, 0.0, 1.0)
        elif type(r) == type(g) == type(b) == int:
            r = int(clamp(r, 0, 255))
            g = int(clamp(g, 0, 255))
            b = int(clamp(b, 0, 255))
        else:
            print("[Error]: Invalid color arguments")
            r = g = b = 0

        self.r = r
        self.g = g
        self.b = b

    def scale_by(self, scale:float) -> "color":
        """
        returns the current color with the r g b components scaled by the given amount
        """
        return color(self.r * scale, self.g * scale, self.b * scale)
    
    def brightness(self) -> float:
        """
        returns this color brightness calculated using the average between
        the maximum and the minimum among its r g b values
        """
        values = self.values()
        return (max(values) + min(values)) / 2

    def luminance(self) -> float:
        """
        returns the relative (human percieved) color luminance
        """
        return 0.2126 * self.r + 0.7152 * self.g + 0.0722 * self.b
    
    def to_floats(self) -> "color":
        """
        returns the current color with the r g b components turned into [0.0, 1.0] ranged floats
        """
        if type(self.r) == type(self.g) == type(self.b) == float: return self
        return color(self.r / 255.0, self.g / 255.0, self.b / 255.0)
    
    def to_ints(self) -> "color":
        """
        returns the current color with the r g b components turned into [0, 255] ranged integers
        """
        if type(self.r) == type(self.g) == type(self.b) == int: return self
        return color(int(self.r * 255), int(self.g * 255), int(self.b * 255))
    
    def values(self) -> tuple[float, float, float]|tuple[int, int, int]:
        """
        returns the color r g b values as a tuple (r, g, b)
        """
        return (self.r, self.g, self.b)
    
    def __str__(self):
        r, g, b = self.values()
        if type(r) == type(g) == type(b) == float:
            return f"color({r:.1f}, {g:.1f}, {b:.1f})"
        if type(r) == type(g) == type(b) == int:
            return f"color({r}, {g}, {b})"

### COLOR CONSTANTS

WHITE = color(1.0, 1.0, 1.0)
LIGHT_GRAY = WHITE.scale_by(0.75) # 3/4 white
GRAY = WHITE.scale_by(0.5) # 2/4 white
DARK_GRAY = WHITE.scale_by(0.25) # 1/4 white
BLACK = color(0.0, 0.0, 0.0)

RED = color(1.0, 0.0, 0.0)
GREEN = color(0.0, 1.0, 0.0)
BLUE = color(0.0, 0.0, 1.0)

CYAN = color(0.0, 1.0, 1.0)
MAGENTA = color(1.0, 0.0, 1.0)
YELLOW = color(1.0, 1.0, 0.0)

DARK_RED = RED.scale_by(0.5)
DARK_GREEN = GREEN.scale_by(0.5)
DARK_BLUE = BLUE.scale_by(0.5)

DARK_CYAN = CYAN.scale_by(0.5)
DARK_MAGENTA = MAGENTA.scale_by(0.5)
DARK_YELLOW = YELLOW.scale_by(0.5)

LIGHT_RED = color(1.0, 0.5, 0.5)
LIGHT_GREEN = color(0.5, 1.0, 0.5)
LIGHT_BLUE = color(0.5, 0.5, 1.0)

LIGHT_CYAN = color(0.5, 1.0, 1.0)
LIGHT_MAGENTA = color(1.0, 0.5, 1.0)
LIGHT_YELLOW = color(1.0, 1.0, 0.5)