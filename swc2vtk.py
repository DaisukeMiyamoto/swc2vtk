# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:37:20 2016

@author: nebula
"""

import os
from swc import Swc
import numpy as np

class VtkGenerator():
    header_base = '''\
# vtk DataFile Version 3.0
VTK Example Cube
ASCII
DATASET UNSTRUCTURED_GRID
'''

    def __init__(self):
        self.header = self.header_base
        
        self.swc_list = []
        self.point_list = []
        self.cell_list = []


    def add_point(self, x, y, z):
        self.point_list.append([x, y, z])
        
        
    def _gen_cylinder_point(self, div=20):

        point_list = []
        point_order = []
        
        
        for i in range(div):
            theta = float(i) / div * 2. * np.pi
            point_list.extend([[0, 0, 0], [0, np.cos(theta), np.sin(theta)]])
            
            point_order.extend([len(point_order), len(point_order)+1])

        point_order.extend([0, 1])

        for i in range(div):
            theta = float(i) / div * 2. * np.pi
            point_list.extend([[0, np.cos(theta), np.sin(theta)], [1, np.cos(theta), np.sin(theta)]])
            
            point_order.extend([div*2+i*2, div*2+1+i*2])
      
        point_order.extend([div*2, div*2+1])
      
        for i in range(div):
            theta = float(i) / div * 2. * np.pi
            point_list.extend([[1, 0, 0], [1, np.cos(theta), np.sin(theta)]])
            
            point_order.extend([div*2*2+i*2, div*2*2+1+i*2])

        point_order.extend([div*2*2, div*2*2+1])
      
        return(point_order, np.array(point_list))
        
        
    def add_cylinder(self, pos_x=0, pos_y=0, pos_z=0, radius=1.0, height=1.0, rot_y=0, rot_z=0, data=0.0):

        point_start = len(self.point_list)
        
        points, local_point_list = self._gen_cylinder_point()
        points = [i+point_start for i in points]

        # scale
        local_point_list = np.array([ v*[height, radius, radius] for v in local_point_list])

        # rot z
        local_point_list = np.array([ [v[0]*np.cos(rot_z)-v[1]*np.sin(rot_z), v[0]*np.sin(rot_z)+v[1]*np.cos(rot_z), v[2]] for v in local_point_list])

        # rot y
        local_point_list = np.array([ [v[0]*np.cos(rot_y)+v[2]*np.sin(rot_y), v[1], -v[0]*np.sin(rot_y)+v[2]*np.cos(rot_y)] for v in local_point_list])

        # move
        local_point_list = np.array([ v+[pos_x, pos_y, pos_z] for v in local_point_list])


        self.point_list.extend(local_point_list)

        cell = {'type':6, 'points':points, 'data':data}        
        self.cell_list.append(cell)


    def add_cube(self, x=0, y=0, z=0, size=1.0, data=0.0):
        self.add_cuboid(x, y, z, size, size, size, 0.0, 0.0, data)


    def add_cuboid(self, pos_x=0, pos_y=0, pos_z=0, size_x=1.0, size_y=1.0, size_z=1.0, rot_y=0.0, rot_z=0.0, data=1.0):
        point_start = len(self.point_list)
        points = [0, 1, 2, 3, 4, 5, 6, 7]
        points = [i+point_start for i in points]
        
        local_point_list = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                                     [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
        local_point_list = [ v-[0.0, 0.5, 0.5] for v in local_point_list]

        # scale
        local_point_list = np.array([ v*[size_x, size_y, size_z] for v in local_point_list])

        # rot z
        local_point_list = np.array([ [v[0]*np.cos(rot_z)-v[1]*np.sin(rot_z), v[0]*np.sin(rot_z)+v[1]*np.cos(rot_z), v[2]] for v in local_point_list])

        # rot y
        local_point_list = np.array([ [v[0]*np.cos(rot_y)+v[2]*np.sin(rot_y), v[1], -v[0]*np.sin(rot_y)+v[2]*np.cos(rot_y)] for v in local_point_list])

        # move
        local_point_list = np.array([ v+[pos_x, pos_y, pos_z] for v in local_point_list])

                                    
        #np.concatenate((self.point_list, local_point_list))
        self.point_list.extend(local_point_list.tolist())
        #print self.point_list
                                    

        cell = {'type':12, 'points':points, 'data':data}        
        self.cell_list.append(cell)


    def add_cuboid_p2p(self, pos1=[0,0,0], pos2=[2,0,0], size=1.0, data=0, draw_type=0):

        pos1 = np.array(pos1)
        pos2 = np.array(pos2)
       
        local_pos = pos2 - pos1
        
        rot_y = -np.arctan(local_pos[2] / local_pos[0])
        rot_z = np.arctan(local_pos[1] / np.sqrt(local_pos[0]**2 + local_pos[2]**2))
        
        len = np.sqrt(local_pos[0]**2 + local_pos[1]**2 + local_pos[2]**2)

        #self.add_cuboid(pos1[0], pos1[1], pos1[2], len, size , size, rot_y, rot_z, data)
        self.add_cylinder(pos1[0], pos1[1], pos1[2], size, len, rot_y, rot_z, data)

        

    def add_line(self, p1_x=0, p1_y=0, p1_z=0, p2_x=1, p2_y=0, p2_z=0, data=0):
        point_start = len(self.point_list)

        self.add_point(p1_x, p1_y, p1_z)
        self.add_point(p2_x, p2_y, p2_z)
        cell = {'type':3, 'points':[point_start, point_start+1], 'data':data}
        
        self.cell_list.append(cell)


    def add_swc_with_cuboid(self, swc_filename):
        self.swc_list.append(Swc(swc_filename))
        datasize = len(self.swc_list[-1].data)
            
        for record in self.swc_list[-1].data.values():
            if record['parent'] > 0:                
                parent_record = self.swc_list[-1].data[record['parent']]
                self.add_cuboid_p2p(record['pos'], parent_record['pos'], record['radius'], float(record['id'])/datasize)


    def add_swc_with_line(self, swc_filename):
        self.swc_list.append(Swc(swc_filename))
        datasize = len(self.swc_list[-1].data)
            
        for record in self.swc_list[-1].data.values():
            if record['parent'] > 0:                
                parent_record = self.swc_list[-1].data[record['parent']]
                self.add_line(record['pos'][0], record['pos'][1], record['pos'][2], 
                              parent_record['pos'][0], parent_record['pos'][1], parent_record['pos'][2],
                              float(record['id'])/datasize)


    def add_swc_with_cube(self, swc_filename):
        self.swc_list.append(Swc(swc_filename))
        datasize = len(self.swc_list[-1].data)

        for record in self.swc_list[-1].data.values():
                self.add_cube(record['pos'][0], record['pos'][1], record['pos'][2], record['radius']*2, float(record['id'])/datasize)
        


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
        
        with open (filename, 'w') as file:
            file.write(vtkdata)
            

    def show_state(self):
        print self.point_list
        print self.cell_list

if __name__ == '__main__':


    def test_swc_line_movie(stoptime=100):
        filename_base = 'swc_line%d.vtk'
        vtkgen = VtkGenerator()
        
    
        vtkgen.add_swc_with_line(os.path.join('data', 'Swc_BN_1056.swc'))
    
        for t in range(stoptime):
            for i in range(len(vtkgen.cell_list)):
                vtkgen.cell_list[i]['data'] += 0.02
                if vtkgen.cell_list[i]['data'] > 1.0:
                    vtkgen.cell_list[i]['data'] = 0.0
                
            vtkgen.write_vtk(filename_base % t)


    def test_swc_movie(stoptime=100):
        filename_base = 'swc_cuboid%d.vtk'
        vtkgen = VtkGenerator()
        
        vtkgen.add_swc_with_cuboid(os.path.join('data', 'Swc_BN_1056.swc'))
    
        for t in range(stoptime):
            print('t = %d' % t)
            for i in range(len(vtkgen.cell_list)):
                vtkgen.cell_list[i]['data'] += 0.01
                if vtkgen.cell_list[i]['data'] > 1.0:
                    vtkgen.cell_list[i]['data'] = 0.0
                
            vtkgen.write_vtk(filename_base % t)
    
    
    def test_cylinder(num):
        filename = 'cylinder.vtk'
        vtkgen = VtkGenerator()


        for i in range(num):
            vtkgen.add_cylinder(i*5, 0, 0, i*0.1+1, i*2+1, 0, 0, 0.2*i)
        
        vtkgen.write_vtk(filename)
        
    test_cylinder(1)
    test_swc_movie(100)
