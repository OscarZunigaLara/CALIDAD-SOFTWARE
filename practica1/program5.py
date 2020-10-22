import math




def gamma(n):
    #print("n", n)
    #print(n)
    #print(round(n))

    if round(n) == n:
        n = round(n) - 1
        fact = 1
        for num in range(2, n + 1):
            fact = fact * num

        return fact

    if round(n) != n:
        fact = n - 1
        factList = [fact]
        while(fact > 1):
           factList.append(fact - 1)
           fact -= 1
        factList.append(math.pow(math.pi, .5))
        #print(factList)
        fact = 1
        for x in factList:
            fact = fact * x
        #print("fact", fact)
        return (fact)


def simpsonRule(x0, xf,setNumSeg,dof):
   #print("Simpson Rule")

    w = xf / setNumSeg

    xiList = []
    for x in range(setNumSeg + 1):
        xiList.append(x * xf/setNumSeg)
    #print(xiList)
    unomasx1 = []

    for x in range(setNumSeg + 1):
        #print(1 + xiList[x] * xiList[x] / dof)
        unomasx1.append(1 + xiList[x] * xiList[x] / dof)
    #print(unomasx1)

    unomasx1elevado = []
    for x in range(setNumSeg + 1):
       #print(pow(unomasx1[x], (- (dof + 1)/2)))
       unomasx1elevado.append(pow(unomasx1[x], (- (dof + 1)/2)))
    #print(unomasx1elevado)

    tabla4 = []
    for x in range(setNumSeg + 1):
        x = (gamma((dof + 1)/2))
        y = (math.pow((dof * math.pi), .5))
        z = (gamma(dof/2))

        tabla4.append(x / (y * z))

    #print(tabla4)

    tabla5 = []
    for x in range(setNumSeg + 1):
        dato = math.pow((1 + xiList[x] * xiList[x]/dof), (- (dof + 1)/2))
        tabla5.append(tabla4[x] * dato)
    #print(tabla5)

    multiplier = [1]

    for x in range(setNumSeg - 1):
        if x %2 == 0:
            multiplier.append(4)
        else:
            multiplier.append(2)

    multiplier.append(1)
    #print(multiplier)

    terms = []
    for x in range(setNumSeg + 1):
        terms.append(w/ 3 * multiplier[x] * tabla5[x])

    #print(terms)
    resultado = 0

    for x in terms:
        resultado += x


    #print("F0   ",F0, "     FX: ", FX, "    primersum", primerSum, "    segundasum", segundaSum, "w", w)
    #print(resultado)
    return resultado




def test1():
    print("TEST 1")
    dof = 9
    expectedValue= 0.35006
    x1 = 0
    x2 = 1.1
    setNumSeg = 10

    value = simpsonRule(x1, x2, setNumSeg, dof )
    print("EXPECTED VALUE:  ", expectedValue, "VALUE: ",value)


def test2():
    print("TEST 2")
    dof = 10
    expectedValue= 0.36757
    x1 = 0
    x2 = 1.1812
    setNumSeg = 10

    value = simpsonRule(x1, x2, setNumSeg, dof)
    print("EXPECTED VALUE:  ", expectedValue, "VALUE: ", value)

def test3():
    print("TEST 3")
    dof = 30
    expectedValue = 0.49500
    x1 = 0
    x2 = 2.75
    setNumSeg = 10

    value = simpsonRule(x1, x2, setNumSeg, dof)
    print("EXPECTED VALUE:  ", expectedValue, "VALUE: ", value)


def program5():
    test1()
    test2()
    test3()


if __name__ == '__main__':
    print("PROGRAM 5")
    program5()


