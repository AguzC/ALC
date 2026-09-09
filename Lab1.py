import numpy as np


def error(x,y):

    return np.float64(abs(x-y))

def error_relativo(x,y):

    return abs(error(x,y)/x)

def matricesIguales(A,B):

    dimA = np.shape(A)

    if dimA != np.shape(B):
        return False

    res = True
    filas = dimA[0]
    columnas = dimA[1]

    for i in range(0,filas):
        for j in range(0,columnas):
            res = res and np.isclose(A[i][j],B[i][j]) 
    
    return res
    
