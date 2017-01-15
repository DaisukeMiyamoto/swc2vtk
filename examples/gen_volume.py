# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:52:38 2016

@author: nebula
"""

import os
from swc2vtk.vtkgenerator import VtkGenerator


filelist_small = [
    '0004_regist',
    '0005_regist',
    '0008_regist',
    '0009_regist',
    '0012_regist',
    '0017_regist',
    '0986_regist',
]

filelist_small2 = [
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

filelist = filelist_small
vtkfilename = 'volume_all.vtk'

vtkgen = VtkGenerator()
for filename in filelist:
    vtkgen.add_swc(os.path.join('swc', filename + '.swc'))

vtkgen.write_volume_vtk(vtkfilename, origin=(0.0, 0.0, 0.0), ratio=(4.0, 4.0, 4.0), div=(256, 256, 77))
