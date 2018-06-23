class Vector:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
