import Labo1
import numpy as np


matriz1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz2 = np.ones((3,3))
matriz3 = np.zeros((2,3))
matriz4 = np.array([[3,9,2],
                    [1,5,2]])

matrices = [matriz1,matriz2,matriz3,matriz4]
casosTest = len(matrices)

vectorRes = np.zeros((1,20))
print(vectorRes)


""" for i in range(0,casosTest):

    matrizNumpy = np.matrix.transpose(matrices[i])
    print(matrices[i])
    print(matrizNumpy)
 """




# an_array = np.ones((2,3))
# print('dimensiones: ', an_array.shape)
# print('cantidad de dimensiones: ', an_array.ndim)
# print('cantidad de elementos: ', an_array.size)
# print('tipo: ', an_array.dtype) 

def sonIguales(matriz1,matriz2):
    if matriz1.shape != matriz2.shape:
        return False

    matrizBool = matriz1 == matriz2
    res = True
    for i in range(0,len(matrizBool)):
        for j in range(0,len(matrizBool[0])):
            res = res and matrizBool[i][j]
    return res


def test_esCuadrada():
    for i in range(0,casosTest):
        assert Labo1.esCuadrada(matrices[i]) == (matrices[i].shape[0] == matrices[i].shape[1])

def test_triangSup():
    for i in range(0,casosTest):
        nuevaMatriz = Labo1.triangSup(matrices[i])
        assert sonIguales(nuevaMatriz,np.triu(matrices[i]))

def test_triangInf():
    for i in range(0,casosTest):
        nuevaMatriz = Labo1.triangInf(matrices[i])
        assert sonIguales(nuevaMatriz,np.tril(matrices[i]))


#Si le pasas un vector crea una matriz diagonal.
#Si le pasas una matriz extrae una diagonal.
#Porque asi funca....
#Tonces np.diag(A) saca el vector diagonal de la matriz,
#y si haces np.diag(np.diag(A)), a ese vector lo transformas en la matriz
#con esa diagonal y el resto en 0.

def test_diagonal():
    for i in range(0,casosTest):
        matrizActual = matrices[i]
        if (not Labo1.esCuadrada(matrizActual)):
            continue
        nuevaMatriz = Labo1.diagonal(matrizActual)
        matrizNumpy = np.diag(np.diag(matrizActual))
        assert sonIguales(nuevaMatriz,matrizNumpy) , (
            f"Fallo un test con matriz{i}: \n"
            f"Tu funcion dio {nuevaMatriz}\n"
            f"Numpy dio {matrizNumpy}\n"
        )

def test_traza():
    for i in range(0,casosTest):
        matrizActual = matrices[i]
        if (not Labo1.esCuadrada(matrizActual)):
            continue
        nuevaMatriz = Labo1.traza(matrizActual)
        matrizNumpy = np.trace(matrizActual)
        assert nuevaMatriz == matrizNumpy , (
            f"Fallo un test con matriz{i}: \n"
            f"Tu funcion dio {nuevaMatriz}\n"
            f"Numpy dio {matrizNumpy}\n"
        )


def test_traspuesta():
    for i in range(0,casosTest):
        matrizActual = matrices[i]
        nuevaMatriz = Labo1.traspuesta(matrizActual)
        matrizNumpy = np.matrix.transpose(matrizActual)
        assert sonIguales(nuevaMatriz,matrizNumpy) , (
            f"Fallo un test con matriz{i+1} que era:\n"
            f"\n{matrices[i]}\n"
            f"Tu funcion dio \n{nuevaMatriz}\n"
            f"Numpy dio\n {matrizNumpy}\n"
        )


def test_esSimetrica():
    for i in range(0,casosTest):
        matrizActual = matrices[i]
        if (not Labo1.esCuadrada(matrizActual)):
            continue
        boolFuncionCasera = Labo1.esSimetrica(matrizActual)
        boolFuncionNumpy = np.array_equal(matrizActual,np.matrix.transpose(matrizActual))
        assert  boolFuncionCasera == boolFuncionNumpy, (
            f"Fallo un test con matriz{i+1} que era:\n"
            f"\n{matrices[i]}\n"
            f"Tu funcion dio \n{boolFuncionCasera}\n"
            f"Numpy dio\n {boolFuncionNumpy}\n"
        ) 

def test_calcularAx():
        for i in range(0,casosTest):
        matrizActual = matrices[i]
        if (not Labo1.esCuadrada(matrizActual)):
            continue
        boolFuncionCasera = Labo1.esSimetrica(matrizActual)
        boolFuncionNumpy = np.array_equal(matrizActual,np.matrix.transpose(matrizActual))
        assert  boolFuncionCasera == boolFuncionNumpy, (
            f"Fallo un test con matriz{i+1} que era:\n"
            f"\n{matrices[i]}\n"
            f"Tu funcion dio \n{boolFuncionCasera}\n"
            f"Numpy dio\n {boolFuncionNumpy}\n"
        ) 



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])