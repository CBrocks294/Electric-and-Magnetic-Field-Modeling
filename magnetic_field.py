# AUTHOR: CHRISTOPHER BROCKLEBANK

import vector_field
import vector


class MagneticField(vector_field.VectorField):
    def __init__(self, size):
        super().__init__(size)

    def changeVector(self, x, y, z, elecField):
        changeX = (self.deltaFieldZBydeltaY(x, y, z, elecField) - self.deltaFieldYBydeltaZ(x, y, z, elecField))*self.deltaTime
        changeY = (self.deltaFieldXBydeltaZ(x, y, z, elecField) - self.deltaFieldZBydeltaX(x, y, z, elecField))*self.deltaTime
        changeZ = (self.deltaFieldYBydeltaX(x, y, z, elecField) - self.deltaFieldXBydeltaY(x, y, z, elecField))*self.deltaTime
        return vector.Vector(changeX, changeY, changeZ)