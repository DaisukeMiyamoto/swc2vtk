# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:00:41 2016

@author: nebula
"""

import os
import swc2vtk


filelist_simple = [
    'simple',
    'simple',
    'simple',
    'simple'
]

filelist_small = [
    '0664_regist',
    '0965_regist',
    '0970_regist'
]

filelist_small2 = [
    'Swc_BN_1056',
    '200000',
    '300000',
    '301000',
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
    '0966_regist',
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


input_dir = '/home/nebula/git/LAL-VPCmapping/converted_swc'
output_dir = '/home/nebula/work/paraview/standardbrain_colored20170125/'

# filelist = filelist_small
filelist = filelist_all
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

for i, filename in enumerate(filelist):
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'))
    vtkgen.write_vtk(os.path.join(output_dir, filename + '.vtk'), radius_data=True, type_data=True)


vtkgen = swc2vtk.VtkGenerator()
for filename in filelist:
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'))
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'), inv_x=True, shift_x=1024.0)

vtkgen.write_vtk(os.path.join(output_dir, 'all_normalize2.vtk'), coloring=True, normalize_diam=True, radius_data=True, type_data=True)
