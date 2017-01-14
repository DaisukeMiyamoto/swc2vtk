# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
from swc2vtk.vtkgenerator import VtkGenerator


cellname = '300000'
vtkfile_base = os.path.join('..', 'vtk_data', cellname, cellname+'_%d.vtk')

stoptime = 1000.0
datastep = 0.25
nstep = int(stoptime / datastep)

vtkgen = VtkGenerator()
vtkgen.set_draw_mode(3)
swcfilename = os.path.join('swc', cellname + '.swc')
vtkgen.add_swc(swcfilename)

for i in range(1, nstep):
    vtkgen.clear_datafile()

    datafile_base = os.path.join('..', 'data', cellname, cellname + 't%.6f.dat')
    datafile = datafile_base % (i * datastep)
    vtkgen.add_datafile(datafile)

    vtkgen.write_vtk(vtkfile_base % i, datatitle='simulation')

