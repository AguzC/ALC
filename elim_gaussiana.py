#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]
    n=A.shape[1]
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return


    ## desde aqui -- CODIGO A COMPLETAR
    """ 
    Objetivo: Desde i = 0 a i = n-2, voy tomando los pivotes y divido al resto de la columna
    por ese pivote, y despues devolver L, donde la diagonal son todos 1, la parte de arriba 0s
    y la parte de abajo los valores cuando termino el for anterior. Devolver U que va a ser todo
    0s debajo de la diagonal, y el resto igualito a la matriz que tengo. y devolver la cantidad
    de operaciones, donde cuentan las sumas, restas, divisiones y multiplicaciones.
    Cuando reemplazo los valores correspondientes de la primera columna, despues tengo que 
    calcular toda la submatriz A(i), que es hacer la suma, posicion a posicion, de la fila i
    multiplicada por su primer -elemento/a[i][i]
    Primero For dentro: Va a hacer la division de los primeros elementos
    Segundo For dentro: Va a calcular el resto de la submatriz
    """

    cant_op = 0

    for i in range(n-1):
        
        for j in range(i+1,n-1):

            pivot = Ac[i][i]
            cant_op += 1   #1 division
            Ac[j][i] = Ac[j][i] / pivot

        for fila in range(i+1,n-1):
            for col in range(i+1,n-1):

                resAnterior = Ac[fila - 1][]

                Ac[fila][col] = 






                
    ## hasta aqui, calculando L, U y la cantidad de operaciones sobre 
    ## la matriz Ac
            
    
    return L, U, cant_op


def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) 
    B[:n,n-1] = 1
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

if __name__ == "__main__":
    main()
    
    
