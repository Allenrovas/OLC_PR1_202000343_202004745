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
        if self.op == None and self.op_der == None:
            izq = self.op_izq.interpretar(tree, table)
            if isinstance(izq, Excepcion): return izq
            self.tipo = self.op_izq.tipo
            return izq
        else:   
            izq = self.op_izq.interpretar(tree, table)
            der = self.op_der.interpretar(tree, table)
            tipoIzq = self.op_izq.tipo
            tipoDer = self.op_der.tipo
            if isinstance(izq, Excepcion): return izq
            if isinstance(der, Excepcion): return der

            # SUMA

            if self.op == '+':
                if tipoIzq == 'number' and tipoDer == 'number':
                    self.tipo = 'number'
                    return izq + der
                elif tipoIzq == 'number' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq + der
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq + der
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'string' and tipoDer == 'any':
                    if isinstance(der, str):
                        self.tipo = 'string'
                        return str(str(izq) + str(der))
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'string':
                    if isinstance(izq, str):
                        self.tipo = 'string'
                        return str(str(izq) + str(der))
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'any':
                    if (isinstance(der, int) or isinstance(der, float)) and (isinstance(izq, int) or isinstance(izq, float)):
                        self.tipo = 'number'
                        return izq + der
                    elif isinstance(der, str) and isinstance(izq, str):
                        self.tipo = 'string'
                        return str(str(izq) + str(der))
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'string' and tipoDer == 'string':
                    self.tipo = 'string'
                    return str(str(izq) + str(der))
                elif tipoIzq == 'array'or tipoIzq =='struct' and tipoDer == 'array'or tipoDer =='struct':
                    
                    if isinstance(izq, int) or isinstance(izq, float) and isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq + der
                    elif isinstance(izq, str) and isinstance(der, str):
                        self.tipo = 'string'
                        return str(izq) + str(der)
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'array'or tipoIzq =='struct' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq + der
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'number' and tipoDer == 'array' or tipoDer =='struct':
                    if isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq + der
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'array' or tipoIzq =='struct' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float) and isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq + der
                    elif isinstance(der, str) and isinstance(izq, str):
                        self.tipo = 'string'
                        return str(izq) + str(der)
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'array' or tipoDer =='struct':
                    if isinstance(izq, int) or isinstance(izq, float) and isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return int(izq) + int(der)
                    elif isinstance(izq, str) and isinstance(der, str):
                        self.tipo = 'string'
                        return str(izq) + str(der)
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'array' or tipoIzq =='struct' and tipoDer == 'string':
                    if isinstance(izq, str):
                        self.tipo = 'string'
                        return str(izq) + str(der)
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
                elif tipoIzq == 'string' and tipoDer == 'array' or tipoDer =='struct':
                    if isinstance(der, str):
                        self.tipo = 'string'
                        return str(izq) + str(der)
                    else:
                        return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)

                else:
                    return Excepcion("Semantico", "Suma inválida.", self.fila, self.columna)
            # RESTA
            elif self.op == '-':
                if tipoIzq == 'number' and tipoDer == 'number':
                    self.tipo = 'number'
                    return izq - der
                elif tipoIzq == 'number' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq - der
                    else:
                        return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq - der
                    else:
                        return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'any':
                    if (isinstance(der, int) or isinstance(der, float)) and (isinstance(izq, int) or isinstance(izq, float)):
                        self.tipo = 'number'
                        return izq - der
                    else:
                        return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
                elif tipoIzq == 'array'or tipoIzq =='struct' and tipoDer == 'array'or tipoDer =='struct':
                    if ((isinstance(der,int)) or isinstance(der,float)) and ((isinstance(izq,int)) or isinstance(izq,float)):
                        self.tipo = 'number'
                        return izq - der
                    else:
                        return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
                elif tipoIzq == 'array'or tipoIzq =='struct' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq - der
                    else:
                        return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
                elif tipoIzq == 'number' and tipoDer == 'array' or tipoDer =='struct':
                    if isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq - der
                    else:
                        return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
                else:
                    return Excepcion("Semantico", "Resta inválida.", self.fila, self.columna)
            # MULTIPLICACION
            elif self.op == '*':
                if tipoIzq == 'number' and tipoDer == 'number':
                    self.tipo = 'number'
                    return izq * der
                elif tipoIzq == 'number' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq * der
                    else:
                        return Excepcion("Semantico", "Multiplicación inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq * der
                    else:
                        return Excepcion("Semantico", "Multiplicación inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'any':
                    if (isinstance(der, int) or isinstance(der, float)) and (isinstance(izq, int) or isinstance(izq, float)):
                        self.tipo = 'number'
                        return izq * der
                    else:
                        return Excepcion("Semantico", "Multiplicación inválida.", self.fila, self.columna)
                else:
                    return Excepcion("Semantico", "Multiplicación inválida.", self.fila, self.columna)
            # DIVISION
            elif self.op == '/':
                if tipoIzq == 'number' and tipoDer == 'number':
                    if der == 0:
                        return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                    self.tipo = 'number'
                    return izq / der
                if tipoIzq == 'number' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float):
                        if der == 0:
                            return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                        self.tipo = 'number'
                        return izq / der
                    else:
                        return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
                if tipoIzq == 'any' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        if der == 0:
                            return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                        self.tipo = 'number'
                        return izq / der
                    else:
                        return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
                if tipoIzq == 'any' and tipoDer == 'any':
                    if (isinstance(der, int) or isinstance(der, float)) and (isinstance(izq, int) or isinstance(izq, float)):
                        if der == 0:
                            return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                        self.tipo = 'number'
                        return izq / der
                    else:
                        return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
                else:
                    return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
            # MODULO
            elif self.op == '%':
                if tipoIzq == 'number' and tipoDer == 'number':
                    if der == 0:
                        return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                    self.tipo = 'number'
                    return izq % der
                if tipoIzq == 'number' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float):
                        if der == 0:
                            return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                        self.tipo = 'number'
                        return izq % der
                    else:
                        return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
                if tipoIzq == 'any' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        if der == 0:
                            return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                        self.tipo = 'number'
                        return izq % der
                    else:
                        return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
                if tipoIzq == 'any' and tipoDer == 'any':
                    if (isinstance(der, int) or isinstance(der, float)) and (isinstance(izq, int) or isinstance(izq, float)):
                        if der == 0:
                            return Excepcion("Semantico", "División entre 0.", self.fila, self.columna)
                        self.tipo = 'number'
                        return izq % der
                    else:
                        return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
                else:
                    return Excepcion("Semantico", "División inválida.", self.fila, self.columna)
            # POTENCIA
            elif self.op == '^':
                if tipoIzq == 'number' and tipoDer == 'number':
                    self.tipo = 'number'
                    return izq ** der
                elif tipoIzq == 'number' and tipoDer == 'any':
                    if isinstance(der, int) or isinstance(der, float):
                        self.tipo = 'number'
                        return izq ** der
                    else:
                        return Excepcion("Semantico", "Potencia inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'number':
                    if isinstance(izq, int) or isinstance(izq, float):
                        self.tipo = 'number'
                        return izq ** der
                    else:
                        return Excepcion("Semantico", "Potencia inválida.", self.fila, self.columna)
                elif tipoIzq == 'any' and tipoDer == 'any':
                    if (isinstance(der, int) or isinstance(der, float)) and (isinstance(izq, int) or isinstance(izq, float)):
                        self.tipo = 'number'
                        return izq ** der
                    else:
                        return Excepcion("Semantico", "Potencia inválida.", self.fila, self.columna)
                else:
                    return Excepcion("Semantico", "Potencia inválida.", self.fila, self.columna)


    def getTipo(self):
        return self.tipo