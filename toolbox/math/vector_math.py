from math import sqrt, cos, sin, radians, atan2, degrees

class vector2:
    def __init__(self, x:float=0.0, y:float=0.0):
        self.x = x
        self.y = y
    
    def set(self, x:float, y:float):
        self.x = x
        self.y = y

    def get_x(self) -> int:
        """
        returns the x component casted as integer
        """
        return int(self.x)
    
    def get_y(self) -> int:
        """
        returns the y component casted as integer
        """
        return int(self.y)
    
    def int_values(self) -> tuple[int, int]:
        """
        returns the vector components as an integer tuple (x, y)
        """
        return (self.get_x(), self.get_y())
    
    def add(self, vector:"vector2"):
        self.x += vector.x
        self.y += vector.y
    
    def scale(self, s:"float|vector2"):
        if type(s) == float or type(s) == int:
            self.x *= s
            self.y *= s
        elif type(s) == vector2:
            self.x *= s.x
            self.y *= s.y
        else:
            print("[Error] (in vector2.scale): Invalid scale parameter type")

    def divide(self, div:float):
        if div == 0:
            print("[Error] (in vector2.divide): Invalid div parameter value (can't divide by 0)")
            return
        self.x /= div
        self.y /= div
    
    def get_angle(self) -> float:
        """
        returns the vector angle in degrees
        """
        return degrees(atan2(self.y, self.x))

    def copy(self) -> "vector2":
        return vector2(self.x, self.y)

    def __str__(self):
        return f"vector2({self.x:.2f}, {self.y:.2f})"
    
    def __eq__(self, value):
        if value == None: return False
        return self.x == value.x and self.y == value.y

class vector3:
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def set(self, x:float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

    def values(self) -> tuple[float, float, float]:
        """
        returns the vector components as a tuple (x, y, z)
        """
        return (self.x, self.y, self.z)

    def copy(self) -> "vector3":
        return vector3(self.x, self.y, self.z)

    def __str__(self):
        return f"vector3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __eq__(self, value):
        if value == None: return False
        return self.x == value.x and self.y == value.y and self.z == value.z

def zero(dim:int=3) -> vector3|vector2:
    """
    returns vector3(0.0, 0.0, 0.0) if dim == 3 (default) or vector2(0.0, 0.0) if dim == 2
    """
    if dim == 2: return vector2(0.0, 0.0)
    elif dim == 3: return vector3(0.0, 0.0, 0.0)
    else:
        print("[Error] (in zero): Invalid vector dimensions (either 2 or 3)")
        return None

def one(dim:int=3) -> vector3|vector2:
    """
    returns the vector3(1.0, 1.0, 1.0) if dim == 3 (default) or vector2(1.0, 1.0) if dim == 2
    """
    if dim == 2: return vector2(1.0, 1.0)
    elif dim == 3: return vector3(1.0, 1.0, 1.0)
    else:
        print("[Error] (in one): Invalid vector dimensions (either 2 or 3)")
        return None

def from_polar(angle:float, magnitude:float) -> vector2:
    """
    returns a vector with the given magnitude and degree angle
    with respect to the horizontal axis (the angle increases counter-clockwise)
    """
    theta = radians(angle)
    return vector2(magnitude * cos(theta), magnitude * sin(theta))

def sum(v0:vector2|vector3, v1:vector2|vector3) -> vector2|vector3:
    """
    sums the given vectors and returns the result
    """
    if type(v0) == type(v1) == vector2:
        return vector2(v0.x + v1.x, v0.y + v1.y)
    elif type(v0) == type(v1) == vector3:
        return vector3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)
    else:
        print("[Error] (in sum): Invalid vector parameter types")
        return None

def difference(v0:vector2|vector3, v1:vector2|vector3) -> vector2|vector3:
    """
    subtracts the given vectors and returns the result
    """
    if type(v0) == type(v1) == vector2:
        return vector2(v0.x - v1.x, v0.y - v1.y)
    elif type(v0) == type(v1) == vector3:
        return vector3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)
    else:
        print("[Error] (in difference): Invalid vector parameter types")
        return None

def scale(v:vector2|vector3, s:float|vector2|vector3) -> vector2|vector3:
    """
    scales the given vector by the given float or vector3 and returns the result

    if the scale is a float all the vector components will be multiplied by that same number
    if the scale is a vector, the x component will be multiplied by the x scale vector compoenent
    the y with the y and z with the z
    """
    if type(s) == float or type(s) == int:
        if type(v) == vector2:
            return vector2(v.x * s, v.y * s)
        elif type(v) == vector3:
            return vector3(v.x * s, v.y * s, v.z * s)
        else:
            print("[Error] (in scale): Invalid vector parameter type")
            return None
    elif type(s) == type(v) == vector2:
        return vector3(v.x * s.x, v.y * s.y)
    elif type(s) == type(v) == vector2:
        return vector3(v.x * s.x, v.y * s.y, v.z * s.z)
    else:
        print("[Error] (in scale): Invalid scale and/or vector parameter type")
        return None

