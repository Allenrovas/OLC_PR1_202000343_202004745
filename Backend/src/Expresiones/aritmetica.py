from ..Abstract.abstract import Abstract

class Aritmetica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq
        self.op_der = op_der
        self.op = op
        super().__init__(fila, columna)

    def interpretar(self, tree, table):
        izq = self.op_izq.interpretar(tree, table)
        tipo_izq = self.op_izq.getTipo()
        der = self.op_der.interpretar(tree, table)
        tipo_der = self.op_der.getTipo()
        if self.op == '+':
            if tipo_izq == 'number' and tipo_der == 'number':
                return izq + der
            elif tipo_izq == 'string' and tipo_der == 'string':
                return izq + der
            else:
                return 'Error: Tipo de dato invalido en suma'
        elif self.op == '-':
            if tipo_izq == 'number' and tipo_der == 'number':
                return izq - der
            else:
                return 'Error: Tipo de dato invalido en resta'
        elif self.op == '*':
            if tipo_izq == 'number' and tipo_der == 'number':
                return izq * der
            else:
                return 'Error: Tipo de dato invalido en multiplicacion'
        elif self.op == '/':
            if der == 0:
                return 'Error: Division entre 0'
            if tipo_izq == 'number' and tipo_der == 'number':
                return izq / der
            else:
                return 'Error: Tipo de dato invalido en division'
            