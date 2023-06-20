from ..Abstract.abstract import Abstract
from ..TablaSimbolos.generador import Generador
from ..Abstract.return__ import Return
class Primitivos(Abstract):

    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo # Number, String, Boolean
        self.valor = valor # 4, 'hola', true
        self.tipoaux = ''
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        genaux = Generador()
        generador = genaux.getInstance()
        
        if self.tipo == 'number':
            return Return(str(self.valor), self.tipo, False)
        elif self.tipo == 'string':
            temporal = generador.addTemp()
            generador.addAsig(temporal, 'H')

            for char in str(self.valor):
                generador.setHeap('H', ord(char))
                generador.nextHeap()
            generador.setHeap('H', -1)
            generador.nextHeap()

            return Return(temporal, self.tipo, True)

        elif self.tipo == 'boolean':
            ''
    def getTipo(self):
        return self.tipo