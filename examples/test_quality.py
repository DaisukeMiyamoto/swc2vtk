# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:00:41 2016

@author: nebula
"""
import os
from swc2vtk.vtkgenerator import VtkGenerator

filename = 'simple'
outputpos = ''

vtkgen = VtkGenerator()
vtkgen.add_swc(os.path.join('swc', filename + '.swc'))
vtkgen.write_vtk(os.path.join(outputpos, filename + '_draw0.vtk'), draw_mode=0)

vtkgen = VtkGenerator()
vtkgen.add_swc(os.path.join('swc', filename + '.swc'))
vtkgen.write_vtk(os.path.join(outputpos, filename + '_draw1.vtk'), draw_mode=1)

