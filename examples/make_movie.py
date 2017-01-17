# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
from swc2vtk.vtkgenerator import VtkGenerator


# def test_swc_movie(stoptime=10.0):
#     filename_base = os.path.join('movie1', 'swc_cuboid%d.vtk')
#     datafile_base = os.path.join('/home', 'nebula', 'git', 'neuron_samples', 'simple', 'result', 't%.6f.dat')
#     datastep = 0.25
#
#     vtkgen = VtkGenerator()
#
#     vtkgen.add_swc(os.path.join('swc', 'Swc_BN_1056.swc'))
#
#     nstep = int(stoptime / datastep)
#
#     for i in range(0, nstep):
#         datafile = datafile_base % (i * datastep)
#         print('t = %f (%s)' % (i * datastep, datafile))
#
#         vtkgen.write_vtk(filename_base % i, datatitle='simulation', datafile=datafile)

def test_stdbrain_movie(vtkfile_base, datafile_base, swcfilename, stoptime=10.0, datastep=0.25):
    vtkgen = VtkGenerator()
    vtkgen.add_swc(swcfilename, diam_ratio=0.5)

    nstep = int(stoptime / datastep)
    for i in range(0, nstep):
        datafile = datafile_base % (i * datastep)
        print('t = %f (%s)' % (i * datastep, datafile))
        vtkgen.clear_datafile()
        vtkgen.add_datafile(datafile)

        vtkgen.write_vtk(vtkfile_base % i, datatitle='simulation')


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

# for i, name in enumerate(cellname_list):
#     vtkfile_base = '/home/nebula/work/paraview/sb_movie20170110/c' + str(i) + '_%d.vtk'
#     datafile_base = '/home/nebula/work/record/paraswc/output/c' + str(i) + '_t%.6f.txt'
#     swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '.swc'
#
#     test_stdbrain_movie(vtkfile_base, datafile_base, swcfilename, stoptime=40, datastep=0.1)
#
# for i, name in enumerate(cellname_list):
#     vtkfile_base = '/home/nebula/work/paraview/sb_movie20170110/c' + str(i + len(cellname_list)) + '_%d.vtk'
#     datafile_base = '/home/nebula/work/record/paraswc/output/c' + str(i + len(cellname_list)) + '_t%.6f.txt'
#     swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '_flip.swc'
#
#     test_stdbrain_movie(vtkfile_base, datafile_base, swcfilename, stoptime=40, datastep=0.1)


stoptime = 20.0
datastep = 0.1
nstep = int(stoptime / datastep)

vtkgen = VtkGenerator()
for j, name in enumerate(cellname_list):
    swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '.swc'
    print('Processing %s' % swcfilename)
    vtkgen.add_swc(swcfilename, diam_ratio=0.5)
    swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '_flip.swc'
    print('Processing %s' % swcfilename)
    vtkgen.add_swc(swcfilename, diam_ratio=0.5)

for i in range(0, nstep):
    print('t = %f/%f' % (i * datastep, stoptime))
    vtkgen.clear_datafile()
    for j, name in enumerate(cellname_list):
        datafile_base = '/home/nebula/work/record/paraswc/output/c' + str(j) + '_t%.6f.txt'
        datafile = datafile_base % (i * datastep)
        vtkgen.add_datafile(datafile)

        datafile_base = '/home/nebula/work/record/paraswc/output/c' + str(j + len(cellname_list)) + '_t%.6f.txt'
        datafile = datafile_base % (i * datastep)
        vtkgen.add_datafile(datafile)

    vtkfile_base = '/home/nebula/work/paraview/sb_movie20170110/all2_%d.vtk'
    vtkgen.write_vtk(vtkfile_base % i, datatitle='simulation')


# test_swc_movie(100)
