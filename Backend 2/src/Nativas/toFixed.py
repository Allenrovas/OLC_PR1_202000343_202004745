from ..TablaSimbolos.Excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

from ..TablaSimbolos.Excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

class ToFixed(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.tipo = "any"
        super().__init__(nombre, parametros, instrucciones, fila, columna)

    def interpretar(self, arbol, tabla):
        simbolo = tabla.getTabla("toFixed##Param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de toLowerCase", self.fila, self.columna)

        simbolo2 = tabla.getTabla("toFixed##Param2")
        if simbolo2 == None: return Excepcion("Semantico", "No se encontro el parametro de toLowerCase", self.fila, self.columna)



        self.tipo = simbolo.getTipo()
        return round(simbolo.getValor(),simbolo2.getValor())