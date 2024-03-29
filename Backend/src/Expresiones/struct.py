from ..TablaSimbolos.Simbolo import Simbolo
from ..TablaSimbolos.Excepcion import Excepcion
from typing import List
from ..Abstract.abstract import Abstract

class Struct(Abstract):
    def __init__(self, ide, parametros,fila, columna):
        self.ide = ide
        self.fila = fila
        self.colum = columna
        self.parametros = parametros
    
    def interpretar(self, tree, table):
        struct = table.getTabla(self.ide)
        if struct == None:
            return Excepcion("Semantico", "struct no encontrado", self.fila, self.colum)
        claves = []
        for clave in self.parametros:
            claves.append(clave)
        valor = self.getValores(struct.getValor(), claves)

        return valor
        
    def getValores(self, anterior, claves):
        actual = anterior
        for clave in claves:
            try:
                self.tipo = actual[str(clave)].getTipo()
                actual = actual[str(clave)].getValor()
            except:
                return Excepcion("Semantico", "Valores no encontrados", self.fila, self.colum)
        return actual
    
    def getTipo(self):
        return self.tipo