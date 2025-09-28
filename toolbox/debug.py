from toolbox.gfx.graphics import write
from toolbox.canvas import *

### DEBUG FLAGS
DEBUG_SHOW_CANVAS_INFO = "debug_show_canvas_info"
DEBUG_SHOW_INPUT_INFO = "debug_show_input_info"

flags = {
    DEBUG_SHOW_CANVAS_INFO: False,
    DEBUG_SHOW_INPUT_INFO: False
}

### DEBUG
def debug_set_flag(flag:str, enabled:bool):
    """
    enables or disables the given debug flag
    """
    if not flag in flags.keys():
        print(f"[Error]: Invalid debug flag for \"{flag}\"!")
        return
    flags[flag] = enabled

def debug_toggle_flag(flag:str):
    """
    switches the given debug flag state
    (disables it if it's enabled, enables it if it's disabled)
    """
    if not flag in flags.keys():
        print(f"[Error]: Invalid debug flag for \"{flag}\"!")
        return
    flags[flag] = not flags[flag]

def is_debug_flag_enabled(flag:str) -> bool:
    """
    returns the given debug flag state (True = enabled, False = disabled)
    """
    if not flag in flags.keys():
        print(f"[Error]: Invalid debug flag for \"{flag}\"!")
        return False
    return flags[flag]

def debug_create_flag(flag:str, enabled:bool):
    """
    creates a new debug flag with the given id (flag) and the given initial state (enabled)
    """
    if flag in flags.keys():
        print(f"[Error]: Already existing debug flag for \"{flag}\"!")
        return
    flags[flag] = enabled

### DRAW FUNCTION

_y = 0
def write_debug_line(line:str="", foreground:color=BLACK):
    """
    automatically handles line accumulation
    skips a line if line is ""
    """
    global _y
    _, h = write(line, 0, _y, foregroud_color=foreground, backgroud_color=LIGHT_GRAY, backgroud_alpha=0.2)
    if line == "" and _y == 0: h = 0
    _y += h

def debug_draw():
    global _y
    _y = 0 # reset line y coordinate

    if is_debug_flag_enabled(DEBUG_SHOW_CANVAS_INFO):
        write_debug_line(f"TPS: {get_tps()}; FPS: {get_fps()}; DT: {get_delta_time():.2f}")
        write_debug_line(f"W: {get_width()}; H: {get_height()}; AR: {get_aspect_ratio():.2f}")
        write_debug_line(f"T: {get_time_millis()} ms")
    if is_debug_flag_enabled(DEBUG_SHOW_INPUT_INFO):
        write_debug_line()
        write_debug_line(f"MP: {get_mouse_position()}; MS: {get_mouse_scroll()}")