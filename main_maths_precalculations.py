import electric_field
import magnetic_field
import vector
def main():
    a = vector.Vector()
    b = vector.Vector()
    c = a+b
    print(c.xMagnitude)
    XSIZE = 10
    YSIZE=10
    ZSIZE = 10
    size = (XSIZE, YSIZE, ZSIZE)
    electricfield = electric_field.ElectricField(size)
    magneticfield = magnetic_field.MagneticField(size)
    endTime = 100000000
    for time in range(endTime):
        #calculate how field change
        electricfield.calculateField()
        magneticfield.calculateField()
        electricfield.updateField()
        magneticfield.updateField()

        #save changes to sql DB
        pass
main()