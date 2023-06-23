from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion

class Asignacion_Array(Abstract):
    def __init__(self,ide, indices, fila, columna, valor = None):
        self.ide = ide
        self.indices = indices
        self.valor = valor
        self.tipo = 'array'
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        if self.valor != None:
            value = self.valor.interpretar(tree, table)
            if isinstance(value, Excepcion): return value
            indices = []
            for x in range (0,len(self.indices)):
                try:
                    indice = self.indices[x].interpretar(tree,table)
                    if indice >= 0:
                        indices.append(indice)
                    else:
                        return Excepcion("Semantico", "Indice no valido", self.fila, self.columna)
                except:
                    return Excepcion("Semantico", "Indice no valido", self.fila, self.columna)
            simbolo = Simbolo(str(self.ide), self.valor.getTipo(), value, self.fila, self.columna)
            result = table.actualizarArray(simbolo,indices)
            if isinstance(result, Excepcion): return result
            return None