# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:49:53 2016

@author: nebula
"""
import numpy as np
from swc2vtk import VtkGenerator

if __name__ == '__main__':

    filename = 'rot_cube.vtk'
    vtkgen = VtkGenerator()
    
    pi = 3.141592
    pos = np.array([[0, 0, 0], [0, 2, 0], [4, 2, 0], [5, 5, 5], [8, 8, 8]])
    #pos = np.array([[0, 0, 0], [0, 2, 0], [4, 2, 0], [5, 5, 0], [8, 8, 0]])
    
    for i in range(pos.shape[0]-1):
        print str(pos[i]) + ' to ' + str(pos[i+1])
        
        local_pos = pos[i+1] - pos[i]
        print local_pos
        
        rot_y = -np.arctan(local_pos[2] / local_pos[0])
        rot_z = -np.arctan(np.sqrt(local_pos[0]**2 + local_pos[2]**2) / local_pos[1])
        len = np.sqrt(local_pos[0]**2 + local_pos[1]**2 + local_pos[2]**2)

        vtkgen.add_cuboid(pos[i][0], pos[i][1], pos[i][2], 1.0, len, 1.0, rot_y, rot_z, 0.2 * i)

    
    #for i in range(10):
    #    vtkgen.add_cuboid(i*5, 0, 0, 1.0, 2.0*i, 1.0, pi*i/32.0, 0.0, 0.1 * i)



    vtkgen.write_vtk(filename)
    
    
    