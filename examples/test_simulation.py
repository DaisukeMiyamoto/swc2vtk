# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
import swc2vtk
from tqdm import tqdm


cellname_list = [
    '200000',
    '300000',
    '301000',
    ]

stoptime = 1000.0
datastep = 0.25
nstep = int(stoptime / datastep)

for cellname in cellname_list:
    vtkfile_base = os.path.join('/data/vtk_data/arase_simulation_5571105', 'vtk', cellname + '_%d.vtk')
    swcfilename = os.path.join('swc', cellname + '.swc')
    datafile_base = os.path.join('/data/vtk_data/arase_simulation_5571105', 'data', cellname, cellname + 't%.6f.dat')

    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.set_draw_mode(3)
    vtkgen.add_swc(swcfilename)

    for i in tqdm(range(1, nstep), desc='Generating VTK'):
        vtkgen.clear_datafile()
        datafile = datafile_base % (i * datastep)
        vtkgen.add_datafile(datafile)

        vtkgen.write_vtk(vtkfile_base % i, datatitle='simulation')

