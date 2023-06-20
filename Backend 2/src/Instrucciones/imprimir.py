from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from typing import Dict, List

from ..TablaSimbolos.generador import Generador
from ..Abstract.return__ import Return

class Imprimir(Abstract):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion # <<Class.Primitivos>>
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        genaux = Generador()
        generador = genaux.getInstance()
        
        
        #Recibe una lista 
        value = ''
        value = self.expresion.interpretar(tree, table)

        if isinstance(value, Excepcion): return value

        if value.getTipo() == 'number':
            generador.addPrint('f', value.getValue())
        elif value.getTipo() == 'string':
            generador.fPrintString()

            paramTemp = generador.addTemp()

            generador.addExp(paramTemp, 'P', table.size, '+')
            generador.addExp(paramTemp, paramTemp, '1', '+')
            generador.setStack(paramTemp, value.value)

            generador.newEnv(table.size)
            generador.callFun('printString')

            temp = generador.addTemp()
            generador.getStack(temp, 'P')
            generador.retEnv(table.size)