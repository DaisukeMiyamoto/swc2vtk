# -*- coding: utf-8 -*-
import unittest
import os
import swc2vtk


class TestVtkGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.swc_file_path = os.path.join('tests', 'simple.swc')
        self.data_file_path = os.path.join('tests', 'simple.dat')
        self.output_file_path = os.path.join('tests', 'output.vtk')
        self.vtk_generator = swc2vtk.VtkGenerator()

    def tearDown(self):
        self.vtk_generator.write_vtk(self.output_file_path)

    def test_add_cylinder(self):
        self.vtk_generator.add_cylinder()

    def test_add_sphere(self):
        self.vtk_generator.add_sphere()

    def test_add_swc(self):
        simple_cmp_size = 11
        self.vtk_generator.add_swc(self.swc_file_path)
        self.assertEqual(simple_cmp_size, len(self.vtk_generator.swc_list[0].data))

    def test_add_swc_flip(self):
        simple_cmp_size = 11
        self.vtk_generator.add_swc(self.swc_file_path, inv_x=True, inv_y=True, inv_z=True,
                                   shift_x=100, shift_y=100, shift_z=100)
        self.assertEqual(simple_cmp_size, len(self.vtk_generator.swc_list[0].data))

    def test_add_datafile(self):
        simple_cmp_size = 11
        self.vtk_generator.add_swc(self.swc_file_path)
        self.vtk_generator.add_datafile(self.data_file_path)
        self.assertEqual(simple_cmp_size, len(self.vtk_generator.swc_list[0].data))

    def test_write_vtk_options(self):
        self.vtk_generator.add_swc(self.swc_file_path)
        self.vtk_generator.write_vtk(self.output_file_path, fixval=True, movingval=True, coloring=True,
                                     diam_ratio=0.2, normalize_diam=True, radius_data=True)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestVtkGenerator))
    return suite


if __name__ == '__main__':
    unittest.main()
