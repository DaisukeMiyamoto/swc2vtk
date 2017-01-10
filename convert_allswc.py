# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:00:41 2016

@author: nebula
"""

import os
from swc2vtk.swc2vtk import VtkGenerator

filelist_simple = [
    'simple',
    'simple',
    'simple',
    'simple'
]

filelist_small = [
    '0993_regist',
]

filelist_all = [
    '0004_regist',
    '0005_regist',
    '0008_regist',
    '0009_regist',
    '0012_regist',
    '0017_regist',
    '0019_regist',
    '0021_regist',
    '0655_regist',
    '0661_regist',
    '0663_regist',
    '0664_regist',
    '0965_regist',
    # '0966_regist',
    '0967_regist',
    '0969_regist',
    '0970_regist',
    '0973_regist',
    '0984_regist',
    '0986_regist',
    '0988_regist',
    '0993_regist',
    '1009_regist',
    '1020_regist',
    '1068_regist',
    '1080_regist',
    '090815_4_sn_reg'
    ]

outputpos = '/home/nebula/work/paraview/standardbrain20170107/'
# filelist = filelist_small
filelist = filelist_all

# for i, filename in enumerate(filelist):
#     print 'Processing: %s' % filename
#     fixval = int(i * (256 / len(filelist)))
#     vtkgen = VtkGenerator()
#     vtkgen.add_swc(os.path.join('swc', filename + '.swc'))
#     vtkgen.write_vtk(outputpos + filename + '.vtk')
#
# for i, filename in enumerate(filelist):
#     print 'Processing: %s' % filename
#     fixval = int(i * (256 / len(filelist)))
#     vtkgen = VtkGenerator()
#     vtkgen.add_swc(os.path.join('swc', filename + '.swc'), inv_x=True, shift_x=1024.0)
#     vtkgen.write_vtk(outputpos + filename + '_flip.vtk')


vtkgen = VtkGenerator()
for filename in filelist:
    print 'Processing: %s' % filename
    vtkgen.add_swc(os.path.join('swc', filename + '.swc'), normalize_diam=True)

vtkgen.write_vtk(outputpos + 'all_normalize2.vtk', coloring=True)

vtkgen = VtkGenerator()
for filename in filelist:
    print 'Processing: %s' % filename
    vtkgen.add_swc(os.path.join('swc', filename + '.swc'), inv_x=True, shift_x=1024.0, normalize_diam=True)

vtkgen.write_vtk(outputpos + 'all_flip_normalize2.vtk', coloring=True)
