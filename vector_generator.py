import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2)

    def get_magnitude(self):
        self.magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        return self.magnitude

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)
