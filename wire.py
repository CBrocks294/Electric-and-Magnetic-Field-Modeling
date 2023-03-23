import math
import vector
class Wire():

    def __init__(self, frequency, peakvoltage, inductance, coilRadius, wireRadius, turnRate):
        self.frequency = frequency
        self.peakvoltage = peakvoltage
        self.inductance = inductance
        self.coilRadius = coilRadius
        self.wireRadius = wireRadius
        self.turnRate = turnRate

    def current(self, time):
        return self.peakvoltage * math.cos(1 / self.frequency * math.pi * time) / self.inductance / self.frequency

    def currentFluxDensity(self, time):
        diameter = 0.002
        cross_sectional_area = (diameter / 2) ** 2 * math.pi
        return self.current(time) / cross_sectional_area

    def inWire(self, x,y,z):
        return (x-math.sin(z/self.turnRate))**2 (y-math.cos(z/self.turnRate))**2 <= self.wireRadius

    def fluxVector(self, t):
        return vector.Vector.normalise(vector.Vector(math.cos(t), - math.sin(t), self.turnRate)) * self.currentFluxDensity(t)
