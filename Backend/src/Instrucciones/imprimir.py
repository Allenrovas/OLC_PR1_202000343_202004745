from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from typing import Dict, List

class Imprimir(Abstract):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion # <<Class.Primitivos>>
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        #Recibe una lista 
        value = ""
        if self.expresion != None:
            for x in self.expresion:
                temporal = x.interpretar(tree,table)
                if isinstance(temporal,Excepcion):return temporal
                if isinstance(temporal, List): 
                    temporal = self.getArray(temporal)
                    if len(temporal) ==1:
                        temporal = temporal[0]
                if isinstance(temporal,dict): temporal = self.getStruct(temporal)
                value = value + str(temporal)
            tree.updateConsola(str(value))
        return None

    def getArray(self, temporalAnt):
        temporalActual = []
        for x in temporalAnt:
            actual = x.getValor()
            if isinstance(actual, List):
                valor = self.getArray(actual)
                temporalActual.append(valor)
            elif isinstance(actual, Dict):
                valor = self.getStruct(actual)
                temporalActual.append(valor)
            else:
                temporalActual.append(x.getValor())

        return temporalActual

    def getStruct(self, temporalDiccionario):
        val = "{"
        for x in temporalDiccionario:
            actual = temporalDiccionario[x].getValor()
            if isinstance(actual, List):
                value = self.getArray(actual)
                val += str(value) +", "
            elif isinstance(actual,Dict):
                value = self.getStruct(actual)
                val += str(value) + ", "
            else:
                val += str(temporalDiccionario[x].getValor()) + ", "

        val = val[:-2]
        return val