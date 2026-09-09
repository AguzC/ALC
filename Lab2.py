import numpy as np

def rota(theta):
    return np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])

def escala(s):

    dim = len(s)
    res = np.zeros((dim,dim))
    for i in range(0,dim):
        res[i][i] = s[i]

    return res


def rota_y_escala(theta,s):

    rotacion = rota(theta)
    escalar = escala(s)
    return escalar @ rotacion
    

def afin(theta,s,b):

    matriz2x2 = rota_y_escala(theta,s)
    res = np.zeros((3,3))

    for i in range(0,2):
        for j in range(0,2):
            res[i][j] = matriz2x2[i][j]

    res[0][2] = b[0]
    res[1][2] = b[1]
    res[2][2] = 1

    return res

def trans_afin(v,theta,s,b):
    nuevoV = np.array([v[0],v[1],1])

    vectorNuevo = afin(theta,s,b) @ nuevoV
    return np.array([vectorNuevo[0],vectorNuevo[1]])
