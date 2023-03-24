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

    def updateField(self):
        del self.vectors
        self.vectors = copy.deepcopy(self.nextVectors)

    def calculateField(self, otherField, time):
        for z in range(self.zSize):
            for y in range(self.ySize):
                for x in range(self.xSize):
                    self.nextVectors[z][y][x] += self.changeVector(x, y, z, time, otherField)

    def changeVector(self, x, y, z, time, otherField):
        raise NotImplementedError("Must override changeX")

    def numericalCalc(self, x, y, z, field):
        changeX = (self.deltaFieldZBydeltaY(x, y, z, field) - self.deltaFieldYBydeltaZ(x, y, z, field)) * self.deltaTime
        changeY = (self.deltaFieldXBydeltaZ(x, y, z, field) - self.deltaFieldZBydeltaX(x, y, z, field)) * self.deltaTime
        changeZ = (self.deltaFieldYBydeltaX(x, y, z, field) - self.deltaFieldXBydeltaY(x, y, z, field)) * self.deltaTime
        return vector.Vector(changeX, changeY, changeZ)

    def deltaFieldXBydeltaX(self, x, y, z, Field):
        if x == 0:
            return (Field.vectors[x][y][z].xMagnitude - Field.vectors[x + 1][y][z].xMagnitude) / self.deltaSpace
        elif x == (self.xSize - 1):
            return (Field.vectors[x - 1][y][z].xMagnitude - Field.vectors[x][y][z].xMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x - 1][y][z].xMagnitude - Field.vectors[x + 1][y][z].xMagnitude) / (2 * self.deltaSpace)

    def deltaFieldYBydeltaX(self, x, y, z, Field):
        if x == 0:
            return (Field.vectors[x][y][z].yMagnitude - Field.vectors[x + 1][y][z].yMagnitude) / self.deltaSpace
        elif x == (self.xSize - 1):
            return (Field.vectors[x - 1][y][z].yMagnitude - Field.vectors[x][y][z].yMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x - 1][y][z].yMagnitude - Field.vectors[x + 1][y][z].yMagnitude) / (2 * self.deltaSpace)

    def deltaFieldZBydeltaX(self, x, y, z, Field):
        if x == 0:
            return (Field.vectors[x][y][z].zMagnitude - Field.vectors[x + 1][y][z].zMagnitude) / self.deltaSpace
        elif x == (self.xSize - 1):
            return (Field.vectors[x - 1][y][z].zMagnitude - Field.vectors[x][y][z].zMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x - 1][y][z].zMagnitude - Field.vectors[x + 1][y][z].zMagnitude) / (2 * self.deltaSpace)

    def deltaFieldXBydeltaY(self, x, y, z, Field):
        if y == 0:
            return (Field.vectors[x][y][z].xMagnitude - Field.vectors[x][y + 1][z].xMagnitude) / self.deltaSpace
        elif y == (self.ySize - 1):
            return (Field.vectors[x][y - 1][z].xMagnitude - Field.vectors[x][y][z].xMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x][y - 1][z].xMagnitude - Field.vectors[x][y + 1][z].xMagnitude) / (2 * self.deltaSpace)

    def deltaFieldZBydeltaY(self, x, y, z, Field):
        if y == 0:
            return (Field.vectors[x][y][z].zMagnitude - Field.vectors[x][y + 1][z].zMagnitude) / self.deltaSpace
        elif y == (self.ySize - 1):
            return (Field.vectors[x][y - 1][z].zMagnitude - Field.vectors[x][y][z].zMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x][y - 1][z].zMagnitude - Field.vectors[x][y + 1][z].zMagnitude) / (2 * self.deltaSpace)

    def deltaFieldXBydeltaZ(self, x, y, z, Field):
        if z == 0:
            return (Field.vectors[x][y][z].xMagnitude - Field.vectors[x][y][z + 1].xMagnitude) / self.deltaSpace
        elif z == (self.zSize - 1):
            return (Field.vectors[x][y][z - 1].xMagnitude - Field.vectors[x][y][z].xMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x][y][z - 1].xMagnitude - Field.vectors[x][y][z + 1].xMagnitude) / (2 * self.deltaSpace)

    def deltaFieldYBydeltaZ(self, x, y, z, Field):
        if z == 0:
            return (Field.vectors[x][y][z].yMagnitude - Field.vectors[x][y][z + 1].yMagnitude) / self.deltaSpace
        elif z == (self.zSize - 1):
            return (Field.vectors[x][y][z - 1].yMagnitude - Field.vectors[x][y][z].yMagnitude) / self.deltaSpace
        else:
            return (Field.vectors[x][y][z - 1].yMagnitude - Field.vectors[x][y][z + 1].yMagnitude) / (2 * self.deltaSpace)

