import shutil
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

#import toolbox.pg_input as pgi
from toolbox.pg_input import pgi_init, pgi_tick, pgi_set_mouse_scroll, get_mouse_x, get_mouse_y, get_mouse_position, get_mouse_scroll, is_key_down, is_key_pressed, is_key_released, is_button_down, is_button_pressed, is_button_released
from toolbox.gfx.color import *

### MAIN VARIABLES
has_requested_quit = False
tps = 60 # ticks per second
fps = 60 # frames per second
logic_interval = 1000 // tps
render_interval = 1000 // fps
actual_tps = 0
actual_fps = 0

_time = 0

_screen = None
_font = None

_auto_clear = True
_background_color = WHITE

### MAIN FUNCTIONS

def create_canvas(title:str, width:int, height:int):
    """
    creates a canvas with the given title and size
    """
    global _screen, _font

    # start pygame
    pygame.init()

    # window
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)

    # initialize input
    pgi_init()

    # create font
    pygame.font.init()
    _font = pygame.font.SysFont('Consolas', 16)

_tick_count = 0
_draw_count = 0

def run(init, tick, draw):
    """
    runs the main loop with the given functions
    """
    # I know importing debug_draw() here is a very bad practice,
    # but this run function is called only once,
    # and we need the debug_draw() to call functions in here
    # that are defined when we call run() but not before...
    # circular import is never cool but I need it here
    from toolbox.debug import debug_draw

    global actual_tps, actual_fps, _tick_count, _draw_count
    global _time

    # login and rendering timer
    last_logic_update = pygame.time.get_ticks()
    last_render_update = pygame.time.get_ticks()
    last_tps_fps_update = pygame.time.get_ticks()

    # clear the screen once before calling init so that
    # if you want you can also do a "draw once sketch"
    # where you just draw once and then don't clear the screen
    clear(_background_color)

    init()

    while not has_requested_quit:
        # reset mouse scroll
        # pgi.set_mouse_scroll(0)
        pgi_set_mouse_scroll(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                request_close()
            if event.type == pygame.MOUSEWHEEL:
                pgi_set_mouse_scroll(event.y)

        now = pygame.time.get_ticks()

        # every SECOND we get how many ticks per SECOND and how many frames per SECOND
        # if instead of 1000 we put 2000 we would have to divide by two the numbers we obtain
        if now - last_tps_fps_update >= 1000:
            actual_tps = _tick_count
            actual_fps = _draw_count
            _tick_count = 0
            _draw_count = 0
            last_tps_fps_update = now

        # Logic update
        if now - last_logic_update >= logic_interval:
            pgi_tick()
            if is_key_pressed(pygame.K_ESCAPE): request_close()
            # custom app tick
            tick()
            _tick_count += 1
            last_logic_update = now

            _time += logic_interval

        # Rendering update
        if now - last_render_update >= render_interval:
            # background filling
            if _auto_clear: clear(_background_color)
            # custom app draw
            draw()

            debug_draw()

            _draw_count += 1
            # swap buffers to refresh the canvas and draw the just-built frame
            pygame.display.flip()
            last_render_update = now
    
    # this deletes the "__pycache__" folders that where created
    # delete all "__pycache__" folders
    clear_pycache(os.getcwd())
    
    pygame.quit()

### UTILITY FUNCTIONS

def get_width() -> int:
    """
    returns the canvas width
    """
    return _screen.get_width()

def get_height() -> int:
    """
    returns the canvas height
    """
    return _screen.get_height()

def get_aspect_ratio() -> float:
    """
    returns the canvas aspect ratio
    """
    return get_width() / get_height()

def get_time_millis() -> int:
    """
    returns the current run time in milliseconds
    """
    return _time

def get_time_seconds() -> float:
    """
    returns the current run time in seconds
    """
    return _time / 1000.0

def tick_rate(ticks_per_second:int):
    """
    sets the tick rate (default is 60)
    lowering this will make movements slow, increasing it will make them faster
    """
    global tps, logic_interval
    tps = ticks_per_second
    logic_interval = 1000 // tps

def frame_rate(frames_per_second:int):
    """
    sets the frame rate (default is 60)
    lowering this will make movements laggy, increasing it will make them smoother
    """
    global fps, render_interval
    fps = frames_per_second
    render_interval = 1000 // fps

def get_tps() -> int:
    """
    returns the current tps
    """
    return actual_tps

def get_fps() -> int:
    """
    returns the current fps
    """
    return actual_fps

def get_delta_time() -> float:
    """
    returns the current delta time (calcualted based on the current tps)
    """
    if actual_tps == 0: return 0
    return 1.0 / actual_tps

def request_close():
    """
    gently asks to close the canvas
    """
    global has_requested_quit
    has_requested_quit = True

def clear_pycache(path):
    """
    deletes all the __pycache__ folders
    it cannot be called unless quit is scheduled, and it will be autamically called
    when quit is requested, so you should NEVER call this manually
    """
    if not has_requested_quit: return
    for fileName in os.listdir(path):
        newPath = f"{path}/{fileName}"
        if str(fileName).strip() == "__pycache__":
            shutil.rmtree(newPath)
            continue
        if os.path.isdir(newPath):
            clear_pycache(newPath)

### GRAPHICS FUNCTIONS

def auto_clear(auto_clear:bool):
    """
    sets the automatic clear function (ENABLED by default)
    True means you don't have to manually call the "clear()" function to clear the screen
    """
    global _auto_clear
    _auto_clear = auto_clear

def clear(color:color=None):
    """
    clears the screen to the given color if specified
    clears the screen to the set background color if color is None
    """
    if color == None: color = _background_color
    _screen.fill(color.to_ints().values())

def set_background(color:color=WHITE):
    """
    sets the background color
    """
    global _background_color
    _background_color = color