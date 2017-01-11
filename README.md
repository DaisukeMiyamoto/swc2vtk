# swc2vtk
![python-2.7, 3.5-blue](https://img.shields.io/badge/python-2.7, 3.5-blue.svg)
![license](https://img.shields.io/badge/license-apache-blue.svg)
![paraview](https://img.shields.io/badge/Paraview-5.2-green.svg)
![NEURON](https://img.shields.io/badge/NEURON-7.4-green.svg)

swc to vtk converter for visualizing neurons and neural circuit simulations in ParaView

## Dependency

## Install

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
row equals to SWC compartment
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
vtkgen.add_swc('simle.swc')

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
### single neuron
![single](https://github.com/DaisukeMiyamoto/swc2vtk/releases/download/v0.01/0965_small.png)

### Coloring multiple SWC files
![Coloring](https://github.com/DaisukeMiyamoto/swc2vtk/releases/download/v0.01/standardbrain_small20170110.png)

## References
- SWC format: http://research.mssm.edu/cnic/swc.html
- http://www.paraview.org/
- http://www.vtk.org/
