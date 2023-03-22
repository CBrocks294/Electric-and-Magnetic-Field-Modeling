class Vector:
    def __init__(self, xMagnitude = 1, YMagnitude = 1, ZMagnitude = 1):
        self.xMagnitude = xMagnitude
        self.yMagnitude = YMagnitude
        self.zMagnitude = ZMagnitude

    def __add__(self, other):
        return Vector(self.xMagnitude + other.xMagnitude,
                      self.YMagnitude + other.YMagnitude,
                      self.ZMagnitude + other.ZMagnitude)

    def __sub__(self, other):
        return Vector(self.xMagnitude - other.xMagnitude,
                      self.YMagnitude - other.YMagnitude,
                      self.ZMagnitude - other.ZMagnitude)
