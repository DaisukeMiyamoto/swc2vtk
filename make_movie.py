# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
from swc2vtk.swc2vtk import VtkGenerator


def test_swc_movie(stoptime=10.0):
    filename_base = os.path.join('movie1', 'swc_cuboid%d.vtk')
    datafile_base = os.path.join('/home', 'nebula', 'git', 'neuron_samples', 'simple', 'result', 't%.6f.dat')
    datastart = 0.0
    datastep = 0.25

    vtkgen = VtkGenerator()

    vtkgen.add_swc(os.path.join('swc', 'Swc_BN_1056.swc'))

    nstep = int(stoptime / datastep)

    for i in range(0, nstep):
        datafile = datafile_base % (i * datastep)
        print('t = %f (%s)' % (i * datastep, datafile))

        vtkgen.write_vtk(filename_base % i, datatitle='simulation', datafile=datafile)


test_swc_movie(100)
