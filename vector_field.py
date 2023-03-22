import vector
import copy

class VectorField():
    def __init__(self, size):
        self.vectors = [[[vector.Vector() for x in range(size[1])] for x in range(size[1])] for x in range(size[1])]
        self.nextVectors = copy.deepcopy(self.vectors)
        print(self.vectors)

    def updateField(self):
        del self.vectors
        self.vectors = copy.deepcopy(self.nextVectors)
