import pandas
from sklearn import linear_model
import practica1.GaussianElimination


def sumList(list):
    s = 0
    for x in list:
        s = s + x
    return s

def sumCuadrada(list):
    s = 0
    for x in list:
        s = s + x * x
    return s

def sumDosListas(lista1, lista2):
    s = 0
    for x in range(len(lista1)):
        s = s + lista1[x] * lista2[x]
    return s

def multiplyAll(list):
    m = 1
    for x in list:
        m = m * x
    return m

def test1():
    LOCADDED = 650
    LOCREUSED = 3000
    LOCMODIFIED = 155

    addedLocList = [345, 168, 94, 187, 621, 255]
    reusedLocList = [65, 18, 0, 185, 87, 0]
    modifiedLocList = [23, 18, 0, 98, 10, 0]
    developmentHoursList = [31.4, 14.6, 6.4, 28.3, 42.1, 15.3]
    listaDeProgramas = []

    addedLocList = [1142, 863, 1065, 554, 983, 256]
    reusedLocList = [1060, 995, 3205, 120, 2896, 485]
    modifiedLocList = [325, 98, 23, 0, 120, 88]
    developmentHoursList = [201, 98, 162, 54, 138, 61]


    lista1 = [len(addedLocList), sumList(addedLocList), sumList(reusedLocList), sumList(modifiedLocList), sumList(developmentHoursList) ]
    lista2 = [sumList(addedLocList), sumCuadrada(addedLocList), sumDosListas(addedLocList, reusedLocList),
              sumDosListas(addedLocList, modifiedLocList), sumDosListas(addedLocList, developmentHoursList)]
    lista3 = [sumList(reusedLocList), sumDosListas(addedLocList, reusedLocList),
              sumCuadrada(reusedLocList), sumDosListas(reusedLocList, modifiedLocList), sumDosListas(reusedLocList, developmentHoursList)]
    lista4 = [sumList(modifiedLocList),sumDosListas(addedLocList,modifiedLocList),
              sumDosListas(reusedLocList, modifiedLocList), sumCuadrada(modifiedLocList), sumDosListas(modifiedLocList, developmentHoursList)]

    #print(lista1)
    #print(lista2)
    #print(lista3)
    #print(lista4)


    bcero = float
    buno     = float
    bdos = float
    btres = float
    projectedHours = float
    upi = float
    lpi = float




    listaB = practica1.GaussianElimination.gaus([lista1, lista2, lista3, lista4])
    bcero = listaB[0]
    buno = listaB[1]
    bdos = listaB[2]
    btres = listaB[3]

    projectedHours = bcero + buno * LOCADDED + bdos * LOCREUSED + btres * LOCMODIFIED

    upi = projectedHours * 1.3
    lpi = projectedHours * .7

    print("BCERO, BUNO, BDOS, BTRES, PHOURS, UPI, LPI  OBTENIDOS" )
    print(bcero, "  ", buno, "  ", bdos, "  ", btres, "   ", projectedHours, "   "
          , upi, "    ", lpi)

    bceroExpected = 0.56645
    bunoExpected = 0.06533
    bdosExpected = 0.008719
    btresExpected = 0.15105
    projectedHoursExpected = 20.76
    UPI70porciento = 28.89
    LPI70porciento = 14.63

    bceroExpected = 6.7013
    bunoExpected = 0.0784
    bdosExpected = 0.0150
    btresExpected = 0.2461
    projectedHoursExpected = 140.9
    UPI70porciento = 179.7
    LPI70porciento = 102.1

    print("BCERO, BUNO, BDOS, BTRES, PHOURS, UPI, LPI EXPECTED")
    print(bceroExpected, "  ", bunoExpected, "  ", bdosExpected, "  ",
          btresExpected, "   ", projectedHoursExpected, "   ",
          UPI70porciento, "    ", LPI70porciento)


def test2():
    LOCADDED = 650
    LOCREUSED = 3000
    LOCMODIFIED = 155

    addedLocList = [345, 168, 94, 187, 621, 255]
    reusedLocList = [65, 18, 0, 185, 87, 0]
    modifiedLocList = [23, 18, 0, 98, 10, 0]
    developmentHoursList = [31.4, 14.6, 6.4, 28.3, 42.1, 15.3]
    listaDeProgramas = []



    lista1 = [len(addedLocList), sumList(addedLocList), sumList(reusedLocList), sumList(modifiedLocList),
              sumList(developmentHoursList)]
    lista2 = [sumList(addedLocList), sumCuadrada(addedLocList), sumDosListas(addedLocList, reusedLocList),
              sumDosListas(addedLocList, modifiedLocList), sumDosListas(addedLocList, developmentHoursList)]
    lista3 = [sumList(reusedLocList), sumDosListas(addedLocList, reusedLocList),
              sumCuadrada(reusedLocList), sumDosListas(reusedLocList, modifiedLocList),
              sumDosListas(reusedLocList, developmentHoursList)]
    lista4 = [sumList(modifiedLocList), sumDosListas(addedLocList, modifiedLocList),
              sumDosListas(reusedLocList, modifiedLocList), sumCuadrada(modifiedLocList),
              sumDosListas(modifiedLocList, developmentHoursList)]

    #print(lista1)
    #print(lista2)
    #print(lista3)
    #print(lista4)

    bcero = float
    buno = float
    bdos = float
    btres = float
    projectedHours = float
    upi = float
    lpi = float

    listaB = practica1.GaussianElimination.gaus([lista1, lista2, lista3, lista4])
    bcero = listaB[0]
    buno = listaB[1]
    bdos = listaB[2]
    btres = listaB[3]

    projectedHours = bcero + buno * LOCADDED + bdos * LOCREUSED + btres * LOCMODIFIED

    upi = projectedHours * 1.3
    lpi = projectedHours * .7

    print("BCERO, BUNO, BDOS, BTRES, PHOURS, UPI, LPI OBTENIDOS")
    print(bcero, "  ", buno, "  ", bdos, "  ", btres, "   ", projectedHours, "   "
          , upi, "    ", lpi)

    bceroExpected = 0.56645
    bunoExpected = 0.06533
    bdosExpected = 0.008719
    btresExpected = 0.15105
    projectedHoursExpected = 20.76
    UPI70porciento = 28.89
    LPI70porciento = 14.63



    print("BCERO, BUNO, BDOS, BTRES, PHOURS, UPI, LPI EXPECTED")
    print(bceroExpected, "  ", bunoExpected, "  ", bdosExpected, "  ",
          btresExpected, "   ", projectedHoursExpected, "   ",
          UPI70porciento, "    ", LPI70porciento)

def programa8test():
    print("PROGRAMA 8 TEST")
    test1()
    test2()


if __name__ == '__main__':
    print("PROGRAM 8")
    programa8test()
