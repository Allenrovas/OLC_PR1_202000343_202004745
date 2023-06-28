from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.generador import Generador
from ..Abstract.return__ import Return
from ..Instrucciones.llamada_funcion import Llamada_Funcion

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
            if isinstance(izq, Excepcion): return izq
            tipoIzq = self.op_izq.tipo
            if isinstance(self.op_der, Llamada_Funcion):
                self.op_der.guardarTemps(generador, table, [izq.getValue()])
                der = self.op_der.interpretar(tree, table)
                if isinstance(der, Excepcion): return der
                self.op_der.recuperarTemps(generador, table, [izq.getValue()])
            else:
                tipoDer = self.op_der.tipo
                der = self.op_der.interpretar(tree, table)
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
                if der == 0:
                    return Excepcion("Semantico", "No se puede dividir entre 0", self.fila, self.columna)
                operador = '/'
                temporal = generador.addTemp()
                generador.addExp(temporal, izq.getValue(), der.getValue(), operador)
                self.tipo = 'number'
                return Return(temporal, self.tipo, True)   
               
            # MODULO
            elif self.op == '%':
                if der == 0:
                    return Excepcion("Semantico", "No se puede dividir entre 0", self.fila, self.columna)
                self.tipo = 'number'
                operador = '%'
                temporal = generador.addTemp()
                generador.setImport('math')
                generador.addModulo(temporal, izq.getValue(), der.getValue())
                return Return(temporal, self.tipo, True)
            # POTENCIA
            elif self.op == '^':
                self.tipo = 'number'
                operador = '^'
                temp = generador.addTemp()
                generador.fPotencia()

                t5 = generador.addTemp()

                generador.addExp(t5, 'P', table.size,'+')
                generador.addExp(t5,t5,'1','+')

                generador.setStack(t5, izq.getValue())
                generador.addExp(t5, t5,'1','+')
                generador.setStack(t5, der.getValue())

                generador.newEnv(table.size)
                generador.callFun('potencia')

                generador.getStack(temp, 'P')

                generador.retEnv(table.size)

                return Return(temporal, self.tipo, True)
               
    def getTipo(self):
        return self.tipo