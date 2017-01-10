# swc2vtk
swc to vtk converter for visualization in ParaView

## Dependency

## Install

## Usage

## Basic way to generate VTK file from SWC
```python
import swc2vtk
vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('simle.swc')
vtkgen.write_vtk('simple.vtk')
```

