from ..Instrucciones._return import Return
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue


class Funcion(Abstract):

    def __init__(self, nombre, parametros, instrucciones, tipoReturn , fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipoReturn = tipoReturn
        self.tipo = None
        super().__init__(fila, columna)


    def interpretar(self, arbol, tabla):
        entorno = TablaSimbolos(tabla)
        for instruccion in self.instrucciones:
            value = instruccion.interpretar(arbol, entorno)
            if isinstance(value, Excepcion): return value
            if isinstance(value, Return):
                if value.tipo == self.tipoReturn:
                    self.tipo = value.tipo
                    return value.value
                else:
                    if value.tipo == None and self.tipoReturn == None:
                        self.tipo = value.tipo
                        return value.value
                    elif self.tipoReturn == 'any':
                        self.tipo = 'any'
                        return value.value
                    else:
                        return Excepcion("Semantico", "El tipo de retorno no coincide con el tipo de la funcion", self.fila, self.columna)

                #self.tipo = value.tipo
                #return value.value
            if isinstance(value, Break): return Excepcion("Semantico", "Sentencia break fuera de ciclo", value.fila, value.columna)
            if isinstance(value, Continue): return Excepcion("Semantico", "Sentencia continue fuera de ciclo", value.fila, value.columna)
        return None
