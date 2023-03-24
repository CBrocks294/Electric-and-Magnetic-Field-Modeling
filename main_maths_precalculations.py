# AUTHOR: CHRISTOPHER BROCKLEBANK

import electric_field
import magnetic_field
import time as t


def main():
    XSIZE = 100
    YSIZE = 100
    ZSIZE = 100
    size = (XSIZE, YSIZE, ZSIZE)
    electricfield = electric_field.ElectricField(size)
    magneticfield = magnetic_field.MagneticField(size)
    endTime = 100
    for time in range(endTime):
        # calculate how field change
        start = t.time()
        electricfield.calculateField(magneticfield, time)
        magneticfield.calculateField(electricfield, time)
        electricfield.updateField()
        magneticfield.updateField()
        print("iter: " + str(time) + " Time taken: " + str(t.time()-start))

        # save changes to sql DB
        pass


main()
