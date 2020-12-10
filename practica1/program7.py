import practica1.program1
import practica1.contaPalabra
import practica1.program3
import practica1.programa4
import practica1.program5
import practica1.program6
from numpy import cov
import math

import scipy.stats

def calcular_rx(dataset1, dataset2):
    rx = cov(dataset1, dataset2)
    rx = scipy.stats.pearsonr(dataset1, dataset2)
    rx = rx[0]
    return rx

def calcular_rx_cuadrada(rxy):
    rxy_cuadrada = rxy * rxy
    return rxy_cuadrada
def programa7Calc():
    print("CALCULANDO")

def calcularX(rxy, n):
    x = (abs(rxy) * math.sqrt((n - 2)) )/ (math.sqrt((1 - rxy * rxy)))
    #print(x)
    return x

def calculateProbability(x, tDistribution , distance):
    print("CALCULAR PROBABILITY")
    probability = practica1.program5.simpsonRule(0, x,tDistribution ,distance - 2)
    print(probability)
    return probability

def calcularTailArea(p):
    print("CALCULAR TAIL AREA")
    print(p)

def test1():
    print("TEST 1")
    rxy_expected = 0.954496574
    r_squared_expected = 0.91106371
    tail_area_expected = 1.77517E-05
    Bcero_expected = -22.55253275
    b_uno_expected = 1.727932426
    y_k_expected = 644.4293838
    range_expected = 230.0017197
    upi_70_expected = 874.4311035
    lpi_70_expected = 414.427664

    table1_estimatedProxy_Size = (130, 650, 99, 150, 128, 302, 95, 945, 368, 961)
    table1_plan_added_and_modified_size = (163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130)
    table_1_actual_and_modified_size = (186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
    table_1_actual_development_hours = (15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)
    programa7Calc()

    n = len(table_1_actual_development_hours) -2
    r_xy = calcular_rx(table1_estimatedProxy_Size, table_1_actual_and_modified_size)
    print("rxy ", r_xy)
    r_xy_cuadrada = calcular_rx_cuadrada(r_xy)
    print("RXY_Cuadrada ", r_xy_cuadrada)

    B_uno, Bcero, r_xy, tail_Area, std_err = scipy.stats.linregress(table1_estimatedProxy_Size, table_1_actual_and_modified_size)



    x = calcularX(r_xy, len(table_1_actual_development_hours))
    print(x)
    #probability = calculateProbability(x, tDistribution, len(table_1_actual_development_hours))

    #p = practica1.program6.testforx(x, (n - 2) ,-2, False, False )
    #print(p)

    #tailArea = calcularTailArea(probability)

    print("BUNO, BCERO, RXY, TAILAREA")
    print(B_uno, Bcero, r_xy, tail_Area)


    print("RXY EXPECTED ", rxy_expected, "r_expected    ", r_squared_expected,
          "tail_area_expected", tail_area_expected, "\nbceroExpected", Bcero_expected,
    "B_uno_expected", b_uno_expected, "y_k expected", y_k_expected,
    "\nrangeexpected", range_expected, " upi_70_expected ", upi_70_expected,
    "lpi_70 expected, ", lpi_70_expected )



def test2():
    print("TEST 2")
    rxy_expected = 0.933306898
    r_squared_expected = 0.871061766
    tail_area_expected = 7.98203E-05
    Bcero_expected = -4.038881575
    b_uno_expected = 0.16812665
    y_k_expected = 60.85800528
    range_expected = 27.55764748
    upi_70_expected = 88.41565276
    lpi_70_expected = 33.3003578
    xk = 386


    table1_estimatedProxy_Size = (130, 650, 99, 150, 128, 302, 95, 945, 368, 961)
    table1_plan_added_and_modified_size = (163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130)
    table_1_actual_and_modified_size = (186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601)
    table_1_actual_development_hours = (15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2)
    programa7Calc()


    n = len(table_1_actual_development_hours) - 2
    r_xy = calcular_rx(table1_estimatedProxy_Size, table_1_actual_development_hours)
    print("rxy ", r_xy)
    r_xy_cuadrada = calcular_rx_cuadrada(r_xy)
    print("RXY_Cuadrada ", r_xy_cuadrada)

    B_uno, Bcero, r_xy, tail_Area, std_err = scipy.stats.linregress(table1_estimatedProxy_Size,
                                                                    table_1_actual_development_hours)

    x = calcularX(r_xy, len(table_1_actual_development_hours))
    print(x)
    # probability = calculateProbability(x, tDistribution, len(table_1_actual_development_hours))

    # p = practica1.program6.testforx(x, (n - 2) ,-2, False, False )
    # print(p)

    # tailArea = calcularTailArea(probability)

    print("BUNO, BCERO, RXY, TAILAREA")
    print(B_uno, Bcero, r_xy, tail_Area)

    print("RXY EXPECTED ", rxy_expected, "r_expected    ", r_squared_expected,
          "tail_area_expected", tail_area_expected, "\nbceroExpected", Bcero_expected,
          "B_uno_expected", b_uno_expected, "y_k expected", y_k_expected,
          "\nrangeexpected", range_expected, " upi_70_expected ", upi_70_expected,
          "lpi_70 expected, ", lpi_70_expected)


def test3():
    print("TEST 3")
    rxy_expected = 0.954496574
    r_squared_expected = 0.91106371
    tail_area_expected = 1.77517E-05
    Bcero_expected = -22.55253275
    b_uno_expected = 1.727932426
    y_k_expected = 644.4293838
    range_expected = 230.0017197
    upi_70_expected = 874.4311035
    lpi_70_expected = 414.427664


    xk = 386

    programa7Calc()
    print("RXY EXPECTED ", rxy_expected, "r_expected    ", r_squared_expected,
          "tail_area_expected", tail_area_expected, "\nbceroExpected", Bcero_expected,
          "B_uno_expected", b_uno_expected, "y_k expected", y_k_expected,
          "\nrangeexpected", range_expected, " upi_70_expected ", upi_70_expected,
          "lpi_70 expected, ", lpi_70_expected )


def test4():
    print("TEST 4")
    rxy_expected = 0.954496574
    r_squared_expected = 0.91106371
    tail_area_expected = 1.77517E-05
    Bcero_expected = -22.55253275
    b_uno_expected = 1.727932426
    y_k_expected = 644.4293838
    range_expected = 230.0017197
    upi_70_expected = 874.4311035
    lpi_70_expected = 414.427664

    programa7Calc()
    print("RXY EXPECTED ", rxy_expected, "r_expected    ", r_squared_expected,
          "tail_area_expected", tail_area_expected, "\nbceroExpected", Bcero_expected,
          "B_uno_expected", b_uno_expected, "y_k expected", y_k_expected,
          "\nrangeexpected", range_expected, " upi_70_expected ", upi_70_expected,
          "lpi_70 expected, ", lpi_70_expected)

def program7():
    print("PROGRAM 7")
    test1()
    test2()
    test3()
    test4()


if __name__ == '__main__':
    program7()
