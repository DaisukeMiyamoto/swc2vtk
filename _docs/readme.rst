README
======

Introduction
------------
SWC to VTK converter for visualizing neurons and neural circuit simulations in ParaView.


Installation
------------
::

    pip install swc2vtk

Quick example
-------------
- :download:`simple.swc<../tests/simple.swc>`

.. code-block:: python

    import swc2vtk
    vtkgen = swc2vtk.VtkGenerator()
    vtkgen.add_swc('simple.swc')
    vtkgen.write_vtk('simple.vtk')


.. image:: _static/simple.0003.png


Citation
---------
