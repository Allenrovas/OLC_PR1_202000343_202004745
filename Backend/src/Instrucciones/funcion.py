from ..Instrucciones._return import Return
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos


class Funcion(Abstract):

    def __init__(self, nombre, parametro, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametro = parametro
        self.instrucciones = instrucciones
        self.tipo = None
        super().__init__(fila, columna)


    def interpretar(self, arbol, tabla):
        entorno = TablaSimbolos(tabla)
        for instruccion in self.instrucciones:
            value = instruccion.interpretar(arbol, entorno)
            if isinstance(value, Excepcion): return value
            if isinstance(value, Return):
                self.tipo = value.tipo
                return value.value
        return None
