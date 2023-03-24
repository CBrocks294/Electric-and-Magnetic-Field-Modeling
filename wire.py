# AUTHOR: CHRISTOPHER BROCKLEBANK

import math
import vector


class Wire():

    def __init__(self, frequency, peakvoltage, inductance, coilRadius, wireRadius, turnRate, startPos, length):
        self.frequency = frequency
        self.peakvoltage = peakvoltage
        self.inductance = inductance
        self.coilRadius = coilRadius
        self.wireRadius = wireRadius
        self.turnRate = turnRate
        self.start = startPos
        self.end = startPos+length

    def current(self, time):
        return self.peakvoltage * math.cos(1 / self.frequency * math.pi * time) / self.inductance / self.frequency

    def currentFluxDensity(self, time):
        cross_sectional_area = self.wireRadius ** 2 * math.pi
        return self.current(time) / cross_sectional_area

    def inWire(self, x, y, z):
        return ((x - math.sin(z / self.turnRate)) ** 2 + (y - math.cos(z / self.turnRate)) ** 2 <= self.wireRadius
                and (z > self.start) and z < self.end)

    def fluxVector(self, time, x, y, z):
        if self.inWire(x, y, z):
            return (vector.Vector.normalise(vector.Vector(math.cos(z/self.turnrate)*2*math.pi,
                                                          - math.sin(z/self.turnrate)*2*math.pi,
                                                          self.turnRate))
                    * self.currentFluxDensity(time))
        else:
            return vector.Vector(0, 0, 0)
