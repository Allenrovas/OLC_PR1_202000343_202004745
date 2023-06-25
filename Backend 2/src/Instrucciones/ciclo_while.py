from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones._return import Return
from ..TablaSimbolos.generador import Generador

class While(Abstract):

    def __init__(self, condicion, bloqueWhile, fila, columna):
        self.condicion = condicion
        self.bloqueWhile = bloqueWhile
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment("Compilacion de While")

       # while True: