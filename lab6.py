import numpy as np


def prodInterno(v,w):
    lenV = len(v)
    lenW = len(w)

    if (lenV != lenW):
        print("Multiplicaste vectores de distinta long")
        return None

    res = 0
    for i in range(lenV):
        res += v[i] * w[i]
    return res


def prodMat(A,B):

    rowA,colA = A.shape
    rowB,colB = B.shape

    if (colA != rowB):
        return None

    res = np.zeros((rowA,rowB))

    for i in range(rowA):
        for j in range(colB):
            res[i][j] = prodInterno(A[i],B[:,j:j+1])


    return res

def prodMatVec(A,v):

    rowA,colA = A.shape
    lenV = len(v)

    if (colA != lenV):
        print("Multiplicaste una matriz NxM por v de otra dimension incorrecta")
        return None

    res = v.copy()

    for i in range(rowA):
        res[i] = prodInterno(A[i],v)

    return res

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

""" 
def fooIterativa(A,vector,k):
    if (k == 0):
        print("Pasame un k mayor a 0")
        return 0

    for i in range(k):
        w = prodMatVec(A,vector)

        normaW = norma(w,2)
        if  """
    
def foo(A,vector):
    w = prodMatVec(A,vector)

    normaW = norma(w,2)
    if (normaW > 0):
        return w/normaW
    else:
        return 0
    

def metpot2k(A,tol=1e-15,K=1000):

    
