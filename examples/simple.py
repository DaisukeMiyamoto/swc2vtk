import swc2vtk

vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('../swc/Swc_BN_1056.swc')
vtkgen.write_vtk('bn1056.vtk')
