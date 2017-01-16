from setuptools import setup
import os
import sys

description='SWC to VTK converter for visualize multi-compartment neurons and neural circuit simulations',
long_description = description
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()


sys.path.append('./tests')

setup(
    name='swc2vtk',
    version='0.1.1',
    packages=['swc2vtk'],
    package_dir={'swc2vtk': 'swc2vtk'},
    description=description,
    author='nebula',
    author_email='miyamoto@brain.imi.i.u-tokyo.ac.jp',
    url='https://github.com/DaisukeMiyamoto/swc2vtk',
    install_requires=['numpy', 'tqdm'],
    keywords=['neuron', 'simulation', 'visualization', 'paraview', 'vtk'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    test_suite = 'test_genprimitives.suite',
)
