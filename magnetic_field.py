import vector_field
import electric_field


class MagneticField(vector_field.VectorField):
    def __init__(self, size):
        super().__init__(size)

    def changeVector(self, x, y, z, magField):
        changeX = (self.deltaFieldZBydeltaY(x, y, z, magField) - self.deltaFieldYBydeltaZ(x, y, z, magField))*self.deltaTime
        changeY = (self.deltaFieldXBydeltaZ(x, y, z, magField) - self.deltaFieldZBydeltaX(x, y, z, magField))*self.deltaTime
        changeZ = (self.deltaFieldYBydeltaX(x, y, z, magField) - self.deltaFieldXBydeltaY(x, y, z, magField))*self.deltaTime
        return vector.Vector(changeX, changeY, changeZ)