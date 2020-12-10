import math

class practica3():
    tablaEstimatedProxy = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
    tablaAddedAndModified = [163, 765, 141, 166, 137, 355, 136, 1206, 433, 1130]
    tablaActualAndModified = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    tablaActualDevelopmentHours = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]

    n = 0
    x = 0
    y = 0
    xx  = 0
    yy = 0
    xy = 0
    xav = 0
    yav = 0

    b1 =0
    b0 = 0
    rxy = 0
    rr = 0
    prox = 0

    def calculateVariance(self):
        for i in self.tablaEstimatedProxy:
            print(i)
            self.x += self.tablaEstimatedProxy[0]
            self.y += self.tablaEstimatedProxy[0]
            self.xx += self.x * self.x
            self.yy += self.y * self.y
            self.xy += self.x * self.y

        self.xav = self.x/len(self.tablaAddedAndModified)
        self.yav = self.y / len(self.tablaAddedAndModified)
        self.n = len(self.tablaAddedAndModified)

    def calculateParameters(self):
        self.b1 = ((self.xy - (self.n * self.xav * self.yav))/ (self.xx - self.n * math.pow(self.xav, 2)))
        self.b0 = self.yav - (self.b1 * self.xav)
    def calculateCorrelation(self):
        self.rxy = (self.n * self.xy - (self.x * self.y))/\
                   math.sqrt((self.n * self.xx - math.pow(self.x, 2)) * (self.n * self.yy - math.pow(self.y, 2)))

    def calculatePrediction(self):
        self.x = 386.0
        self.prox = self.b0 + (self.b1 * self.x)

    def printTest(self):
        print("B0 ", self.b0)
        print("B1 ", self.b1)
        print("RXY ", self.rxy)
        print("Rcuadrada ", self.rr)
        print("prxy ",self.prox )

    def test1(self):
        self.calculateVariance(self)
        self.calculateParameters(self)
        self.calculateCorrelation(self)
        self.calculatePrediction(self)
        self.printTest(self);


if __name__ == '__main__':
    print("PRACTICA 3")
    prac3 = practica3
    prac3.test1(prac3)
  
