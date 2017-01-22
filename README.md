# swc2vtk
![travisci](https://travis-ci.org/DaisukeMiyamoto/swc2vtk.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/DaisukeMiyamoto/swc2vtk/badge.svg?branch=master)](https://coveralls.io/github/DaisukeMiyamoto/swc2vtk?branch=master)
![python-2.7,3.3,3.4-blue](https://img.shields.io/badge/python-2.7,3.3,3.4-blue.svg)
![license](https://img.shields.io/badge/license-apache-blue.svg)
![paraview](https://img.shields.io/badge/Paraview-5.2-green.svg)
![NEURON](https://img.shields.io/badge/NEURON-7.4-green.svg)

SWC to VTK converter for visualizing neurons and neural circuit simulations in ParaView.
This software helps making beautiful visualization of large scale multi-compartmental neuron simulations with a parallelized environment.
If you need any further information, please check http://daisukemiyamoto.github.io/swc2vtk/ .


## Dependency
- tqdm
- numpy
- ~~PyVTK~~


## Install
- $ pip install swc2vtk


## Usage

### Basic way to generate VTK file from one SWC file
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simple.swc')
vtkgen.write_vtk('simple.vtk')
```

### generate a VTK file from multiple SWC files
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simple.swc')
vtkgen.add_swc('simple1.swc')
vtkgen.add_swc('simple2.swc')
vtkgen.write_vtk('combined.vtk')
```

### generate a VTK file from SWC file with simulation data
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simple.swc')
vtkgen.add_datafile('result.dat')
vtkgen.write_vtk('simple.vtk')
```


- data example  
each rows correspondence to SWC compartments
```
-65.0
-65.0
-65.0
-65.0
```

### generate VTK files from SWC file with sequential simulation data
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simple.swc')

vtkgen.add_datafile('result1.dat')
vtkgen.write_vtk('simple1.vtk')

vtkgen.clear_datafile()
vtkgen.add_datafile('result2.dat')
vtkgen.write_vtk('simple2.vtk')

vtkgen.clear_datafile()
vtkgen.add_datafile('result3.dat')
vtkgen.write_vtk('simple3.vtk')
```

## Output Examples
### Single Neuron Morphology
![single](https://github.com/DaisukeMiyamoto/swc2vtk/releases/download/v0.01/singleneuron_small.png)

- [high resolution version](https://github.com/DaisukeMiyamoto/swc2vtk/releases/download/v0.01/singleneuron.png)

### Coloring Multiple SWC Files
![Coloring](https://github.com/DaisukeMiyamoto/swc2vtk/releases/download/v0.01/standardbrain_small20170110.png)

### Single Neuron Simulation

### Neural Circuit Simulation

### Volume Rendering


## References
- SWC format: http://research.mssm.edu/cnic/swc.html
- http://neuromorpho.org/
- http://www.paraview.org/
- http://www.vtk.org/
