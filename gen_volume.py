# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
from swc2vtk.swc2vtk import VtkGenerator

filename = 'simple'
vtkfilename = '/home/nebula/work/paraview/volume/volume1.vtk'

vtkgen = VtkGenerator()
vtkgen.add_swc(os.path.join('swc', filename + '.swc'))
vtkgen.write_volume_vtk(vtkfilename)
