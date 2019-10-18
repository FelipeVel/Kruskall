import re

###############################################################################
#Se inivializan las listas y la variable k
puntosA = []
puntosB = []
distancias = []
conjuntos = list(range(len(matriz)))
k=0

#Se llenan las litas con los datos ingresados en la matriz de adyacencia
for i in range(len(matriz)):
    for j in range (i, len(matriz)):
        if matriz[i][j] != 0 and matriz[i][j]!=99 :
            distancias.append(matriz[i][j])
            puntosA.append(i)
            puntosB.append(j)

#Se organizan las distancias de menor a mayor y se hace el ajuste en las tres listas
for i in range (len(distancias)-1):
    for j in range(i+1, len(distancias)):
        if distancias[i]>distancias[j]:
            t=distancias[i]
            distancias[i]=[j]
            distancias[j]=t
            
            t=puntosA[i]
            puntosA[i]=[j]
            puntosA[j]=t
            
            t=puntosB[i]
            puntosB[i]=[j]
            puntosB[j]=t
            
#Se inicializan los conjuntos de cada punto
for i in range(len(matriz)):
    conjuntos[k] = set([i])
    k+=1

#Se comprueba si los los puntos en la lista sean disyuntos y los une
for i in range(len(matriz)):
    if conjuntos[puntosA[i]].isdisjoint(conjuntos[puntosB[i]]) :
        conjuntos[puntosA[i]].add(conjuntos[puntosB[i]])
        conjuntos[puntosB[i]].add(conjuntos[puntosA[i]])
    
    else:
        puntosA[i]=0
        puntosB[i]=0
        distancias[i]=0
        
#Los elementos diferentes de 0 en los tres arreglos serán los aristas del grafo reccubridor 
    