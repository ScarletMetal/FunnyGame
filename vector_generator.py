class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        self.x *= other
        self.y *= other
