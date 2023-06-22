from ..Abstract.abstract import Abstract
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..TablaSimbolos.Excepcion import Excepcion


class Continue(Abstract):

    def __init__(self, fila, columna):
        self.fila = fila
        self.colum = columna
    
    def interpretar(self, tree, table):
        return self