class Vector:
    def __init__(self, xMagnitude=1, YMagnitude=1, ZMagnitude=1):
        self.xMagnitude = xMagnitude
        self.yMagnitude = YMagnitude
        self.zMagnitude = ZMagnitude
        self.modulus = (self.xMagnitude ** 2 + self.yMagnitude ** 2 + self.zMagnitude ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.xMagnitude + other.xMagnitude,
                      self.YMagnitude + other.YMagnitude,
                      self.ZMagnitude + other.ZMagnitude)

    def __sub__(self, other):
        return Vector(self.xMagnitude - other.xMagnitude,
                      self.YMagnitude - other.YMagnitude,
                      self.ZMagnitude - other.ZMagnitude)

    def __mul__(self, other):
        return Vector(self.xMagnitude * other,
                      self.yMagnitude * other,
                      self.zMagnitude * other)

    def __truediv__(self, other):
        if other == 0:
            raise Exception(ZeroDivisionError)
        return self * (1 / other)

    def dotProduct(self, vect1, vect2):
        return (vect1.xMagnitude * vect2.xMagnitude
                + vect1.yMagnitude * vect2.yMagnitude
                + vect1.zMagnitude * vect2.zMagnitude)

    def normalise(self, vector):
        return vector / vector.modulus
