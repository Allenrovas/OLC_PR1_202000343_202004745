from ..TablaSimbolos.Excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

class ToLowerCase(Funcion):

    def __init__(self, id, params, inst, tipo, fila, colum):
        super().__init__(id, params, inst, fila, colum)

    def compilar(self, tree, table):
        return