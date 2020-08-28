####SOFTWARE PARA CONTAR CODIGO....

import glob

class contadorDeLineas:
    totalLines = 0
    emptyLines = 0
    declaredFunctions = 0
    comments = 0
    filesReaded = []

    def readFiles(self,file):
        with open(file) as file_in:
            lines = []
            for line in file_in:
                lines.append(line)
        return lines

    def readCode(self):
        file_name_list = glob.glob('*.py')
        #print(file_name_list)
        files = []
        for x in file_name_list:
            files.append(self.readFiles(x))
        #print(files)
        return files

    def contarLineasTotales(self):
        for x in self.filesReaded:
            self.totalLines += len(x)
        #print(lineasTotales)
        return self.totalLines

    def borrarLineasVacias(self):
        newFilesReaded = []
        for x in self.filesReaded:
            #print(x)
            for y in x:
                if (y != '\n'):
                    newFilesReaded.append(y)
                else:
                    self.emptyLines +=1
        #print(newFilesReaded)
        #print(len(newFilesReaded))
        #print(self.emptyLines)
        self.filesReaded = newFilesReaded

    def borrarComentarios(self):
        #TERMINAR ESTO....

        newFilesReaded = []
        for x in self.filesReaded:
            #print(x)
            esComentario = False
            for y in x:
                if (y == '#'):
                    esComentario= True
            if (esComentario):
                print(x)
                self.comments +=1
            else:
                newFilesReaded.append(x)
        # print(newFilesReaded)
        # print(len(newFilesReaded))
        # print(self.emptyLines)
        self.filesReaded = newFilesReaded


    def contarFunciones(self):
        #TERMINAR
        pass

    def toString(self):
        print("TOTAL LINES = ", self.totalLines, "  EMPTY LINES = ", self.emptyLines, "  DECLARED FUNCTIONS = ", self.declaredFunctions, "COMMENTS = ", self.comments, "codeLines = ", len(self.filesReaded),"  FILES READD = ") #, self.filesReaded)

    def leerLineas(self):
        for x in self.filesReaded:
            print(x)
        print(self.filesReaded)


def CONTAR():
    ###FUNCION ENCARGADA DE CONTAR LINEAS
    print("CONTADOR DE LINEAS/FUNCIONES")
    contador = contadorDeLineas()
    contador.filesReaded = contador.readCode()
    contador.contarLineasTotales()
    contador.borrarLineasVacias()
    contador.borrarComentarios()
    contador.toString()
    #contador.leerLineas()

if __name__ == '__main__':
    CONTAR()


