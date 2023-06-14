from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos

class While(Abstract):

    def __init__(self, condicion, bloqueWhile, fila, columna):
        self.condicion = condicion
        self.bloqueWhile = bloqueWhile
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        nuevaTabla = TablaSimbolos(tabla)  # NUEVO ENTORNO


        condicion = self.condicion.interpretar(arbol, nuevaTabla)
        if isinstance(condicion, Excepcion): return condicion
        # Validar que el tipo sea booleano
        if self.condicion.tipo != 'boolean':
            return Excepcion("Semantico", "Tipo de dato no booleano en WHILE.", self.fila, self.columna)
        # Recorriendo las instrucciones
        while condicion:
            for instruccion in self.bloqueWhile:
                
                result = instruccion.interpretar(arbol, nuevaTabla)
                if isinstance(result, Excepcion):
                    arbol.excepciones.append(result)

            condicion = self.condicion.interpretar(arbol, nuevaTabla)
            if isinstance(condicion, Excepcion): return condicion
            if self.condicion.tipo != 'boolean':
                return Excepcion("Semantico", "Tipo de dato no booleano en WHILE.", self.fila, self.columna)
        return None