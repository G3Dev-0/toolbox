import toolbox.canvas as canvas
import toolbox.math.math_utils as mathu
import toolbox.math.vector_math as vm
from toolbox.gfx.color import *

### GRAPHICS CONSTANTS

fill_color = None

### GRAPHICS and DRAWING FUNCTIONS

def fill(color:color|None=BLACK):
    """
    sets the fill color for shape drawing, set to None to disable shape filling
    """
    global fill_color
    fill_color = color

def point(position:vm.vector2, color:color=BLACK, radius:int=2):
    """
    draws a point in screen space ([0, width - 1], [0, height - 1])
    """
    canvas.pygame.draw.circle(canvas._screen, color.to_ints().values(), position.int_values(), radius)

def line(p0:vm.vector2, p1:vm.vector2, color:color=BLACK, stroke:int=1):
    """
    draws a line between the two given points in screen space ([0, width - 1], [0, height - 1])
    """
    canvas.pygame.draw.line(canvas._screen, color.to_ints().values(), p0.int_values(), p1.int_values(), stroke)

def rect(top_left:vm.vector2, bottom_right:vm.vector2, color:color=BLACK, stroke:int=1):
    """
    draws a rectangle between the two given corner points in screen space ([0, width - 1], [0, height - 1])
    """
    rectangle = [
        top_left.get_x(), top_left.get_y(),
        abs(bottom_right.get_x() - top_left.get_x()),
        abs(bottom_right.get_y() - top_left.get_y())
    ]
    # fill the rect
    if fill_color != None:
        canvas.pygame.draw.rect(canvas._screen, fill_color.to_ints().values(), rectangle, 0)
    # draw boundries
    canvas.pygame.draw.rect(canvas._screen, color.to_ints().values(), rectangle, stroke)

def circle(center:vm.vector2, radius:int, color:color=BLACK, stroke:int=1):
    """
    draws a circle with the given radius and center point in screen space ([0, width), [0, height))
    """
    # fill the circle
    if fill_color != None:
        canvas.pygame.draw.circle(canvas._screen, fill_color.to_ints().values(), center.int_values(), radius, 0)
    # draw boundries
    canvas.pygame.draw.circle(canvas._screen, color.to_ints().values(), center.int_values(), radius, stroke)

def square(top_left:vm.vector2, side_length:int, color:color=BLACK, stroke:int=1):
    """
    draws a square with the given side length and the top left corner point in screen space ([0, width), [0, height))
    """
    rect(top_left.int_values(), (top_left.get_x() + side_length, top_left.get_y() + side_length), color.to_ints().values(), stroke)

TRIANGLE_VERTICES = [
    vm.vector2(-0.5, 0),
    vm.vector2(0.5, 0),
    vm.vector2(0, -1)
]
def triangle(position:vm.vector2, angle:float, base:float=1, height:float=1, color:color=BLACK, stroke:int=1):
    """
    draws a triangle at the given position in screen space ([0, width - 1], [0, height - 1])
    with the given degree angle rotation, base length and height
    """
    scaling = vm.vector2(base, height)
    vertices = TRIANGLE_VERTICES.copy()
    for i in range(3):
        vertices[i] = vm.scale(TRIANGLE_VERTICES[i], scaling)
        vertices[i] = vm.rotate2D(vertices[i], angle)
        vertices[i] = vm.sum(vertices[i], position)
        vertices[i] = vertices[i].int_values()
    # fill the triangle
    if fill_color != None:
        canvas.pygame.draw.polygon(canvas._screen, fill_color.to_ints().values(), vertices, 0)
    # draw boundries
    canvas.pygame.draw.polygon(canvas._screen, color.to_ints().values(), vertices, stroke)
    
def polygon(vertices:list[vm.vector2], color:color=BLACK, stroke:int=1):
    """
    draws a polygon made by connecting together the given vertices with a line
    """
    if len(vertices) < 2:
        print("[Error] (in polygon): not enough points!")
        return
    vertices = list(map(vm.vector2.int_values, vertices))
    # fill the polygon
    if fill_color != None:
        canvas.pygame.draw.polygon(canvas._screen, fill_color.to_ints().values(), vertices, 0)
    # draw boundries
    canvas.pygame.draw.polygon(canvas._screen, color.to_ints().values(), vertices, stroke)

def lines(vertices:list[vm.vector2], closed:bool, color:color=BLACK, stroke:int=1):
    """
    draws a line connecting the given vertices, does not get affected by filling even when closed = True
    to fill a closed line use polygon
    """
    if len(vertices) < 2:
        print("[Error] (in lines): not enough points!")
        return
    vertices = list(map(vm.vector2.int_values, vertices))
    # draw boundries
    canvas.pygame.draw.lines(canvas._screen, color.to_ints().values(), closed, vertices, stroke)

def write(text, x, y, foregroud_color:color=BLACK, backgroud_color:color|None=None, backgroud_alpha:float|None=0.2) -> tuple[int, int]:
    """
    draws text at given coordinates in screen space.
    backgroud_alpha has no effect if the backgroud_color is set to None
    returns the size of the text box (width, height)
    """
    textSurface = canvas._font.render(text, True, foregroud_color.to_ints().values(), None)
    size = canvas._font.size(text)
    
    textBackgroundSurface = canvas.pygame.Surface(textSurface.get_size())
    if backgroud_color:
        textBackgroundSurface.fill(backgroud_color.to_ints().values()) # make sure you take the [0-255] ranged integer RGB components
        textBackgroundSurface.set_alpha(mathu.clamp(backgroud_alpha * 255, 0, 255))
    else:
        textBackgroundSurface.set_alpha(0)
    
    canvas._screen.blit(textBackgroundSurface, (x, y))
    canvas._screen.blit(textSurface, (x, y))

    return size

def vector(vector:vm.vector2, application_point:vm.vector2, color:color=RED, stroke:int=2, draw_tip:bool=2):
    """
    draws the given vector at the given application point
    if draw_tip = 0 the tip isn't drawn
    if draw_tip = 1 the tip is drawn as a point
    if draw_tip = 2 the tip is drawn as a triangle
    """
    if vm.magnitude(vector) == 0:
        point(application_point, color, stroke)
        return
    end = vm.sum(application_point, vector)
    line(application_point, end, color, stroke)
    if draw_tip == 1:
        point(end, color, stroke + 1)
    if draw_tip == 2:
        triangle(end, vector.get_angle() + 90, stroke * 5, stroke * 7, color, 0)