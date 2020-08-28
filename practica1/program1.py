##PROGRAMA1:
import math


def leerNumeros(tamanoDeLista):
    #Funcion encargada de leer una serie de numeros
    listaDeNumeros= []
    for x in range(0,tamanoDeLista):
        listaDeNumeros.append(float(input("InserteNumero")))
    return listaDeNumeros

def calcularMedia(lista):
    total = 0
    for x in lista:
        total += x
    #print("TOTAL =", total, "SIZE = ", len(lista))
    media = total/len(lista)
    return media

def calcularDesviacionEstandar(lista):
    desviacionEstandar = 0
    media = calcularMedia(lista)
    for x in lista:
        desviacionEstandar += (x-media)**2
    desviacionEstandar = desviacionEstandar/ len(lista)
    desviacionEstandar = math.sqrt(desviacionEstandar)
    return desviacionEstandar

def programa1():
    print("MEDIA Y DESVIACION STANDARD")
    tamanoDeLista = (input("INSERTA TAMANO DE LISTA"))
    tamanoDeLista = int(tamanoDeLista)
    listaDeNumeros = leerNumeros(tamanoDeLista)
    print(listaDeNumeros)
    media = calcularMedia(listaDeNumeros)
    print("MEDIA = ", media)
    desviacionEstandar = calcularDesviacionEstandar(listaDeNumeros)
    print("DESVIACION ESTANDAR = " , desviacionEstandar )

if __name__ == '__main__':
    print("PROGRAMA 1")
    programa1()

