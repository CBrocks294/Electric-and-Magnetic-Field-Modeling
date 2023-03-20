import math
class current():
    self.frequency
    self.peakVoltage
    self.inductance
    def __init__(frequency, peakVoltage, inductance):
        self.frequency = frequency
        self.peakVoltage = peakVoltage
        self.inductance = inductance

    def current(time):
        return(peakVoltage* math.cos(1/frequency*math.pi)/inductance/frequency)




