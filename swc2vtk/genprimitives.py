# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:37:20 2016

@author: nebula
"""
import numpy as np


class GenPrimitives():
    """

    """

    @staticmethod
    def cuboid():
        point_order = [0, 1, 2, 3, 4, 5, 6, 7]
        point_list = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                               [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
        point_list = [v - [0.0, 0.5, 0.5] for v in point_list]

        return (point_order, np.array(point_list))

    @staticmethod
    def cylinder(div=8, top_face_diam=1.0):
        point_list = []
        point_order = []

        for i in range(div):
            theta = float(i) / div * 2. * np.pi
            point_list.extend([[0, 0, 0], [0, np.cos(theta), np.sin(theta)]])

            point_order.extend([len(point_order), len(point_order) + 1])

        point_order.extend([0, 1])

        for i in range(div):
            theta = float(i) / div * 2. * np.pi
            point_list.extend([[0, np.cos(theta), np.sin(theta)], [1, np.cos(theta)*top_face_diam, np.sin(theta)*top_face_diam]])

            point_order.extend([div * 2 + i * 2, div * 2 + 1 + i * 2])

        point_order.extend([div * 2, div * 2 + 1])

        for i in range(div):
            theta = float(i) / div * 2. * np.pi
            point_list.extend([[1, 0, 0], [1, np.cos(theta)*top_face_diam, np.sin(theta)*top_face_diam]])

            point_order.extend([div * 2 * 2 + i * 2, div * 2 * 2 + 1 + i * 2])

        point_order.extend([div * 2 * 2, div * 2 * 2 + 1])

        return point_order, np.array(point_list)

    @staticmethod
    def sphere(div=10):
        cell_list = []
        point_list = []

        for i in range(div+1):
            ph = np.pi * i / float(div)
            y = np.cos(ph)
            r = np.sin(ph)
            for j in range(div):
                th = 2.0 * np.pi * j / float(div)
                x = r * np.cos(th)
                z = r * np.sin(th)

                point_list.append([x, y, z])

        for i in range(div):
            points = []
            for j in range(div):
                points.extend([i*div+j, (i+1)*div+j])
            points.extend([i*div, (i+1)*div])
            cell = {'type': 6, 'points': points}
            cell_list.append(cell)

        return cell_list, np.array(point_list)

    @staticmethod
    def hemisphere(div=10):
        cell_list = []
        point_list = []

        for i in range(int(div/2)+1):
            ph = np.pi * i / float(div)
            y = np.cos(ph)
            r = np.sin(ph)
            for j in range(div):
                th = 2.0 * np.pi * j / float(div)
                x = r * np.cos(th)
                z = r * np.sin(th)

                point_list.append([x, y, z])

        for i in range(int(div/2)):
            points = []
            for j in range(div):
                points.extend([i*div+j, (i+1)*div+j])
            points.extend([i*div, (i+1)*div])
            cell = {'type': 6, 'points': points}
            cell_list.append(cell)

        return cell_list, np.array(point_list)

    def hemisphere_cylinder(self, div=10):
        cell_list = []
        point_list = []
