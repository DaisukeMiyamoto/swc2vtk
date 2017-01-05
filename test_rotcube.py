# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:49:53 2016

@author: nebula
"""
import numpy as np
from swc2vtk.swc2vtk import VtkGenerator

if __name__ == '__main__':

    filename = 'rot_cube.vtk'
    vtkgen = VtkGenerator()
    
    pi = 3.141592
    # pos = np.array([[0, 0, 0], [0, 2, 0], [4, 2, 0], [5, 5, 5], [8, 8, 8]])
    pos = np.array([[0, 0, 0], [0, 2, 0], [4, 2, 0], [5, 5, 5], [8, 8, 8], [6, 6, 6], [4, 6, 6], [4, 4, 6]])
    # pos = np.array([[0, 0, 0], [0, 2, 0], [4, 2, 0], [5, 5, 0], [8, 8, 0]])
    
    for i in range(pos.shape[0]-1):
        print str(pos[i]) + ' to ' + str(pos[i+1])
        vtkgen.add_cuboid_p2p(pos[i], pos[i+1], 0.2*i+0.3, 0.2*i)

    vtkgen.write_vtk(filename)
