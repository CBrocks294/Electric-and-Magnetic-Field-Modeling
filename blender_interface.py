# AUTHOR: CARA THOMPSON

import bpy
import math 
import random

def CreateGrid(dist, n, r): # dist=the distance between the origins of adjecent spheres, n=the number of spheres in a line (odd), r=radius of spheres
    
    distFromCentre = ((n-1)//2)*dist
    
    for x in range(-distFromCentre, distFromCentre+dist, dist):
        for y in range(-distFromCentre, distFromCentre+dist, dist):
            for z in range(-distFromCentre, distFromCentre+dist, dist):
    
                bpy.ops.mesh.primitive_ico_sphere_add(radius=r, location=(x, y, z))  
                
def CreateArrowGrid(dist, n, r): # dist=the distance between the origins of adjecent spheres, n=the number of spheres in a line (odd), r=radius of spheres
    
    distFromCentre = ((n-1)//2)*dist
    
    #arrow = bpy.context.scene.objects["arrow"]
    i=1
    
    bpy.data.objects["arrow"].select_set(True)
    
    for z in range(-distFromCentre, distFromCentre+dist, dist):
        for y in range(-distFromCentre, distFromCentre+dist, dist):
            for x in range(-distFromCentre, distFromCentre+dist, dist):
    
                bpy.ops.object.duplicate()
                if i<10:
                    arrows[i-1] = bpy.data.objects["arrow.00"+str(i)]
                elif i<100:
                    arrows[i-1] = bpy.data.objects["arrow.0"+str(i)]
                else:
                    arrows[i-1] = bpy.data.objects["arrow."+str(i)]
                arrows[i-1].location = (x,y,z)
                i+=1

def RotateArrows(l): # l is the list of magnitudes in the x,y,z directions
    i=0
    for z in l:
        for y in z:
            for x in y:
                yRotation = math.atan( x[1][2] / x[1][0] )
                zRotation = math.atan( x[1][1] / x[1][0] )
                print(yRotation)
                print(zRotation)
                
                arrows[i].rotation_euler[1] = yRotation
                arrows[i].rotation_euler[2] = zRotation
                i+=1


#CreateGrid(1, 7, 0.1)

mainList = [[[]for y in range(7)] for z in range(7)]
for z in mainList:
    for y in z:
        for x in y:
            x.append([[random.random(), random.random(), random.random()],[random.random()/2, random.random()/2, random.random()/2]])
maxE = 1
maxB = 0.5


print(mainList)

arrows = [0]*343
CreateArrowGrid(1,7,0.1)
RotateArrows(mainList)