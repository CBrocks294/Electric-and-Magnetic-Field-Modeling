# AUTHOR: CHRISTOPHER BROCKLEBANK

import math
import vector
import vector_field


class ElectricField(vector_field.VectorField):
    def __init__(self, size):
        super().__init__(size)
        self.ELEC_CONST = 8.8541878128(13) / (10 ** 12)
        self.VAC_CONST = 4 * math.pi / (10 ** 7)

    def changeVector(self, x, y, z, magField):
        changeX = (self.deltaFieldZBydeltaY(x, y, z, magField) - self.deltaFieldYBydeltaZ(x, y, z,
                                                                                          magField)) * self.deltaTime
        changeY = (self.deltaFieldXBydeltaZ(x, y, z, magField) - self.deltaFieldZBydeltaX(x, y, z,
                                                                                          magField)) * self.deltaTime
        changeZ = (self.deltaFieldYBydeltaX(x, y, z, magField) - self.deltaFieldXBydeltaY(x, y, z,
                                                                                          magField)) * self.deltaTime
        return vector.Vector(changeX, changeY, changeZ)
