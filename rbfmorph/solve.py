import numpy as np

def M(coor,ctr_pts):
    M_m=np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            M_m[i,j]=rbf(rd(ctr_pts[i],ctr_pts[j]))
    return M_m
def lhs_(P,M_m):
    lhs=np.zeros((N+4,N+4))
    P_t=np.transpose(P)
    for i in range(N+4):
        for j in range(N+4):
            if (i<N and j<N): lhs[i,j]=M_m[i,j]
            elif (i<N and j>(N-1)): lhs[i, j]=P[i,j-N]
            elif (i>(N-1) and j<N):lhs[i,j]= P_t[i-N,j]
    return lhs
def sol_yb(lhs, g):
    rhs=np.zeros((N+4,3))
    for i in range(N):
        for j in range(3):
            rhs[i,j]=g[i,j]

    inv_lhs=np.linalg.inv(lhs)
    yb= inv_lhs @ rhs
    gmma=np.zeros((N,3))
    beta=np.zeros((4,3))
    for i in range(N+4):
        if (i<N): gmma[i,:]=yb[i,:]
        else : beta[i-N,:]=yb[i,:]
    return (gmma, beta)
