import math
class Current():

    def __init__(self, frequency, peakvoltage, inductance):
        self.frequency = frequency
        self.peakvoltage = peakvoltage
        self.inductance = inductance

    def current(self, time):
        return self.peakvoltage * math.cos(1 / self.frequency * math.pi * time) / self.inductance / self.frequency

    def currentFluxDensity(self, time):
        diameter = 0.002
        cross_sectional_area = (diameter / 2) ** 2 * math.pi
        return self.current(time) / cross_sectional_area
