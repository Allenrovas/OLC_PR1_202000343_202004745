from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion

class Aritmetica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq #
        self.op_der = op_der #
        self.op = op # *
        self.tipo = None
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        izq = self.op_izq.interpretar(tree, table)
        der = self.op_der.interpretar(tree, table)
        tipoIzq = self.op_izq.getTipo()
        tipoDer = self.op_der.getTipo()

        # SUMA
        if self.op == '+':
            if tipoIzq == 'number' and tipoDer == 'number':
                self.tipo = 'number'
                return izq + der
            elif tipoIzq == 'string' and tipoDer == 'string':
                self.tipo = 'string'
                return str(str(izq) + str(der))
            else:
                return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
        # RESTA
        elif self.op == '-':
            if tipoIzq == 'number' and tipoDer == 'number':
                self.tipo = 'number'
                return izq - der
            else:
                return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
        # MULTIPLICACION
        elif self.op == '*':
            if tipoIzq == 'number' and tipoDer == 'number':
                self.tipo = 'number'
                return izq * der
            else:
                return Excepcion("Semantico", "Multiplicación inválida.", self.fila, self.columna)
        # DIVISION
        elif self.op == '/':
            if tipoIzq == 'number' and tipoDer == 'number':
                if der == 0:
                    return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                self.tipo = 'number'
                return izq / der
            else:
                return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
        # MODULO
        elif self.op == '%':
            if tipoIzq == 'number' and tipoDer == 'number':
                if der == 0:
                    return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                self.tipo = 'number'
                return izq % der
            else:
                return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
        # POTENCIA
        elif self.op == '^':
            if tipoIzq == 'number' and tipoDer == 'number':
                self.tipo = 'number'
                return izq ** der
            else:
                return Excepcion("Semantico", "Potencia inválida.", self.fila, self.columna)

    def getTipo(self):
        return self.tipo