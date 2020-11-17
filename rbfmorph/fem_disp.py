from dolfin import *
import numpy as np
def displacements(Fenics_exp, def_face, fixed, ):
    V = FunctionSpace(mesh, "CG", 1)
    v = project(Expression("x[0]*x[1]+x[2]", degree=2),V)
    mf = MeshFunction("size_t", mesh, mesh.topology().dim()-1, 0)
    boundary().mark(mf, 1)
    v2d = vertex_to_dof_map(V)
    dofs = []
    for facet in facets(mesh):
        if mf[facet.index()] == 1:
            vertices = facet.entities(0)
            for vertex in vertices:
                dofs.append(v2d[vertex])

    unique_dofs = np.array(list(set(dofs)), dtype=np.int32)
    boundary_coords = V.tabulate_dof_coordinates()[unique_dofs]
    N=len(boundary_coords[:,1])
    g=np.zeros((N,3))
    for i, dof in enumerate(unique_dofs):
        g[i,0]=v.vector()[dof]
return (g , boundary_coords)

def solve_linear_elasticity(mesh, boundaries, d):
    c = Constant(d)

    V = VectorFunctionSpace(mesh, "Lagrange", 1)
    u = TrialFunction(V)
    v = TestFunction(V)

    E, nu = 10.0, 0.3
    mu = E/(2.0*(1.0 + nu))
    lmbda = E*nu/((1.0 + nu)*(1.0 -2.0*nu))
    sigma = 2*mu*sym(grad(u)) + lmbda*tr(grad(u))*Identity(3)
    F = inner(sigma, grad(v))*dx
    a, L = lhs(F), rhs(F)

    bcs = [DirichletBC(V, Constant((0.0, 0.0, 0.0)), boundaries, 1),
           DirichletBC(V.sub(0), c, boundaries, 2)]

    displacement = Function(V)
    solve(a==L, displacement, bcs)
    return displacement
