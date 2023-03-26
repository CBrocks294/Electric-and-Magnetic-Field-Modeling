# AUTHOR: CHRISTOPHER BROCKLEBANK
import random


class Vector:
    def __init__(self, xMagnitude=1, yMagnitude=1, zMagnitude=1):
        self.xMagnitude = xMagnitude
        self.yMagnitude = yMagnitude
        self.zMagnitude = zMagnitude
        self.modulus = (self.xMagnitude ** 2 + self.yMagnitude ** 2 + self.zMagnitude ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.xMagnitude + other.xMagnitude,
                      self.yMagnitude + other.yMagnitude,
                      self.zMagnitude + other.zMagnitude)

    def __iadd__(self, other):
        self.xMagnitude += other.xMagnitude
        self.yMagnitude += other.yMagnitude
        self.zMagnitude += other.zMagnitude
        self.modulus = (self.xMagnitude ** 2 + self.yMagnitude ** 2 + self.zMagnitude ** 2) ** 0.5
        return(self)

    def __isub__(self, other):
        self.xMagnitude -= other.xMagnitude
        self.yMagnitude -= other.yMagnitude
        self.zMagnitude -= other.zMagnitude
        self.modulus = (self.xMagnitude ** 2 + self.yMagnitude ** 2 + self.zMagnitude ** 2) ** 0.5
        return(self)

    def __sub__(self, other):
        return Vector(self.xMagnitude - other.xMagnitude,
                      self.yMagnitude - other.yMagnitude,
                      self.zMagnitude - other.zMagnitude)

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

    @staticmethod
    def normalise(vector):
        return vector / vector.modulus
