# -*- coding: utf-8 -*-
import os
import swc2vtk

inputfile = 'swc/200000.swc'
output_dir = '/home/nebula/work/paraview/test_annotation20170126/'
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc(inputfile)
vtkgen.add_swc_mark(0, 10, 5, data=0.8)
vtkgen.add_swc_connection(0, 100, 0, 1214, 5, data=2)
vtkgen.write_vtk(os.path.join(output_dir, '200000.vtk'))
vtkgen.write_annotation_vtk(os.path.join(output_dir, '200000_ano.vtk'))
