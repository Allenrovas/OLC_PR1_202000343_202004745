from ..TablaSimbolos.Excepcion import Excepcion
from ..Instrucciones.funcion import Funcion

class ToLowerCase(Funcion):

    def __init__(self, nombre, parametros, instrucciones,tipoReturn, fila, columna):
        self.tipo = "any"
        super().__init__(nombre, parametros, instrucciones,tipoReturn, fila, columna)

    def interpretar(self, arbol, tabla):
        simbolo = tabla.getTabla("toLower##Param1")
        if simbolo == None: return Excepcion("Semantico", "No se encontro el parametro de toLowerCase", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return simbolo.getValor().lower()