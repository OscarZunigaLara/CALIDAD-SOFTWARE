import practica1.program5


def testforx(p, dof, possibleX, front, back):

    #print("TESTING")
    value = practica1.program5.simpsonRule(0, possibleX, 1000, dof)
    diference = p - value

    #print("POSSIBLE X   ",possibleX,"EXPECTED VALUE", p,"VALUE: " , value, "DIFFERENCE: ", diference)
    #print("ROUND ", round(value, 3))
    #print(" ASDFASDF", front, back)

    if round(value, 3) == (round(p,3)) or front and back:
        #print("ENCONTRADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        #print("POSIBLE X", possibleX)
        return possibleX

    else:
        if (diference > 0):
            possibleX += .005
            front = True
            return testforx(p, dof, possibleX, front, back)
        else:
            back = True
            possibleX -= .005
            return testforx(p, dof, possibleX, front, back)







def test1():
    print("TEST 1")
    p = 0.2
    dof = 6
    possibleX = 1
    expectedValue= 0.55338
    value = float
    value = testforx(p, dof, possibleX, False, False)
    print("EXPECTED VALUE:  ", expectedValue, "VALUE: ",value)


def test2():
    print("TEST 2")
    p = 0.45
    dof = 15
    possibleX = 1

    expectedValue = 1.75305
    value = float
    value = testforx(p, dof, possibleX, False, False)

    print("EXPECTED VALUE:  ", expectedValue, "VALUE: ", value)

def test3():
    print("TEST 3")
    dof = 4
    p = 0.495
    possibleX = 1

    expectedValue = 4.60409
    value = float
    value = testforx(p, dof, possibleX, False, False)

    print("EXPECTED VALUE:  ", expectedValue, "VALUE: ", value)


def program6():
    print("PROGRAM 6")
    test1()
    test2()
    test3()



if __name__ == '__main__':
    program6()

