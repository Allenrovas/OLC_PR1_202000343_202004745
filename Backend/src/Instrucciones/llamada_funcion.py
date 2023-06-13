
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..TablaSimbolos.Excepcion import Excepcion


class Llamada_Funcion(Abstract):

    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.tipo = None
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        result = arbol.getFuncion(self.nombre)
        if result == None:
            return Excepcion("Semantico", "No se encontro la funcion: " + str(self.nombre), str(self.fila), str(self.columna))
        entorno = TablaSimbolos(arbol.getTsglobal())
        # if len(self.parametros) == len(result.parametros):
        #     # aqui se hace la declaracion de los parametros
        #     pass

        value = result.interpretar(arbol, entorno) # me puede retornar un valor

        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo
        return value