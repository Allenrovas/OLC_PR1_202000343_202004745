from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion

class AsignacionStruct(Abstract):

    def __init__(self, nombre, parametros, expresion, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.expresion = expresion
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        struct = table.getTabla(self.nombre)
        if struct == None:
            return Excepcion("Semantico", "Variable no encontrada.", self.fila, self.columna)
        if self.parametros == None:
            return Excepcion("Semantico", "Parametros no encontrados.", self.fila, self.columna)
        if self.expresion == None:
            return Excepcion("Semantico", "Expresion no encontrada.", self.fila, self.columna)
        value = self.expresion.interpretar(tree, table)
        if isinstance(value, Excepcion): return value
        valores = []
        for parametro in self.parametros:
            valores.append(str(parametro))
        simbolo = Simbolo(str(self.nombre), self.expresion.tipo, value, self.fila, self.columna)
        result = table.actualizarStruct(simbolo,valores)
        if isinstance(result, Excepcion): return result
        return None