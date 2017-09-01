# -*- coding: utf-8 -*-

import os
import swc2vtk
import swcfilelist


# input_dir = '/home/nebula/git/LAL-VPCmapping/converted_swc'
input_dir = './swc'
output_dir = '/home/nebula/work/paraview/standardbrain20170131/'
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

filelist = swcfilelist.filelist_lalvpc

vtkgen = swc2vtk.VtkGenerator()
for filename in filelist:
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'))
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'), inv_x=True, shift_x=1024.0)

vtkgen.write_vtk(os.path.join(output_dir, 'all.vtk'), coloring=True, normalize_diam=True, radius_data=True)
