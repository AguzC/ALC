import numpy as np



def norma(x,p):

    if (p == 'inf'):
        res = abs(x[0])
        for i in range(0,len(x)):
            res = max(res,abs(x[i]))
        return res

    res =0
    for i in range(0,len(x)):
        res += np.power(x[i],p)

    res = np.power(res,1/p)
    return res

def normaliza(X,p):
    res = [[] for _ in range(len(X))]

    for i in range(len(X)):
        normaVector = norma(X[i],p)

        for j in range(len(X[i])):
            res[i].append(X[i][j]/normaVector)

    return res


def normaExacta(A, p = [1,'inf']):

    if(p == 1 or p == 'inf'):
        return normaMatriz(A,p)

    if(p != [1,'inf']):
        return None

    return (normaMatriz(A,1),normaMatriz(A,'inf'))

def normaMatriz(A,p):

    res = -np.inf
    dim = A.shape
    filas = dim[0]
    col = dim[1]
    
    if (p==1):
        for i in range(0,col):
            acumulado = 0
            for j in range(0,filas):
                acumulado += abs(A[j][i])
            res = max(acumulado,res)

    if (p=='inf'):
        for i in range(0,filas):
            acumulado = 0
            for j in range(0,col):
                acumulado += abs(A[i][j])
            res = max(acumulado,res)

    return res

def normaMatMC(A,q,p,Np=1000):

    filas = len(A)
    col = len(A[0])
    vectoresAleatorios = np.random.randint(0, 10, size=(Np, col))
    normalizados = normaliza(vectoresAleatorios,p)

    maxNorma = -np.inf
    maxVectorinho = []

    for i in range(len(normalizados)):
        Ax = A @ normalizados[i]
        valorNorma = norma(Ax,q)

        if (maxNorma <= valorNorma):
            maxNorma = valorNorma
            maxVectorinho = Ax

    return (maxNorma,maxVectorinho)


    

def condExacta(a,b):
    None
