import numpy as np

#function that multiplies matrices
def mult_m(p,x,y,z):
    resp1=np.dot(z,x)
    resp2=np.dot(resp1,y)
    resp3=np.dot(resp2,p)
    return resp3