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

for i in range(4):
    vtkgen.set_draw_mode(i)
    vtkgen.write_vtk(os.path.join(outputpos, filename + '_draw'+str(i)+'.vtk'))

