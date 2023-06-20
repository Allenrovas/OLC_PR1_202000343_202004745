from ..Abstract.abstract import Abstract
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..TablaSimbolos.Excepcion import Excepcion


class Break(Abstract):

    def __init__(self,expresion, fila, columna):
        self.expresion = expresion
        self.value = None
        self.tipo = None
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        result = self.expresion.interpretar(arbol, tabla)
        if isinstance(result, Excepcion): return result
        self.tipo = self.expresion.tipo
        self.value = result
        return self