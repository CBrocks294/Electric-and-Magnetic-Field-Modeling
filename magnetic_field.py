import vector_field
import electric_field


class MagneticField(vector_field.VectorField):
  def __init__(self, size):
    super().__init__(size)

  def calculateField(self):
    pass