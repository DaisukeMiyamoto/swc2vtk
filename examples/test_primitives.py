# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:49:53 2016

@author: nebula
"""
import swc2vtk

# outputpos = '/home/nebula/work/paraview/primitives/'
outputpos = ''
filename = 'primitive.vtk'
vtkgen = swc2vtk.VtkGenerator()

# vtkgen.add_cube()
# vtkgen.add_cylinder(2.0, 0.0, 0.0)
# vtkgen.add_cube(0, 5, 0, 2.0)
# vtkgen.add_sphere()
vtkgen.add_sphere()

vtkgen.write_vtk(outputpos + filename)
