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

for i, filename in enumerate(filelist):
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'))
    vtkgen.write_vtk(os.path.join(output_dir, filename + '.vtk'), radius_data=True, normalize_diam=True)

for i, filename in enumerate(filelist):
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc(os.path.join(input_dir, filename + '.swc'), inv_x=True, shift_x=1024.0)
    vtkgen.write_vtk(os.path.join(output_dir, filename + '_flip.vtk'), radius_data=True, normalize_diam=True)
