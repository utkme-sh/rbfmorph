import numpy as np
from .rbf_func import *

def s_x(ctr_pts, coor, beta, gmma,deg):
    s_x=np.zeros(3)
    for i in range(3):
        for j in range(N):
            s_x[i]=s_x[i]+gmma[j,i]*rbf(rd(coor, ctr_pts[j]),deg)
        s_x[i]=s_x[i]+beta[0,i]*1 + beta[1,i]*coor[0] + coor[1]*beta[2,i] + coor[2]*beta[3,i]
    return s_x
# %% codecell

def New_coor(coor,ctr_pts,P,g,num_coor):
    M_m=M(coor,ctr_pts)
    # M_m
    # %% codecell
    lhs=lhs_(P,M_m)
    # lhs
    # %% codecell
    gmma, beta=sol_yb(lhs, g)
    # %% codecell
    coor_new=np.zeros((num_coor,3))
    # %% codecell
    cor_t=(1.0,1.0,1.0)
    s_x(ctr_pts, cor_t, beta, gmma,deg)
    # %% codecell
    for i in range(num_coor):
        coor_new[i,:]=coor[i,:]+s_x(ctr_pts, coor[i], beta, gmma,deg)
return coor_new
