# -*- coding: utf-8 -*-

import os
import datetime
import examples.swcfilelist
import swc2vtk


input_dir = '/home/nebula/git/LAL-VPCmapping/swc'
output_dir = '/home/nebula/git/LAL-VPCmapping/swc'
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

file_list = examples.swcfilelist.filelist_all

for i, filename in enumerate(file_list):
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'), inv_x=True, shift_x=1024.0)
    vtkgen.write_swc(os.path.join(output_dir, filename + '_flip.swc'),
                     comment='swc2vtk flip' + str(datetime.date.today()))
