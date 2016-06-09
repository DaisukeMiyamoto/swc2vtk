# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:37:20 2016

@author: nebula
"""

import os
from swc import Swc

class VtkGenerator():
    header_base = '''\
# vtk DataFile Version 3.0
VTK Example Cube
ASCII
DATASET UNSTRUCTURED_GRID
'''

    def __init__(self):
        self.stoptime = 100
        self.header = self.header_base
        
        self.point_list = []
        self.cell_list = []


    def add_point(self, x, y, z):
        self.point_list.append([x, y, z])
        

    def add_cube(self, x=0, y=0, z=0, data=1.0):
        point_start = len(self.point_list)
        points = [0, 1, 2, 3, 4, 5, 6, 7]
        points = [i+point_start for i in points]
        
        self.point_list.append((0+x, 0+y, 0+z))
        self.point_list.append((1+x, 0+y, 0+z))
        self.point_list.append((1+x, 1+y, 0+z))
        self.point_list.append((0+x, 1+y, 0+z))
        self.point_list.append((0+x, 0+y, 1+z))
        self.point_list.append((1+x, 0+y, 1+z))
        self.point_list.append((1+x, 1+y, 1+z))
        self.point_list.append((0+x, 1+y, 1+z))
        cell = {'type':12, 'points':points, 'data':data}
        
        self.cell_list.append(cell)

    def add_swc(self, swc_filename):
        swc = Swc(swc_filename)
        for (i, record) in enumerate(swc.data):
            self.add_cube(record['pos'][0], record['pos'][1], record['pos'][2], float(i)/len(swc.data) )

    

    def _point2text(self):
        text = 'POINTS %d float\n' % (len(self.point_list))
        for point in self.point_list:
            text += '%f %f %f\n' % (point[0], point[1], point[2])
            
        return text
    

    def _cell2text(self):
        num_data = sum([len(cell['points'])+1 for cell in self.cell_list])
        
        text = '\nCELLS %d %d\n' % (len(self.cell_list), num_data)
        for cell in self.cell_list:
            text += str(len(cell['points']))
            for x in cell['points']:
                text += ' '+str(x)

            text += '\n'

        text += '\nCELL_TYPES %d\n' % (len(self.cell_list))
        for cell in self.cell_list:
            text += str(cell['type'])+'\n'

        text += '\nCELL_DATA %d\n' % (len(self.cell_list))
        text += 'SCALARS data float 1\n'
        text += 'LOOKUP_TABLE default\n'
        for cell in self.cell_list:
            text += str(cell['data'])+'\n'
        
        return text


    def write_vtk(self, filename):

        vtkdata = ''
        vtkdata += self.header
        vtkdata += self._point2text()
        vtkdata += self._cell2text()
        print vtkdata        
        
        with open (filename, 'w') as file:
            file.write(vtkdata)
            

    def show_state(self):
        print self.point_list
        print self.cell_list

if __name__ == '__main__':

    filename = 'swc.vtk'
    vtkgen = VtkGenerator()
    
    #for i in range(10):
    #    vtkgen.add_cube(i, i, 0, i*0.1)
        
    #vtkgen.add_swc(os.path.join('data', 'simple.swc'))
    vtkgen.add_swc(os.path.join('data', 'Swc_BN_1056.swc'))

        
    vtkgen.write_vtk(filename)
    vtkgen.show_state()
