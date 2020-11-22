from math import sqrt


# Implementation of a point in 3d.
class Point3:

    # X value of the point
    x: float

    # Y value of the point
    y: float

    # Z value of the point
    z: float

    # Constructs a new Point3 object
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    # Returns the distance from the actual point to another
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    # Returns the x distance from the actual point to another
    def delta_x(self, other):
        return self.x - other.x

    # Returns the y distance from the actual point to another
    def delta_y(self, other):
        return self.y - other.y

    # Returns the z distance from the actual point to another
    def delta_z(self, other):
        return self.z - other.z

    # Returns the 2d distance from the actual point to another
    def dist_2d(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # Returns a textual representation of a point
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
