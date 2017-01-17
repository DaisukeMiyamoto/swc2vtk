# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:37:20 2016

@author: nebula
"""

import os
import math
import numpy as np
from tqdm import tqdm

# from swc2vtk.genprimitives import GenPrimitives
# from swc2vtk.swc import Swc
import swc2vtk


class VtkGenerator():
    header_base = '''\
# vtk DataFile Version 3.0
SWC2VTK
ASCII
DATASET UNSTRUCTURED_GRID
'''
    volume_header_base = '''\
# vtk DataFile Version 1.0
SWC2VTK VOLUME
ASCII
DATASET STRUCTURED_POINTS
'''

    def __init__(self):
        self.header = self.header_base
        self.volume_header = self.volume_header_base
        
        self.swc_list = []
        self.point_list = []
        self.cell_list = []
        self.datafile_list = []

        self.point_text = ''
        self.cell_text = ''

        self.converted = False
        self.draw_mode = 0
        self.ncell_per_compartment = 1

    def set_draw_mode(self, draw_mode):
        self.draw_mode = draw_mode
        self.converted = False
        self.point_list = []
        self.cell_list = []

    def add_cylinder(self, pos_x=0, pos_y=0, pos_z=0, radius=1.0, height=1.0, rot_y=0, rot_z=0,
                     data=0.0, radius_ratio=1.0):

        local_cell_list = []
        local_point_list = []
        if self.draw_mode == 0:
            local_cell_list, local_point_list = swc2vtk.GenPrimitives.cylinder()
        elif self.draw_mode == 1:
            local_cell_list, local_point_list = swc2vtk.GenPrimitives.cylinder(top_face_diam=radius_ratio)
        elif self.draw_mode == 2:
            local_cell_list, local_point_list = swc2vtk.GenPrimitives.cylinder_3cell(top_face_diam=radius_ratio)
            self.ncell_per_compartment = len(local_cell_list)
        elif self.draw_mode == 3:
            local_cell_list, local_point_list = swc2vtk.GenPrimitives.hemisphere_cylinder(top_face_diam=radius_ratio,
                                                                                          height=height, radius=radius)
            self.ncell_per_compartment = len(local_cell_list)
            height = 1.0
            radius = 1.0

        point_start = len(self.point_list)
        for cell in local_cell_list:
            cell['points'] = [(i + point_start) for i in cell['points']]
            cell['data'] = data

        # scale
        local_point_list = np.array([ v*[height, radius, radius] for v in local_point_list])
        # rot z
        local_point_list = np.array([ [v[0]*np.cos(rot_z)-v[1]*np.sin(rot_z), v[0]*np.sin(rot_z)+v[1]*np.cos(rot_z), v[2]] for v in local_point_list])
        # rot y
        local_point_list = np.array([ [v[0]*np.cos(rot_y)+v[2]*np.sin(rot_y), v[1], -v[0]*np.sin(rot_y)+v[2]*np.cos(rot_y)] for v in local_point_list])
        # move
        local_point_list = np.array([ v+[pos_x, pos_y, pos_z] for v in local_point_list])

        self.point_list.extend(local_point_list)
        self.cell_list.extend(local_cell_list)

    def add_sphere(self, x=0, y=0, z=0, size=1.0, data=0.0):
        point_start = len(self.point_list)
        # local_cell_list, local_point_list = GenPrimitives.hemisphere_cylinder()
        local_cell_list, local_point_list = swc2vtk.GenPrimitives.sphere()
        for cell in local_cell_list:
            cell['points'] = [i + point_start for i in cell['points']]
            cell['data'] = data

        # scale
        local_point_list = np.array([ v*[size, size, size] for v in local_point_list])
        # move
        local_point_list = np.array([ v+[x, y, z] for v in local_point_list])

        self.point_list.extend(local_point_list)
        self.cell_list.extend(local_cell_list)

    def add_cylinder_p2p(self, pos1=(0, 0, 0), pos2=(2, 0, 0), size=1.0, data=0, radius_ratio=1.0):
        pos1 = np.array(pos1)
        pos2 = np.array(pos2)
        local_pos = pos2 - pos1

        rot_y = -np.arctan2(local_pos[2], local_pos[0])
        rot_z = np.arctan2(local_pos[1], np.sqrt(local_pos[0]**2 + local_pos[2]**2))
        len = np.sqrt(local_pos[0]**2 + local_pos[1]**2 + local_pos[2]**2)

        self.add_cylinder(pos1[0], pos1[1], pos1[2], size, len, rot_y, rot_z, data, radius_ratio=radius_ratio)

    def convert_swc(self, diam_ratio=1.0, normalize_diam=False):
        self.converted = True

        for swc_data in self.swc_list:
            data_size = len(swc_data.data)

            for record in tqdm(swc_data.data.values(), desc='Converting: ' + swc_data.filename):
                if normalize_diam:
                    record['radius'] = math.sqrt(record['radius'])

                self.ncell_per_compartment = 1
                if record['parent'] > 0:
                    parent_record = swc_data.data[record['parent']]
                    self.add_cylinder_p2p(record['pos'], parent_record['pos'], record['radius'] * diam_ratio,
                                          float(record['id']) / data_size,
                                          radius_ratio=(parent_record['radius']/record['radius']))

        self.point_text = self._point2text()
        self.cell_text = self._cell2text()

    def add_swc(self, swc_filename,
                shift_x=0.0, shift_y=0.0, shift_z=0.0, inv_x=False, inv_y=False, inv_z=False):
        self.converted = False
        self.swc_list.append(swc2vtk.Swc(swc_filename))
        self.swc_list[-1].invert(inv_x, inv_y, inv_z)
        self.swc_list[-1].shift(shift_x, shift_y, shift_z)

    def _point2text(self):
        text = 'POINTS %d float\n' % (len(self.point_list))
        for point in tqdm(self.point_list, desc='Generating Points'):
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

    def _fixval2text(self, title='fixval', fixval=0.0):
        text = ''
        text += 'SCALARS '+title+' float 1\n'
        text += 'LOOKUP_TABLE default\n'
        for cell in self.cell_list:
            text += str(fixval)+'\n'

        return text

    def _movingval2text(self, title='movingval', num=100):
        text = ''
        text += 'SCALARS '+title+' float ' + str(num) + '\n'
        text += 'LOOKUP_TABLE default\n'

        for i in range(len(self.cell_list)):
            val = i
            for j in range(num):
                text += str(val) + ' '
                val = (val + 1) % 512

            text += '\n'

        return text

    def _file2text(self, datafile_list, title):
        text = ''
        text += 'SCALARS ' + title + ' float 1\n'
        text += 'LOOKUP_TABLE default\n'

        for filename in datafile_list:
            with open(filename, 'r') as f:
                read_data = f.readlines()

            for i in range(len(read_data)):
                if read_data[i][0] != '#':
                    for j in range(self.ncell_per_compartment):
                        text += read_data[i].rstrip() + '\n'

        return text

    def _radius2text(self):
        text = ''
        text += 'SCALARS radius float 1\n'
        text += 'LOOKUP_TABLE default\n'

        for swc in self.swc_list:
            for j, record in swc.data.items():
                if j > 1:
                    for k in range(self.ncell_per_compartment):
                        text += str(record['radius']) + '\n'

        return text

    def _coloringbyswc(self):
        text = ''
        text += 'SCALARS coloring float 1\n'
        text += 'LOOKUP_TABLE default\n'

        for i, swc in enumerate(self.swc_list):
            val = i * (1.0 / len(self.swc_list))
            for j in range(len(swc.data) - 1):
                text += str(val + (1.0 / len(self.swc_list) / (len(swc.data) - 1))) + '\n'

        return text

    def add_datafile(self, datafilename):
        self.datafile_list.append(datafilename)

    def clear_datafile(self):
        self.datafile_list = []

    def write_vtk(self, filename, fixval=None, datatitle='filedata', movingval=False, coloring=False,
                  diam_ratio=1.0, normalize_diam=False, radius_data=False):
        if not self.converted:
            self.convert_swc(diam_ratio=diam_ratio, normalize_diam=normalize_diam)

        with open(filename, 'w') as file:
            file.write(self.header)
            file.write(self.point_text)
            file.write(self.cell_text)

            if fixval is not None:
                file.write(self._fixval2text(fixval=fixval))

            if movingval:
                file.write(self._movingval2text())

            if len(self.datafile_list) > 0:
                file.write(self._file2text(self.datafile_list, datatitle))

            if coloring:
                file.write(self._coloringbyswc())

            if radius_data:
                file.write(self._radius2text())

    def _swc2volume(self, swc, world, origin=(0.0, 0.0, 0.0), ratio=(1.0, 1.0, 1.0)):
        point_weight = 0.2
        # for point in self.point_list:
        for k, record in tqdm(swc.data.items(), desc=swc.filename):
            pos = (int(round((record['pos'][0] - origin[0]) / ratio[0], 0)),
                   int(round((record['pos'][1] - origin[1]) / ratio[1], 0)),
                   int(round((record['pos'][2] - origin[2]) / ratio[2], 0)))
            if pos[2] < 0 or 0 or pos[1] < 0 or pos[0] < 0 or pos[2] > len(world) or pos[1] > len(world[0]) or pos[
                0] > len(world[0][0]):
                print('Out of range: (%f, %f, %f)' % (record['pos'][0], record['pos'][1], record['pos'][2]))
            else:
                world[pos[2]][pos[1]][pos[0]] += point_weight

        return world

    def write_volume_vtk(self, filename, origin=(0.0, 0.0, 0.0), ratio=(1.0, 1.0, 1.0), div=(256, 256, 64)):
        vtkdata = ''
        vtkdata += self.volume_header
        vtkdata += 'DIMENSIONS %d %d %d\n' % (div[0], div[1], div[2])
        vtkdata += 'ORIGIN %f %f %f\n' % (origin[0], origin[1], origin[2])
        vtkdata += 'ASPECT_RATIO %f %f %f\n' % (ratio[0], ratio[1], ratio[2])
        vtkdata += ('POINT_DATA %d\n' % (div[0] * div[1] * div[2]))
        vtkdata += 'SCALARS volume float\n'
        vtkdata += 'LOOKUP_TABLE default\n'

        world = np.zeros((div[2], div[1], div[0]))

        for swc in self.swc_list:
            world = self._swc2volume(swc, world, origin, ratio)

        with open (filename, 'w') as file:
            file.write(vtkdata)
            for i in range(div[2]):
                for j in range(div[1]):
                    for k in range(div[0]):
                        file.write('%f\n' % (world[i][j][k]))

    def show_state(self):
        print(self.point_list)
        print(self.cell_list)
        print(self.swc_list)
        print(self.datafile_list)


if __name__ == '__main__':

    def test_swc_movie(stoptime=100):
        filename_base = 'swc_cuboid%d.vtk'
        vtkgen = VtkGenerator()
        
        vtkgen.add_swc(os.path.join('swc', 'Swc_BN_1056.swc'))
    
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
    # test_swc_movie(100)
    # test_swc_line()
