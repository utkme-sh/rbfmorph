from dolfin import *
import meshio
msh = meshio.read("meshings/final_final.msh")

## physical surface & volume data
for key in msh.cell_data_dict["gmsh:physical"].keys():
    if key == "triangle":
        triangle_data = msh.cell_data_dict["gmsh:physical"][key]
    elif key == "tetra":
        tetra_data = msh.cell_data_dict["gmsh:physical"][key]

## cell data
tetra_cells = np.array([None])
triangle_cells = np.array([None])
for cell in msh.cells:
    if cell.type == "tetra":
        if tetra_cells.all() == None:
            tetra_cells = cell.data
        else:
            tetra_cells = np.concatenate((tetra_cells,cell.data))
    elif cell.type == "triangle":
        if triangle_cells.all() == None:
            triangle_cells = cell.data
        else:
            triangle_cells = np.concatenate((triangle_cells,cell.data))

## put them together
tetra_mesh = meshio.Mesh(points=msh.points,
                         cells={"tetra": tetra_cells},
                         cell_data={"name_to_read":[tetra_data]})
triangle_mesh =meshio.Mesh(points=msh.points,
                               cells=[("triangle", triangle_cells)],
                               cell_data={"name_to_read":[triangle_data]})
## output
meshio.write("meshings/mesh.xdmf", tetra_mesh)
meshio.write("meshings/mf.xdmf", triangle_mesh)

mesh = Mesh()
with XDMFFile("meshings/mesh.xdmf") as infile:
    infile.read(mesh)
mvc = MeshValueCollection("size_t", mesh, 2)
with XDMFFile("meshings/mf.xdmf") as infile:
    infile.read(mvc, "name_to_read")
mf = cpp.mesh.MeshFunctionSizet(mesh, mvc)

mvc2 = MeshValueCollection("size_t", mesh, 3)
with XDMFFile("meshings/mesh.xdmf") as infile:
    infile.read(mvc2, "name_to_read")
cf = cpp.mesh.MeshFunctionSizet(mesh, mvc2)
