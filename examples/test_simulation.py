# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
from swc2vtk.vtkgenerator import VtkGenerator
from tqdm import tqdm


cellname_list = [
    '200000',
    '300000',
    '301000',
    ]

stoptime = 2000.0
datastep = 0.25
nstep = int(stoptime / datastep)

for cellname in cellname_list:
    vtkfile_base = os.path.join('..', 'vtk_data', cellname, cellname+'_%d.vtk')
    swcfilename = os.path.join('swc', cellname + '.swc')
    datafile_base = os.path.join('..', 'data', cellname, cellname + 't%.6f.dat')

    vtkgen = VtkGenerator()
    vtkgen.set_draw_mode(3)
    vtkgen.add_swc(swcfilename)

    for i in tqdm(range(1, nstep), desc='Generating VTK'):
        vtkgen.clear_datafile()
        datafile = datafile_base % (i * datastep)
        vtkgen.add_datafile(datafile)

        vtkgen.write_vtk(vtkfile_base % i, datatitle='simulation')

