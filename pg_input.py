import pygame

_mouse_x = 0
_mouse_y = 0
_mouse_scroll = 0
_can_press_keys = None
_can_release_keys = None
_can_press_buttons = None
_can_release_buttons = None

def pgi_init():
    """
    automatically called to initialize the input module, you don't need to call this
    """
    global keys, _can_press_keys, _can_release_keys, NUM_KEYS
    global buttons, _can_press_buttons, _can_release_buttons, NUM_BUTTONS

    # keyboard
    keys = pygame.key.get_pressed()
    NUM_KEYS = len(keys)

    _can_press_keys = [False] * NUM_KEYS
    _can_release_keys = [False] * NUM_KEYS

    # mouse
    buttons = pygame.mouse.get_pressed()
    NUM_BUTTONS = len(buttons)

    _can_press_buttons = [False] * NUM_BUTTONS
    _can_release_buttons = [False] * NUM_BUTTONS

def pgi_tick():
    """
    automatically called to update the input module, you don't need to call this
    """
    global keys, _can_press_keys, _can_release_keys, NUM_KEYS
    global buttons, _can_press_buttons, _can_release_buttons, NUM_BUTTONS, _mouse_x, _mouse_y

    keys = pygame.key.get_pressed()
    buttons = pygame.mouse.get_pressed()
    _mouse_x, _mouse_y = pygame.mouse.get_pos()

    # keyboard
    for i in range(NUM_KEYS):
        if keys[i]: _can_release_keys[i] = True
        else: _can_press_keys[i] = True

    # mouse
    for i in range(NUM_BUTTONS):
        if buttons[i]: _can_release_buttons[i] = True
        else: _can_press_buttons[i] = True


# KEYBOARD

def is_key_down(key) -> bool:
    """
    returns True if the given key is currently being pressed (takes pygame.K_keyname),
    returns False otherwise
    """
    global keys
    return keys[key]

def is_key_pressed(key) -> bool:
    """
    returns True the first tick the given key is pressed (takes pygame.K_keyname),
    returns False otherwise
    """
    global keys, _can_press_keys
    if keys[key] and _can_press_keys[key]:
        _can_press_keys[key] = False
        return True

def is_key_released(key) -> bool:
    """
    returns True the first tick the given key is released (takes pygame.K_keyname),
    returns False otherwise
    """
    global keys, _can_release_keys
    if not keys[key] and _can_release_keys[key]:
        _can_release_keys[key] = False
        return True
    
# MOUSE

def is_button_down(button) -> bool:
    """
    returns True if the given mouse button is currently being pressed (takes pygame.BUTTON_buttonname),
    returns False otherwise
    """
    global buttons
    button -= 1 # left is 1, middle is 2, right is 3 for pygame...just decrement by one and everythign is fine
    return buttons[button]

def is_button_pressed(button) -> bool:
    """
    returns True the first tick the given mouse button is pressed (takes pygame.BUTTON_buttonname),
    returns False otherwise
    """
    global buttons, _can_press_buttons
    button -= 1 # left is 1, middle is 2, right is 3 for pygame...just decrement by one and everythign is fine
    if buttons[button] and _can_press_buttons[button]:
        _can_press_buttons[button] = False
        return True

def is_button_released(button) -> bool:
    """
    returns True the first tick the given mouse button is released (takes pygame.BUTTON_buttonname),
    returns False otherwise
    """
    global buttons, _can_release_buttons
    button -= 1 # left is 1, middle is 2, right is 3 for pygame...just decrement by one and everythign is fine
    if not buttons[button] and _can_release_buttons[button]:
        _can_release_buttons[button] = False
        return True
    
def get_mouse_x() -> int:
    global _mouse_x
    return _mouse_x

def get_mouse_y() -> int:
    global _mouse_y
    return _mouse_y

def get_mouse_position() -> tuple[int, int]:
    global _mouse_x, _mouse_y
    return (_mouse_x, _mouse_y)

def get_mouse_scroll() -> int:
    global _mouse_scroll
    return _mouse_scroll

def pgi_set_mouse_scroll(scroll:int):
    global _mouse_scroll
    _mouse_scroll = scroll