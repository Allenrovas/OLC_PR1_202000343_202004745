from ..TablaSimbolos.Excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

class ToExponential(Funcion):

    def __init__(self, nombre, parametros, instrucciones,tipoReturn, fila, columna):
        self.tipo = "any"
        super().__init__(nombre, parametros, instrucciones,tipoReturn, fila, columna)

    def interpretar(self, arbol, tabla):
        simbolo = tabla.getTabla("toExponential##Param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de toLowerCase", self.fila, self.columna)

        simbolo2 = tabla.getTabla("toExponential##Param2")
        if simbolo2 == None: return Excepcion("Semantico", "No se encontro el parametro de toLowerCase", self.fila, self.columna)



        self.tipo = 'string'

        return "{:.{}e}".format(simbolo.getValor(),simbolo2.getValor())