Draw Annotations
================

draw annotations like stimulation points, samplings point or synapses.

- :download:`simple.swc<../tests/simple.swc>`


Draw marks
----------
.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc')
    vtkgen.add_mark((1.0, 1.0, 1.0), size=0.5)
    vtkgen.write_vtk('simple.vtk')
    vtkgen.write_annotation_vtk('simple_mark.vtk')


.. image:: _static/simple_annotation1.png

Draw SWC compartment marks
--------------------------
.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc')
    vtkgen.add_swc_mark(0, 2, size=0.5)
    vtkgen.write_vtk('simple.vtk')
    vtkgen.write_annotation_vtk('simple_swc_mark.vtk')


.. image:: _static/simple_annotation2.png


Draw Synapses
-------------

.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc')
    vtkgen.add_swc('simple.swc', shift_y=30)
    vtkgen.add_swc_connection(0, 2, 1, 1, size=0.5, data=2)
    vtkgen.write_vtk('simple.vtk')
    vtkgen.write_annotation_vtk('simple_connection.vtk')


.. image:: _static/simple_annotation3.png

