from ..TablaSimbolos.Simbolo import Simbolo
from ..TablaSimbolos.Excepcion import Excepcion
from typing import List, Dict
from ..Abstract.abstract import Abstract

class Declaracion_Array(Abstract):

    def __init__(self, ide, tipoArray, valor, fila, columna):
        self.ide = ide
        self.tipoArray = tipoArray
        self.valor = valor
        self.tipo = 'array'
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        if self.valor != None:
            lista = []
            for valor in self.valor:
                value = valor.interpretar(tree, table)
                if isinstance(value, Excepcion): return value
                simbolo = ""
                if isinstance(value,Dict):
                    simbolo = Simbolo(str(self.ide), self.valor.tipo, value['datos'], self.fila, self.columna)
                else:
                    simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.fila, self.columna)
                lista.append(simbolo)
            array = Simbolo(str(self.ide), 'array', lista, self.fila, self.columna)
            result = table.setTabla(array)
            if isinstance(result, Excepcion): return result
            return None

