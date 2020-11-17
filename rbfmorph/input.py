import numpy as np
def input_param(x_1,y_1,z_1):
    num_coor=len(x_1.flatten())
    coor=np.zeros((num_coor,3))
    coor[:,0]=x_1.flatten()
    coor[:,1]=y_1.flatten()
    coor[:,2]=z_1.flatten()
    return coor

def P_mat(ctr_pts):
    P=np.zeros((N,4))
    for i in range(N):
        for j in range(4):
            if (j==0): P[i,j]=1
            else: P[i,j]=ctr_pts[i,j-1]
    return P
