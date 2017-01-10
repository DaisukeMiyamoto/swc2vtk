# swc2vtk
swc to vtk converter for visualization in ParaView

## Dependency

## Install

## Usage

### Basic way to generate VTK file from one SWC file
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simle.swc')
vtkgen.write_vtk('simple.vtk')
```

### generate a VTK file from multiple SWC files
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simle.swc')
vtkgen.add_swc('simle1.swc')
vtkgen.add_swc('simle2.swc')
vtkgen.write_vtk('combined.vtk')
```

### generate a VTK file from SWC file with simulation data
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simle.swc')
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

vtkgen.clear_datafile('result2.dat')
vtkgen.write_vtk('simple2.vtk')

vtkgen.clear_datafile('result3.dat')
vtkgen.write_vtk('simple3.vtk')
```
