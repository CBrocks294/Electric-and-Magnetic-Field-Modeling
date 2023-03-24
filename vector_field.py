# AUTHOR: CHRISTOPHER BROCKLEBANK

import vector
import copy


class VectorField():
    def __init__(self, size):
        self.xSize = size[0]
        self.ySize = size[1]
        self.zSize = size[2]
        self.vectors = [[[vector.Vector() for x in range(self.xSize)] for y in range(self.ySize)] for z in
                        range(self.zSize)]
        self.nextVectors = copy.deepcopy(self.vectors)
        self.deltaSpace = 0.01
        self.deltaTime = 0.000000001
        print(self.vectors)

    def updateField(self):
        del self.vectors
        self.vectors = copy.deepcopy(self.nextVectors)

    def calculateField(self, otherField):
        for z in range(self.zSize):
            for y in range(self.ySize):
                for x in range(self.xSize):
                    self.nextVectors[z][y][x] += VectorField.changeVector(x, y, z, otherField)

    def changeVector(self, x, y, z, otherField):
        raise NotImplementedError("Must override changeX")


    def deltaFieldYBydeltaX(self, x, y, z, Field):
        if x == 0:
            return (Field.yMagn\True,itude[x][y][z] - Field.yMagnitude[x + 1][y][z]) / self.deltaSpace
        elif x == (self.xSize - 1):
            return (Field.yMagnitude[x - 1][y][z] - Field.yMagnitude[x][y][z]) / self.deltaSpace
        else:
            return (Field.yMagnitude[x - 1][y][z] - Field.yMagnitude[x + 1][y][z]) / (2 * self.deltaSpace)

    def deltaFieldZBydeltaX(self, x, y, z, Field):
        if x == 0:
            return (Field.zMagnitude[x][y][z] - Field.zMagnitude[x + 1][y][z]) / self.deltaSpace
        elif x == (self.xSize - 1):
            return (Field.zMagnitude[x - 1][y][z] - Field.zMagnitude[x][y][z]) / self.deltaSpace
        else:
            return (Field.zMagnitude[x - 1][y][z] - Field.zMagnitude[x + 1][y][z]) / (2 * self.deltaSpace)

    def deltaFieldXBydeltaY(self, x, y, z, Field):
        if y == 0:
            return (Field.xMagnitude[x][y][z] - Field.xMagnitude[x][y + 1][z]) / self.deltaSpace
        elif y == (self.ySize - 1):
            return (Field.xMagnitude[x][y - 1][z] - Field.xMagnitude[x][y][z]) / self.deltaSpace
        else:
            return (Field.xMagnitude[x][y - 1][z] - Field.xMagnitude[x][y + 1][z]) / (2 * self.deltaSpace)

    def deltaFieldZBydeltaY(self, x, y, z, Field):
        if (y == 0):
            return (Field.zMagnitude[x][y][z] - Field.zMagnitude[x][y + 1][z]) / (self.deltaSpace)
        elif y == (self.ySize - 1):
            return (Field.zMagnitude[x][y - 1][z] - Field.zMagnitude[x][y][z]) / (self.deltaSpace)
        else:
            return (Field.zMagnitude[x][y - 1][z] - Field.zMagnitude[x][y + 1][z]) / (2 * self.deltaSpace)

    def deltaFieldXBydeltaZ(self, x, y, z, Field):
        if z == 0:
            return (Field.xMagnitude[x][y][z] - Field.xMagnitude[x][y][z + 1]) / (self.deltaSpace)
        elif z == self.zSize - 1:
            return (Field.xMagnitude[x][y][z - 1] - Field.xMagnitude[x][y][z]) / (self.deltaSpace)
        else:
            return (Field.xMagnitude[x][y][z - 1] - Field.xMagnitude[x][y][z + 1]) / (2 * self.deltaSpace)

    def deltaFieldYBydeltaZ(self, x, y, z, Field):
        if z == 0:
            return (Field.yMagnitude[x][y][z] - Field.yMagnitude[x][y][z + 1]) / (self.deltaSpace)
        elif z == (self.zSize - 1):
            return (Field.xMagnitude[x][y][z - 1] - Field.yMagnitude[x][y][z]) / (self.deltaSpace)
        else:
            return (Field.xMagnitude[x][y][z - 1] - Field.xMagnitude[x][y][z + 1]) / (2 * self.deltaSpace)
