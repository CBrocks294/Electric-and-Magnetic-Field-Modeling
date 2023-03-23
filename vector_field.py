import vector
import copy

class VectorField():
    def __init__(self, size):
        self.xSize = size[0]
        self.ySize = size[1]
        self.zSize = size[2]
        self.vectors = [[[vector.Vector() for x in range(self.xSize)] for y in range(self.ySize)] for z in range(self.zSize)]
        self.nextVectors = copy.deepcopy(self.vectors)
        print(self.vectors)

    def updateField(self):
        del self.vectors
        self.vectors = copy.deepcopy(self.nextVectors)
