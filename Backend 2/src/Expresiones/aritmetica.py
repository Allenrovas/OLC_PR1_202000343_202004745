from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.generador import Generador
from ..Abstract.return__ import Return

class Aritmetica(Abstract):

    def __init__(self, op_izq, op_der, op, fila, columna):
        self.op_izq = op_izq #
        self.op_der = op_der #
        self.op = op # *
        self.tipo = None
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table):
        genaux = Generador()
        generador = genaux.getInstance()
        temporal = ''
        operador = ''
        
        
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
                
                self.tipo = 'number'
                operador = '+'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                return Return(temporal, self.tipo, True)                            
            # RESTA
            elif self.op == '-':
                self.tipo = 'number'
                operador = '-'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                return Return(temporal, self.tipo, True)    
               
            # MULTIPLICACION
            elif self.op == '*':
                self.tipo = 'number'
                operador = '*'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                return Return(temporal, self.tipo, True)    
              
            # DIVISION
            elif self.op == '/':
                self.tipo = 'number'
                operador = '/'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                return Return(temporal, self.tipo, True)    
               
            # MODULO
            elif self.op == '%':
                self.tipo = 'number'
                operador = '%'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                return Return(temporal, self.tipo, True)
            # POTENCIA
            elif self.op == '^':
                self.tipo = 'number'
                operador = '^'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                return Return(temporal, self.tipo, True)    
               
    def getTipo(self):
        return self.tipo