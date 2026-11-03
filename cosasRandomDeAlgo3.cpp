#include <iostream>
#include <vector>
#include <climits>
#include <string>
#include <algorithm>

using namespace std ;




/* 

*Idea actual: Hacer N grafos para las N bicicletas, sabemos que el maximo de nodos y aristas es 1000, para ambos, so, 
*si hacemos todo explicito, con las N listas de adyacencia, tenemos los 32 bytes * N nodos * N bicis * M aristas, con
*un maximo de 32 bytes * 10^9, que son 32 gb, lo cual es psicopata, la otra seria intentar evitar guardar todo explicito,
*si logramos eso, bajamos a un coste maximo de 32mb, which is pretty good, asi que la idea seria poder usar un dijkstra 
*sobre un grafo que represente las N capas pero no explicitas, quizas haciendo la cuenta en el momento??,
*Vamos a tener la lista de adyacencia seguro, con N + M de mem, 

*La lista de adjacencia del grafo de n capas va a tener n.m aristas, puedo hacer que el grafo sea de la pinta
*grafoCapas[bicicleta][nodo], 

*/



int juanYLasCletas(int cantNodos,int cantAristas,vector<vector<pair<int,int>>>& grafoOriginal,vector<int>& factorLentitud){

    
    vector<vector<vector<pair<int,int>>>> grafoNCapas(cantNodos,vector<vector<pair<int,int>>>(cantNodos));


    for (size_t i = 0; i < cantNodos; i++){
        //*"Por cada par (nodo,peso) del nodo i del grafo original..."
        for (auto& [nodo, peso] : grafoOriginal[i]) {
                for (int j = 0; j < cantNodos;j++){
                    //*Esto pone las aristas dentro de una unica capa
                    grafoNCapas[j][i].push_back({nodo,peso * factorLentitud[j]});
                    //*Esto pone las aristas que conectan a capas....
                    grafoNCapas[i][i].push_back({nodo,peso * factorLentitud[j]});
                }
        }
    }
    
    //*Diria que hasta aca tengo N grafos, no conectados entre si pero con sus pesos
    //*ya escalados y tambien las aristas hacia las distintas capas
    
    
    
    
    
    int res;
    //res = dijkstra(grafoNCapas);

    return res;
}




int main () {
    ios :: sync_with_stdio ( false );
    cin . tie ( NULL );
    int cantCasos;
    int cantNodos;
    int cantAristas; 
    cin >> cantCasos;
    int nodoA;
    int nodoB;
    int peso;

    for (int casos = 0; casos < cantCasos; casos++){
        cin >> cantNodos;
        //En cada lista de vecinos, es (nodo,pesoDeLaArista)
        vector<vector<pair<int,int>>> aristas(cantNodos);
        vector<int> factorLentitud(cantNodos);
        cin >> cantAristas;
        
        //Recibo el grafo
        for (int m = 0; m < cantAristas; m++){// n-1 veces que son las aristas
            cin >> nodoA;
            cin >> nodoB;
            cin >> peso;
            //Asigno a ambos nodos la otra arista con su peso
            aristas[nodoA - 1].push_back({nodoB - 1,peso});
            aristas[nodoB - 1].push_back({nodoA - 1,peso});
        }

        for (int j = 0; j < cantNodos; j++){
            cin >> factorLentitud[j];
        }
        
        cout << juanYLasCletas(cantNodos,cantAristas,aristas,factorLentitud);
    }
    

    return 0;
 }


