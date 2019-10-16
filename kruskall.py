import re

###############################################################################

puntosA = []
puntosB = []
distancias = []
conjuntos = list(range(len(matriz)))

for i in range(len(matriz)):
    for j in range (i, len(matriz)):
        if matriz[i][j] != 0 and matriz[i][j]!=99 :
            distancias.append(matriz[i][j])
            puntosA.append(i)
            puntosA.append(j)

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
            
conjuntos