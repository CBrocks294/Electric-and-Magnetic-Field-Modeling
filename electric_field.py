import vector_field


class ElectricField(vector_field.VectorField):
  def __init__(self, size):
    super().__init__(size)

  def calculateField(self):
    pass