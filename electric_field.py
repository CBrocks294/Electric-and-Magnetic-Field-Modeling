# AUTHOR: CHRISTOPHER BROCKLEBANK

import math
import vector
import vector_field
import wire


class ElectricField(vector_field.VectorField):
    def __init__(self, size):
        super().__init__(size)
        self.ELEC_CONST = 8.854187812813 / (10 ** 12)
        self.MAG_CONST = 4 * math.pi / (10 ** 7)
        self.wire = wire.Wire(10000, 3, 0.02, 0.1, 0.02, 0.5, 0.2, 0.6)

    def changeVector(self, x, y, z, time, magField):
        changevector = self.numericalCalc(x, y, z, magField)
        changevector = changevector / self.MAG_CONST
        changevector -= self.wire.fluxVector(time,
                                             (x - (self.xSize / 2)) * self.deltaSpace,
                                             (y - (self.ySize / 2)) * self.deltaSpace,
                                             z * self.deltaSpace)
        changevector = changevector / self.ELEC_CONST
        return changevector
