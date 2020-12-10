import random

random.seed(42)


n_matriz = 4
m_matriz = 5
matriz = [[0] * m_matriz for i in range(n_matriz)]

n = 6 # El total de datos que tengas len(data), data.size()...


def pivote(piv):
    temp = matriz[piv][piv]
    for y in range(n - 1):
        matriz[piv][y] = matriz[piv][y] / temp


def obtenerDiagonal(piv):
    for i in range(n - 2):
        if i != piv:
            valor = matriz[i][piv]
            for j in range(n - 1):
                matriz[i][j] = ((-1 * valor) * matriz[piv][j]) + matriz[i][j]


def obtenerResultadosMatriz():
    piv = 0
    for i in range(n - 2):
        pivote(piv)
        obtenerDiagonal(piv)
        piv += 1


def gaus(lisOfList):
    #print("Crear matriz a resolver")

    # Esta matriz contiene las sumatorias que se indican en el PDF
    # En este caso, solo son números aleatorios por simplicidad
    for i in range(4):
        for j in range(5):
            matriz[i][j] = lisOfList[i][j]

    # imprimir la matriz a resolver\
    #matriz = [addedLoc, reusedLoc,modifiedLoc, developmentHours]
    #print(matriz)




    #print("\nResolviendo la ecuacion...")
    # Mandamos a llamar esta función que resuelve la matriz
    obtenerResultadosMatriz();


    # Imprimir los resultados de la matriz (los números que aparecen a la derecha son B0, B1, etc.
    #("\nResultado")
    #print(matriz)
    listaB= []
    for x in matriz:
        listaB.append(x[-1])
    return listaB

if __name__ == '__main__':
    gaus()