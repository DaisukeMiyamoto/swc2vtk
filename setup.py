from setuptools import setup
import os

description='SWC to VTK converter for visualize multi-compartment neurons and neural circuit simulations'
long_description = description
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name='swc2vtk',
    version='1.0.4',
    packages=['swc2vtk'],
    package_dir={'swc2vtk': 'swc2vtk'},
    description=description,
    long_description=long_description,
    author='nebula',
    author_email='miyamoto@brain.imi.i.u-tokyo.ac.jp',
    url='https://github.com/DaisukeMiyamoto/swc2vtk',
    install_requires=['numpy', 'tqdm'],
    keywords=['neuron', 'simulation', 'visualization', 'paraview', 'vtk', 'multi compartment', 'large scale'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    test_suite='tests',
)
