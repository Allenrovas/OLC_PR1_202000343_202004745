from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.Excepcion import Excepcion
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..Instrucciones.Break import Break
from ..Instrucciones.Continue import Continue
from ..Instrucciones._return import Return
from ..TablaSimbolos.generador import Generador

class While(Abstract):

    def __init__(self, condicion, bloqueWhile, fila, columna):
        self.condicion = condicion
        self.bloqueWhile = bloqueWhile
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        genAux = Generador()
        generator = genAux.getInstance()
        generator.addComment("Compilacion de While")

        while True:
            print("WHILE")
            if self.getTipo():
                lb10 = generator.newLabel()
                generator.putLabel(lb10)
                condicion = self.condicion.interpretar(arbol, tabla)
                if isinstance(condicion, Excepcion): 
                    arbol.setExcepcion(condicion)
                generator.putLabel(condicion.getTrueLbl())
                
                tabla.breakLbl = condicion.getFalseLbl()
                tabla.continueLbl = lb10
                
                for instruccion in self.bloqueWhile:
                    entorno = TablaSimbolos(tabla)
                    entorno.breakLbl = condicion.getFalseLbl()
                    entorno.continueLbl = lb10
                    entorno.returnLbl = tabla.returnLbl
                    value = instruccion.interpretar(arbol, entorno)
                    if isinstance(value, Excepcion):
                        arbol.setExcepcion(condicion)
                    if isinstance(value, Break):
                       generator.addGoto(condicion.getFalseLbl())
                    if isinstance(value, Continue):
                        generator.addGoto(lb10)
                    if isinstance(value, Return):
                        if entorno.returnLbl != '':
                            if value.getTrueLbl() == '':
                                generator.addComment('Resultado a retornar en la funcion')
                                generator.setStack('P', value.getValor())
                                generator.addGoto(entorno.returnLbl)
                                generator.addComment('Fin del resultado a retornar en la funcion')
                            else:
                                generator.addComment('Resultado a retornar en la funcion')
                                generator.putLabel(value.getTrueLbl())
                                generator.setStack('P', '1')
                                generator.addGoto(entorno.returnLbl)
                                generator.putLabel(value.getFalseLbl())
                                generator.setStack('P', '0')
                                generator.addGoto(entorno.returnLbl)   
                                generator.addComment('Fin del resultado a retornar en la funcion')
                tabla.breakLbl = ''
                tabla.continueLbl = ''
                
                generator.addGoto(lb10)
                generator.putLabel(condicion.getFalseLbl())
                generator.addComment('Fin del While')
            break                    
    
    def getTipo():
        return True