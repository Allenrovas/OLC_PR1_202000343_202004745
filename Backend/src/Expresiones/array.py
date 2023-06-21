from TablaSimbolos.Simbolo import Simbolo
from TablaSimbolos.Excepcion import Excepcion
from typing import List, Dict
from Abstract.abstract import Abstract

class Array(Abstract):
    def __init__(self, ide, fila, columna, tipo, indice = None, rango = None):
        self.ide = ide
        self.tipo = tipo
        self.indice = indice
        self.rango = rango
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        if self.ide:
            simbolo = table.getTabla(self.ide)
            if simbolo == None:
                return Excepcion("Semantico", "No se encontro el simbolo: " + self.ide, self.fila, self.columna)
            