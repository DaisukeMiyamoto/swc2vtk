# -*- coding: utf-8 -*-
import os
import swc2vtk

inputfile1 = 'swc/0969_regist.swc'
inputfile2 = 'swc/0664_regist.swc'
output_dir = '/home/nebula/work/paraview/test_annotation20170126/'
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc(inputfile1, inv_x=True, shift_x=1024.0)
vtkgen.add_swc(inputfile2)
vtkgen.add_swc_connection(0, 3177, 1, 4560, 5, data=2)
vtkgen.add_swc_connection(0, 3675, 1, 4485, 5, data=2)
vtkgen.write_vtk(os.path.join(output_dir, 'output_1102.vtk'))
vtkgen.write_annotation_vtk(os.path.join(output_dir, 'output_1102_ano.vtk'))


"""
0986_flip
1020
"""
"""
CellSwc[69] CellSwc[12]
----------
3177 4560 Chemi GABA 1 104
3675 4485 Chemi GABA 1 105
6491 4586 Chemi GABA 2 106
2914 4520 Chemi GABA 1 107
2917 60 Chemi GABA 1 108
1468 31 Chemi GABA 1 109
1459 4464 Chemi GABA 1 110
1440 4562 Chemi GABA 1 111
3249 27 Chemi GABA 1 112
1332 16 Gap nil 1 113
3678 5362 Chemi GABA 1 114
306 4571 Gap nil 1 115
12239 4466 Chemi GABA 1 116
3703 40 Chemi GABA 1 117
3699 5426 Chemi GABA 1 118
317 4492 Chemi GABA 1 119
12304 5327 Chemi GABA 1 120
3698 4579 Chemi GABA 1 121
12067 18 Chemi GABA 1 122
"""
