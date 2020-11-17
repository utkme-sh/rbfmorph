import numpy as np
def rd(c1, c2):
    return np.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2+(c1[2]-c2[2])**2)
#rbf as global support spline type
#Gaussian Spline
def rbf(r):
    return np.exp(-r**2)
#Spline polynomial
def rbf1(r,deg):
    return r**deg
# Global
def rbf2(r):
    return np.exp(-r**2)
# %% codecell