def negate(v:vector2|vector3) -> vector2|vector3:
    """
    scales the given vector by -1 (inverts the sign of all its components)
    and returns the result
    """
    return scale(v, -1)

def magnitude(v:vector2|vector3) -> float:
    """
    returns the given vector magnitude
    """
    if type(v) == vector2:
        return sqrt(v.x * v.x + v.y * v.y)
    elif type(v) == vector3:
        return sqrt(v.x * v.x + v.y * v.y + v.z * v.z)
    else:
        print("[Error] (in magnitude): Invalid vector parameter types")

def normalize(v:vector2|vector3) -> vector2|vector3:
    """
    normalizes the given and returns the result
    """
    mag = magnitude(v)
    if mag == 0:
        if type(v) == vector2:
            return vector2()
        elif type(v) == vector3:
            return vector3()
        else:
            print("[Error] (in normalize): Invalid vector parameter type")
            return None
    return scale(v, 1 / mag)

def dot(v0:vector2|vector3, v1:vector2|vector3) -> float:
    """
    calculates the dot product between the given vectors,
    then returns the result
    """
    if type(v0) == type(v1) == vector2:
        return v0.x * v1.x + v0.y * v1.y
    elif type(v0) == type(v1) == vector3:
        return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z
    else:
        print("[Error] (in dot): Invalid vector parameter types")
        return None

def cross(v0:vector3, v1:vector3) -> vector3:
    """
    performs the cross product between the given vectors,
    then returns the result
    """
    return vector3(
        v0.y * v1.z - v1.y * v0.z,
        v1.x * v0.z - v0.x * v1.z,
        v0.x * v1.y - v1.x * v0.y
    )

def rotate2D(vector:vector2, angle:float) -> vector2:
    """
    rotates the given vector by the given degree angle
    returns the rotated vector
    """
    theta = radians(angle)
    cs = cos(theta)
    sn = sin(theta)
    a =  vector2(
        cs * vector.x - sn * vector.y,
        sn * vector.x + cs * vector.y
    )
    return a

def rotate3D(vector:vector3, euler_angles:vector3) -> vector3:
    """
    rotates the given vector by the given degree euler angles (pitch, yaw, roll)
    then returns the rotated vector
    """
    # rotate around the z axis
    x, y, z = vector.values()
    
    # rotate around all the three axes
    angles = euler_angles.values()
    for rotation in range(3):
        rotation = 3 - 1 - rotation # do z first, then y, then x (roll, yaw, pitch)
        theta = radians(angles[rotation])
        cs = cos(theta)
        sn = sin(theta)
        # rotation == 0 is around the x axis
        if rotation == 0:
            rx = 1*x + 0*y + 0*z
            ry = 0*x + cs*y + sn*z
            rz = 0*x + -sn*y + cs*z
        # rotation == 1 is around the y axis
        elif rotation == 1:
            rx = cs*x + 0*y + sn*z
            ry = 0*x + 1*y + 0*z
            rz = -sn*x + 0*y + cs*z
        # rotation == 2 is around the z axis
        elif rotation == 2:
            rx = cs*x + sn*y + 0*z
            ry = -sn*x + cs*y + 0*z
            rz = 0*x + 0*y + 1*z

        # prepare for the next rotation
        x, y, z = rx, ry, rz

    return vector3(rx, ry, rz)

def distance(p0:vector2|vector3, p1:vector2|vector3) -> float:
    """
    returns the distance between the given points
    """
    return magnitude(difference(p0, p1))

def clamp_magnitude(vector:vector2|vector3, minimum_magnitude:float=None, maximum_magnitude:float=None) -> vector2|vector3:
    """
    returns a vector with a clamped magnitude between minimum and maximum and the same direction
    of the given vector

    if minimum magnitude is None it just clamps to maximum magnitude
    if maximum magnitude is None it just clamps to minimum magnitude
    """
    if minimum_magnitude == maximum_magnitude == None: return vector

    mag = magnitude(vector)
    if minimum_magnitude == None: minimum_magnitude = mag
    if maximum_magnitude == None: maximum_magnitude = mag

    if mag < minimum_magnitude: return scale(normalize(vector), minimum_magnitude)
    elif mag > maximum_magnitude: return scale(normalize(vector), maximum_magnitude)
    else: return vector
    
def set_magnitude(vector:vector2|vector3, magnitude:float) -> vector2|vector3:
    """
    returns a vector with the given magnitude and the same direction of the given vector
    """
    return scale(normalize(vector), magnitude)