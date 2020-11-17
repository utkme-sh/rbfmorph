from pyevtk.hl import *

import pygmsh as pm
from dolfin import *
import numpy as np
# import matplotlib.pyplot as plt
# x0 = 0.0
# y0 = 0.0
# x1 = 100.0
# y1 = 100.0
#
# geom = pm.opencascade.Geometry()
# rec = geom.add_rectangle([x0,y0,0],x1,y1)
# msh=pm.generate_mesh(geom)
# cells_tri=np.vstack((cell.data for cell in msh.cells if cell.type =="triangle"))
def mesh_edit(mesh,g,ctr_pts):
    editor = MeshEditor()
    editor.open(mesh, 'triangle', 2, 2)
    editor.init_vertices(len(msh.points))
    editor.init_cells(len(cells_tri))

    for i, point in enumerate(msh.points):
        new_point = point[:-1]*(np.random.random()*0.01-0.095)
        editor.add_vertex(i, new_point)
    for i, cell in enumerate(cells_tri):
        editor.add_cell(i, cell)
    editor.close()
return new_mesh

#
# fig, ax = plt.subplots(1,2,figsize=(15,8))
# ax1, ax2 = ax
# ax1.triplot(msh.points[:, 0], msh.points[:, 1], cells_tri, "-o")
# ax1.set_title(r"Old Mesh", fontsize=18)
# fig.sca(ax2)
# plot(mesh, "-o")
# ax2.set_title(r"Moved Mesh", fontsize=18)
# fig.tight_layout()
# plt.show()

def mesh_vtk_export(x1,y1,z1,npoints):
# Example 1
    # npoints = 1000
    # x = np.random.rand(npoints)
    # y = np.random.rand(npoints)
    # z = np.random.rand(npoints)
    pressure = np.random.rand(npoints)
    temp = np.random.rand(npoints)
    pointsToVTK("./rnd_points", x_1, y_1, z_1, data={"temp": temp, "pressure": pressure})

def update_mesh(mesh, displacement, boundaries):

    new_mesh = Mesh(mesh)
    new_boundaries = MeshFunction("size_t", new_mesh, 2)
    new_boundaries.set_values(boundaries.array())
    ALE.move(new_mesh, displacement)
    return new_mesh, new_boundaries
