# AUTHOR: CHRISTOPHER BROCKLEBANK

import vector_field
import vector


class MagneticField(vector_field.VectorField):
    def __init__(self, size):
        super().__init__(size)

    def changeVector(self, x, y, z, time, elecField):
        return self.numericalCalc(x, y, z, elecField)
