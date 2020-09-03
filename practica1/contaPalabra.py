####SOFTWARE PARA CONTAR CODIGO....

import glob

class contadorDeLineas:
    totalLines = 0
    emptyLines = 0
    declaredFunctions = 0
    comments = 0
    filesReaded = []
    filesInThisFolder = 0
    classes = 0

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
        self.filesInThisFolder = len(file_name_list)
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
                #print(x)
                self.comments +=1
            else:
                newFilesReaded.append(x)
        # print(newFilesReaded)
        # print(len(newFilesReaded))
        # print(self.emptyLines)
        self.filesReaded = newFilesReaded


    def toString(self):
        print("TOTAL LINES = ", self.totalLines, "  EMPTY LINES = ", self.emptyLines, "  DECLARED FUNCTIONS = ", self.declaredFunctions, "COMMENTS = ", self.comments, "Lines of code = ", len(self.filesReaded)," \nFILES IN THIS FOLDER = ", self.filesInThisFolder, "classes", self.classes)

    def leerLineas(self):
        for x in self.filesReaded:
            print(x)
        print(self.filesReaded)

    def contarFunciones(self):
        for x in self.filesReaded:
            if ("def" in x):
                #print(x)
                self.declaredFunctions +=1

    def countClasses(self):
        for x in self.filesReaded:

            if (x[0] == 'c' and x[1] == 'l' and x[2] == 'a' and x[3] == 's' and x[3] == 's'):
                #print(x)
                self.classes +=1



def CONTAR():
    ###FUNCION ENCARGADA DE CONTAR LINEAS
    print("CONTADOR DE LINEAS/FUNCIONES")
    contador = contadorDeLineas()
    contador.filesReaded = contador.readCode()
    contador.contarLineasTotales()
    contador.borrarLineasVacias()
    contador.borrarComentarios()
    contador.contarFunciones()
    contador.countClasses()
    contador.toString()

    #contador.leerLineas()

if __name__ == '__main__':
    CONTAR()


