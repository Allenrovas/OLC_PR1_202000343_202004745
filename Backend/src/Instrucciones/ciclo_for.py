from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones._return import Return
from typing import List


class For(Abstract):

    def __init__(self, inicio, condicion, aumento, bloqueFor, fila, columna):
        self.inicio = inicio
        self.condicion = condicion
        self.aumento = aumento
        self.bloqueFor = bloqueFor
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        

        inicio = self.inicio.interpretar(arbol, tabla)
        if isinstance(inicio, Excepcion): return inicio

        if self.aumento != None:
            condicion = self.condicion.interpretar(arbol, tabla)
            if isinstance(condicion, Excepcion): return condicion
            # Validar que el tipo sea booleano
            if self.condicion.tipo != 'boolean':
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            # Recorriendo las instrucciones
            while condicion:
                nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO


                #Recorriendo las instrucciones
                for instruccion in self.bloqueFor:
                    result = instruccion.interpretar(arbol, nuevaTabla)
                    if isinstance(result, Excepcion):
                        arbol.excepciones.append(result)
                    if isinstance(result, Break): return None
                    if isinstance(result, Continue): break
                    if isinstance(result, Return): return result




                nuevo_valor = self.aumento.interpretar(arbol, nuevaTabla)
                if isinstance(nuevo_valor, Excepcion): return nuevo_valor


                simbolo = Simbolo(self.inicio.ide, self.inicio.tipo, nuevo_valor, self.fila, self.columna)

                # Actualizando el valor de la variable en la tabla de simbolos
                valor = nuevaTabla.updateTabla(simbolo)

                if isinstance(valor, Excepcion): return valor

                condicion = self.condicion.interpretar(arbol, tabla)
                if isinstance(condicion, Excepcion): return condicion
                if self.condicion.tipo != 'boolean':
                    return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            return None
        else:
            if not isinstance(self.condicion[0],List):
                valor = self.condicion[0].interpretar(arbol, tabla)
                if isinstance(valor, Excepcion): return valor
                if self.condicion[0].tipo == 'string':
                    valores = list(valor)
                    for x in valores:
                        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO
                        simbolo = Simbolo(self.inicio.ide, 'string', x, self.fila, self.columna)
                        # Actualizando el valor de la variable en la tabla de simbolos
                        result = nuevaTabla.setTabla(simbolo)
                        if isinstance(result, Excepcion): return result
                        #Recorriendo las instrucciones
                        for instruccion in self.bloqueFor:
                            result = instruccion.interpretar(arbol, nuevaTabla)
                            if isinstance(result, Excepcion):
                                arbol.excepciones.append(result)
                            if isinstance(result, Break): return None
                            if isinstance(result, Continue): break
                            if isinstance(result, Return): return result
                    return None
                elif self.condicion[0].tipo == 'array':
                    condicion = self.condicion[0].interpretar(arbol, tabla)
                    if isinstance(condicion, Excepcion): return condicion
                    valores = []
                    tipos = []
                    for x in condicion:
                        val = x.getValor()
                        tip = x.getTipo()
                        if isinstance(val, Excepcion): return val
                        valores.append(val)
                        tipos.append(tip)
                    result = self.CicloFor(arbol, tabla, tipos, valores)
                    return result
                else:
                    return Excepcion("Semantico", "Tipo de dato no valido en FOR.", self.fila, self.columna)
            else:
                self.condicion = self.condicion[0]
                valores = []
                tipos = []
                for x in self.condicion:
                    val = x.interpretar(arbol, tabla)
                    if isinstance(val, Excepcion): return val
                    valores.append(val)
                    tipos.append(x.tipo)
                result = self.CicloFor(arbol, tabla, tipos, valores)
                return result
            

    def CicloFor(self,tree, table, tipo, values):
        n = 0
        for x in values:
            entorno = TablaSimbolos(table)
            simbolo = Simbolo(self.inicio.ide, tipo[n],x, self.fila, self.columna)
            result = entorno.setTabla(simbolo)
            for instruccion in self.bloqueFor:
                result = instruccion.interpretar(tree, entorno)
                if isinstance(result, Excepcion):
                    tree.setExcepciones(result)
                if isinstance(result, Return): return result
                if isinstance(result, Break): return None
                if isinstance(result, Continue): break
            n += 1
        return None
        