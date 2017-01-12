# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:49:53 2016

@author: nebula
"""
import numpy as np
from swc2vtk.swc2vtk import VtkGenerator

outputpos = '/home/nebula/work/paraview/primitives/'
filename = 'primitive.vtk'
vtkgen = VtkGenerator()

# vtkgen.add_cube()
# vtkgen.add_cylinder(2.0, 0.0, 0.0)
# vtkgen.add_cube(0, 5, 0, 2.0)
vtkgen.add_sphere()

vtkgen.write_vtk(outputpos + filename)
