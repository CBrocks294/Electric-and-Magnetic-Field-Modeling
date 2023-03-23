import vector_field
import magnetic_field


class ElectricField(vector_field.VectorField):
    def __init__(self, size):
        super().__init__(size)
        dSpace = 0.01
        dTime = 0.000000001

    def calculateField(self, magneticField):
        for z in range(magneticField.zSize):
            for y in range(magneticField.ySize):
                for x in range(magneticField.xSize):
                    # differential of Magnetic field with respects to space
                    print(magneticField.vectors[z][y][x])

