from ..TablaSimbolos.Simbolo import Simbolo
from ..TablaSimbolos.Excepcion import Excepcion
from typing import List, Dict
from ..Abstract.abstract import Abstract

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
            if self.rango == None:
                if self.indice:
                    valores = simbolo.getValor()
                    indices = []
                    for i in self.indice:
                        indice = i.interpretar(tree, table)
                        if int(indice) > 0:
                            indices.append(int(indice))
                        else:
                            return Excepcion("Semantico", "Indice no valido", self.fila, self.columna)
                    valores = self.getValores(valores, indices)
                    return valores
                else:
                    vals = simbolo.getValor()
                    valors = []
                    for i in vals:
                        simbolo = Simbolo("",i.getTipo(), i.getValor(), i.getFila(), i.getColumna())
                        valors.append(simbolo)
                    return valors
            else:
                inicial = self.rango[0].interpretar(tree, table)
                if isinstance(inicial, Excepcion):
                    return inicial
                fin = self.rango[1].interpretar(tree, table)
                if isinstance(fin, Excepcion):
                    return fin
                if int(inicial) > int(fin):
                    return Excepcion("Semantico", "Rango no valido", self.fila, self.columna)
                if self.rango[0].tipo != 'number' or self.rango[1].tipo != 'number':
                    return Excepcion("Semantico", "Tipo de dato no valido", self.fila, self.columna)
                valores = simbolo.getValor()
                indices = []
                for i in range(int(inicial), int(fin)+1):
                    try:
                        if int(i) > 0:
                            simbolo = Simbolo("",valores[i-1].getTipo(), valores[i-1].getValor(), valores[i-1].getFila(), valores[i-1].getColumna())
                            indices.append(simbolo)
                        else:
                            return Excepcion("Semantico", "Indice no valido", self.fila, self.columna)
                    except:
                        return Excepcion("Semantico", "Indice no valido", self.fila, self.columna)
                return indices
        else:
            valores = []
            if self.rango == None:
                return Excepcion("Semantico", "No se encontro el simbolo: " + self.ide, self.fila, self.columna)
            else:
                for val in self.rango:
                    x = val.interpretar(tree, table)
                    if isinstance(x, Excepcion):
                        return x
                    simbolo = Simbolo("",val.tipo, x, self.fila, self.columna)
                    valores.append(simbolo)
                return valores
    
    def getTipo(self):
        return self.tipo
    
    def getID(self):
        return self.ide
    
    def getValores(self,anterior, indices):
        actual = anterior
        for indice in indices:
            try:
                self.tipo = actual[int(indice)-1].getTipo()
                actual = actual[int(indice)-1].getValor()
            except:
                return Excepcion("Semantico", "Indices fuera de rango", self.fila, self.columna)
        return actual 
            