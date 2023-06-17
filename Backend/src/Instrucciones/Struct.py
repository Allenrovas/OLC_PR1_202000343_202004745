from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion

class Dec_Struct(Abstract):

    def __init__(self, nombre, fila, columna, variables= None):
        self.nombre = nombre
        self.variables = variables
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        self.tipo = 'struct'
        if self.variables:
            dict = {}
            for variable in self.variables:
                if variable.tipo:
                    simbolo = Simbolo("", variable.tipo, None, self.fila, self.columna)
                else:
                    simbolo = Simbolo("", 'any', None, self.fila, self.columna)
                dict[str(variable.ide)] = simbolo
            simbolo = Simbolo(str(self.nombre), self.tipo, dict, self.fila, self.columna)
            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion): return result
        return None
    
        
