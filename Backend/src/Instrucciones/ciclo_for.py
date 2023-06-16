from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones._return import Return


class For(Abstract):

    def __init__(self, inicio, condicion, aumento, bloqueFor, fila, columna):
        self.inicio = inicio
        self.condicion = condicion
        self.aumento = aumento
        self.bloqueFor = bloqueFor
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO

        inicio = self.inicio.interpretar(arbol, nuevaTabla)
        if isinstance(inicio, Excepcion): return inicio

        condicion = self.condicion.interpretar(arbol, nuevaTabla)
        if isinstance(condicion, Excepcion): return condicion
        # Validar que el tipo sea booleano
        if self.condicion.tipo != 'boolean':
            return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
        # Recorriendo las instrucciones
        while condicion:
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

            condicion = self.condicion.interpretar(arbol, nuevaTabla)
            if isinstance(condicion, Excepcion): return condicion
            if self.condicion.tipo != 'boolean':
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
        return None