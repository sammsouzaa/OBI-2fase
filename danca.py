n, m, c = list(map(int, input().split()))
contador = 1
matriz = []
for i in range(n):
    aux = []
    for j in range(m):
        aux.append(contador)
        contador = contador+1
    matriz.append(aux)
    
for i in range(c):
    comando, sA, sB = input().split()
    a = int(sA) - 1
    b = int(sB) - 1
    
    if(comando == 'L'):
        aux = []
        aux = matriz[a]
        matriz[a] = matriz[b]
        matriz[b] = aux
        
    else:
        for i in range(n):
            aux = 0
            aux = matriz[i][a]
            matriz[i][a] = matriz[i][b]
            matriz[i][b] = aux

for i in range(n):
    for j in range(m):
        print(matriz[i][j], end=" ")
        if (j == (m-1)):
            print()
        else:
            print(" ", end="")

# matriz2 = str(matriz)
# print(matriz2)

print(" ".join(str(matriz)))
