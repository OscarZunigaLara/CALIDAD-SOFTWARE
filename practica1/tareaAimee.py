def sumatoria(n):
    suma = 0
    for i in range(n):
        suma += 1 / (i* 3-1)
    print("n = ", n, " suma = ", suma)

if __name__ == '__main__':
    sumatoria(1000)