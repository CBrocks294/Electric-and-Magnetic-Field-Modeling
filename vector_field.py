import vector


class VectorField():
    def __init__(self, size):
        self.vectors = [[[vector.Vector() for x in range(size[1])] for x in range(size[1])] for x in range(size[1])]
        print(self.vectors)