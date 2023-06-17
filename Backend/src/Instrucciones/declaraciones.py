from typing import Dict
from ..TablaSimbolos.Excepcion import Excepcion
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Simbolo import Simbolo

class Declaracion_Variables(Abstract):

    def __init__(self, ide, tipo, valor, fila, columna):
        self.ide = ide # a
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        super().__init__(fila, columna)
    
    def interpretar(self, arbol, tabla):
        
        
        if self.tipo != 'array' and self.tipo != 'struct':
        # Verificacion de tipo de dato
            if self.valor == None:
                if self.tipo == 'number':
                    simbolo = Simbolo(str(self.ide), self.tipo, 0, self.fila, self.columna)
                    result = tabla.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    return None
                elif self.tipo == 'string':
                    simbolo = Simbolo(str(self.ide), self.tipo, "", self.fila, self.columna)
                    result = tabla.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    return None
                elif self.tipo == 'boolean':
                    simbolo = Simbolo(str(self.ide), self.tipo, True, self.fila, self.columna)
                    result = tabla.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    return None
                else:
                    simbolo = Simbolo(str(self.ide), self.tipo, None, self.fila, self.columna)
                    result = tabla.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    return None
            else:
                value = self.valor.interpretar(arbol, tabla)
                if isinstance(value, Excepcion): return value # Analisis Semantico -> Error
                if self.tipo == None:
                    if isinstance(value, Dict):
                        if 'datos' in value:
                            simbolo = Simbolo(str(self.ide), self.valor.tipo, value['datos'], self.fila, self.columna)
                        else:
                            simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.fila, self.columna)
                    else:
                        simbolo = Simbolo(str(self.ide), self.valor.tipo, value, self.fila, self.columna)
                    result = tabla.setTabla(simbolo)
                    if isinstance(result, Excepcion): return result
                    return None
                else:
                    if str(self.tipo) == str(self.valor.tipo) or str(self.tipo) == 'any' :
                        simbolo = Simbolo(str(self.ide), self.tipo, value, self.fila, self.columna)
                        result = tabla.setTabla(simbolo)
                        if isinstance(result, Excepcion): return result
                        return None
                    else:
                        result = Excepcion("Semantico", "Tipo de dato diferente declarado.", self.fila, self.columna)
                        return result
        #elif self.tipo == 'array':