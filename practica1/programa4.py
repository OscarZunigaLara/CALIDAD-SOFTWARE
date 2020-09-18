import numpy
import math


class programa4():
    classLocList = []
    noMethodsList = []
    lockMethod = []
    lnxi = []
    totalLnxi = 0
    averageLNXI = 0
    variance = 0
    lnxiMenosAverage = []
    standardDeviation = 0

    vs = 0
    s = 0
    m = 0
    l = 0
    vl = 0

    def test1(self):
        print("TEST 1")
        self.classLocList = [18, 18, 25, 31, 37, 82, 82, 87, 89, 230, 85, 87, 558]
        self.noMethodsList = [3, 3, 3, 3, 3, 5, 4, 4, 4, 10, 3, 3, 10]
        self.paso1()
        self.paso2()
        self.paso3()
        self.paso4()
        self.paso5()
        self.paso6()
        self.paso7()
    def paso1(self):
        for i in range(len(self.classLocList)):
            # print(self.clasLocList[i])
            # print(self.noMethodsList[i])
            # print(self.clasLocList[i], "  ", self.noMethodsList[i], "   ", self.clasLocList[i] / self.noMethodsList[i])
            self.lockMethod.append(self.classLocList[i] / self.noMethodsList[i])
        print(self.lockMethod)

    def paso2(self):
        for i in self.lockMethod:
            self.lnxi.append(numpy.log(i))
        for i in self.lnxi:
            self.totalLnxi += i
        print(self.lnxi, "  ", self.totalLnxi)
        print("TOTAL LNXI = ", self.totalLnxi)

    def paso3(self):
        self.averageLNXI = self.totalLnxi / len(self.lnxi)
        print("AVERAGE LNXI = ", self.averageLNXI)

    def paso4(self):
        for i in self.lnxi:
            self.lnxiMenosAverage.append((i - self.averageLNXI) * (i - self.averageLNXI))
        print(self.lnxiMenosAverage)
        self.variance = sum(self.lnxiMenosAverage) / (len(self.lnxi) - 1)
        print("variance ", self.variance)

    def paso5(self):
        self.standardDeviation = math.sqrt(self.variance)
        print("Standard Deviation   ", self.standardDeviation)

    def paso6(self):
        self.vs = self.averageLNXI - 2 * self.standardDeviation
        self.s = self.averageLNXI - self.standardDeviation
        self.m = self.averageLNXI
        self.l = self.averageLNXI  + self.standardDeviation
        self.vl = self.averageLNXI + 2 * self.standardDeviation

        print("VS = ", self.vs)
        print("S  = ", self.s)
        print("M  = ", self.m)
        print("L  = ", self.l)
        print("VL = ", self.vl)

    def paso7(self):

        self.vs = (math.exp(self.vs))
        self.s = math.exp(self.s)
        self.m = math.exp(self.m)
        self.l = math.exp(self.l)
        self.vl = math.exp(self.vl)

        print("VS = ", self.vs)
        print("S  = ", self.s)
        print("M  = ", self.m)
        print("L  = ", self.l)
        print("VL = ", self.vl)

    def programa4(self, dic):
        self.paso1()
        pass


if __name__ == '__main__':
    print("PROGRAMA 4")
    test = programa4()
    test.test1()
