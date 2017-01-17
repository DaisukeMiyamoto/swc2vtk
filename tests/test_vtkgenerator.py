# -*- coding: utf-8 -*-
import unittest
import swc2vtk


class TestVtkGenerator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.vtk_generator = swc2vtk.VtkGenerator()

    def test_add_cylinder(self):
        self.vtk_generator.add_cylinder()
        self.vtk_generator.write_vtk('test.vtk')

    def test_add_sphere(self):
        self.vtk_generator.add_sphere()
        self.vtk_generator.write_vtk('test.vtk')


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestVtkGenerator))
    return suite


if __name__ == '__main__':
    unittest.main()
