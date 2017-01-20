Examples
========

- :download:`simple.swc<../tests/simple.swc>`
- :download:`simple.dat<../tests/simple.dat>`


Generate a VTK file from multiple SWC files
-------------------------------------------

.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc')
    vtkgen.add_swc('simple1.swc')
    vtkgen.add_swc('simple2.swc')
    vtkgen.write_vtk('combined.vtk')


Generate a VTK file from SWC file with simulation data
------------------------------------------------------

.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc')
    vtkgen.add_datafile('simple.dat')
    vtkgen.write_vtk('simple.vtk')


Generate VTK files from SWC file with sequential simulation data
----------------------------------------------------------------
.. code-block:: python

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


Change SWC file position
------------------------
.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc', shift_x=100.0, shift_y=10.0, shift_z=50.0, inv_x=True)
    vtkgen.write_vtk('simple.vtk')

