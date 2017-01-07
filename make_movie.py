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
    datastep = 0.25

    vtkgen = VtkGenerator()

    vtkgen.add_swc(os.path.join('swc', 'Swc_BN_1056.swc'))

    nstep = int(stoptime / datastep)

    for i in range(0, nstep):
        datafile = datafile_base % (i * datastep)
        print('t = %f (%s)' % (i * datastep, datafile))

        vtkgen.write_vtk(filename_base % i, datatitle='simulation', datafile=datafile)


def test_stdbrain_movie(vtkfile_base, datafile_base, swcfilename, stoptime=10.0, datastep=0.25):
    vtkgen = VtkGenerator()
    vtkgen.add_swc(swcfilename, diam_ratio=0.5)

    nstep = int(stoptime / datastep)
    for i in range(0, nstep):
        datafile = datafile_base % (i * datastep)
        print('t = %f (%s)' % (i * datastep, datafile))

        vtkgen.write_vtk(vtkfile_base % i, datatitle='simulation', datafile=datafile)


cellname_list = [
    '0655',
    '0661',
    '0663',
    '0664',
    '0965',
    '0969',
    '0970',
    '0973',
    '0986',
    '1009',
    '1020',
    '090604_2',
]

for i, name in enumerate(cellname_list):
    vtkfile_base = '/home/nebula/work/paraview/sb_movie1/c' + str(i) + '_%d.vtk'
    datafile_base = '/home/nebula/work/record/paraswc/output/c' + str(i) + '_t%.6f.txt'
    swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '.swc'

    test_stdbrain_movie(vtkfile_base, datafile_base, swcfilename, stoptime=20, datastep=0.1)

for i, name in enumerate(cellname_list):
    vtkfile_base = '/home/nebula/work/paraview/sb_movie1/c' + str(i + len(cellname_list)) + '_%d.vtk'
    datafile_base = '/home/nebula/work/record/paraswc/output/c' + str(i + len(cellname_list)) + '_t%.6f.txt'
    swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '_flip.swc'

    test_stdbrain_movie(vtkfile_base, datafile_base, swcfilename, stoptime=20, datastep=0.1)


# test_swc_movie(100)
