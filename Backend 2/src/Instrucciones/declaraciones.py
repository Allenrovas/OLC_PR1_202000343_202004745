from typing import Dict
from ..TablaSimbolos.Excepcion import Excepcion
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Simbolo import Simbolo
from ..TablaSimbolos.generador import Generador
from ..Abstract.return__ import Return


class Declaracion_Variables(Abstract):

    def __init__(self, ide, tipo, valor, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        self.find = True
        self.ghost = -1
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()

        generator.addComment('Compilacion de valor de variable')
        value = self.valor.interpretar(arbol, tabla)
        if isinstance(value, Excepcion): return value # Analisis Semantico -> Error
        # Verificacion de tipos
        if str(self.tipo) == str(self.valor.tipo):
            inHeap = value.getTipo() == 'string' or value.getTipo() == 'interface'
            simbolo = tabla.setTabla(self.ide, value.getTipo(), inHeap , self.find)
        else:
            generator.addComment('Error, tipo de dato diferente declarado.')
            result = Excepcion("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
            return result

        tempPos = simbolo.pos
        if not simbolo.isGlobal:
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', simbolo.pos, '+')

        generator.setStack(tempPos, value.value)
        generator.addComment('Fin de compilacion de valor de variable')