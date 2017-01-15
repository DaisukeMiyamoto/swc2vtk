from setuptools import setup

setup(
    name='swc2vtk',
    version='0.1.1',
    description='SWC to VTK converter for visualize multi-compartment neurons and neural circuit simulations',
    author='nebula',
    author_email='miyamoto@brain.imi.i.u-tokyo.ac.jp',
    url='https://github.com/DaisukeMiyamoto/swc2vtk',
    install_requires=['numpy', 'tqdm'],
    keywords = ['neuron', 'simulation', 'visualization', 'paraview', 'vtk']
)
