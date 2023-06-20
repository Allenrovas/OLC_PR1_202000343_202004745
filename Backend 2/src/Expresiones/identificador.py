from ..TablaSimbolos.Excepcion import Excepcion
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.generador import Generador
from ..Abstract.return__ import Return

class Identificador(Abstract):
    def __init__(self, ide, fila, columna, tipo = None):
        self.ide = ide
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def interpretar(self, arbol , tabla):
        genaux = Generador()
        generator = genaux.getInstance()
        
        generator.addComment("compilacion de acceso")
        simbolo = tabla.getTabla(self.ide)
        if simbolo == None:
            generator.addComment("Fin de compilacion de Acceso por error")
            return Excepcion("Semantico", "Variable no encontrada", self.fila, self.columna)
        # Temporal para guardar la variable
        temp = generator.addTemp()

        # Obtencion de posicion de la variable
        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')

        generator.getStack(temp, tempPos)
        generator.addComment("Fin de compilacion de Acceso")
        return Return(temp, simbolo.type, True)

    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide