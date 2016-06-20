# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:00:41 2016

@author: nebula
"""

import os
from swc2vtk import VtkGenerator

filename_list = ['Swc_BN_1056', '0655regist', '0661regist',
                 '0663regist', '0664regist', '0965regist', '0969regist',
                 '0970regist', '0973regist', '0984regist',
                 '0986regist', '0988', '1020']

for filename in filename_list:
    print 'Processing: %s' % filename
    vtkgen = VtkGenerator()
    vtkgen.add_swc(os.path.join('swc', filename+'.swc'))                
    vtkgen.write_vtk(filename+'.vtk')

