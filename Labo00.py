import numpy as np

"""
De la libraria numpy de Python, solo estan permitidos utilizar
las funciones que convierten listas a arrays, las que devuelven el tamano de un
array y las funciones que encuentran maximos o minimos 
-list to array
-tam de listas
-max y min
"""


#1. esCuadrada(A) : Bool

def esCuadrada(matriz):
    return len(matriz) == len(matriz[0])

#2. triangSup(A) : matriz
# triangularSuperior es 0 debajo de la diagonal

def triangSup(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizResultado = matriz.copy()

    for i in range(0,filas):
        for j in range(0,columnas):
            if i > j:
                matrizResultado[i][j] = 0
    return matrizResultado

#3. triangInf(A) : matriz
# triangularInferior es con 0 por encima de la diagonal

def triangInf(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizResultado = matriz.copy()

    for i in range(0,filas):
        for j in range(0,columnas):
            if i < j:
                matrizResultado[i][j] = 0
    return matrizResultado

#4. diagonal(A): matriz
#Precondicion: Una matriz es diagonal si es cuadrada, tonces la entrante tiene
#que serlo tambien.

def diagonal(matriz):
    if (not esCuadrada(matriz)):
        print("Maestro, pasame una matriz cuadrada")
        return
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizResultado = matriz.copy()

    for i in range(0,filas):
        for j in range(0,columnas):
            if i != j:
                matrizResultado[i][j] = 0
    return matrizResultado

#5. traza(A) : int | float
#Precondicion: Cuadrada

def traza(matriz):
    if (not esCuadrada(matriz)):
        print("Maestro, pasame una matriz cuadrada")
        return
    filas = len(matriz)
    columnas = len(matriz[0])
    res = 0

    for i in range(0,filas):
        res += matriz[i][i]
    return res

#6.  traspuesta(A)

def traspuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matrizResultado = matriz.copy()
    matrizResultado = matrizResultado.reshape((columnas,filas))

    for i in range(0,filas):
        for j in range(0,columnas):
            matrizResultado[j][i] = matriz[i][j]

    return matrizResultado

#7. simetrica(A)
#Si o si con matrices cuadradas

def esSimetrica(matriz):

    if not esCuadrada(matriz):
        return False

    matrizTraspuesta = traspuesta(matriz)
    matrizBool = matriz == matrizTraspuesta
    res = True
    for i in range(0,len(matrizBool)):
        for j in range(0,len(matrizBool[0])):
            res = res and matrizBool[i][j]
    return res

#8.  calcularAx(A,x) 

def calcularAx(matriz,vector):
    filas = len(matriz)
    columnas = len(matriz[0])
    vectorRes = np.zeros((1,filas)) #array([[0,...,0]])

    for i in range(0,filas):
        for j in range(0,columnas):
            vectorRes[0][i] = vectorRes[0][i] + matriz[i][j] * vector[0][j]
    return vectorRes
