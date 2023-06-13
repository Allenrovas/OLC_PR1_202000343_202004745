from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..Abstract.abstract import Abstract

class Asignacion(Abstract):
    def __init__(self, identificador, valor, fila, columna):
        self.identificador = identificador
        self.valor = valor
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador)
        if simbolo == None:
            return Excepcion("Semantico", "Variable no encontrada.", self.fila, self.columna)
        if self.valor == None:
            return Excepcion("Semantico", "Valor de asignacion no encontrado.", self.fila, self.columna)
        exp = self.valor.interpretar(tree, table)
        if self.valor.tipo != simbolo.getTipo():
            return Excepcion("Semantico", "Tipo de dato diferente en Asignacion.", self.fila, self.columna)
        simbolo.setValor(exp)
        return None
