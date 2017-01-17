# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
import swc2vtk


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

vtkgen = swc2vtk.VtkGenerator()
for j, name in enumerate(cellname_list):
    swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '.swc'
    print('Processing %s' % swcfilename)
    vtkgen.add_swc(swcfilename)
    swcfilename = '/home/nebula/work/data/test1220/' + name + '/' + name + '_flip.swc'
    print('Processing %s' % swcfilename)
    vtkgen.add_swc(swcfilename)

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
