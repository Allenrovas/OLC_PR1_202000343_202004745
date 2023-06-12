from ..TablaSimbolos.Excepcion import Excepcion

class TablaSimbolos:

    def __init__(self, anterior = None):
        self.tabla = {} # Al inicio la tabla esta vacia
        self.anterior = anterior # Apuntador al entorno anterior
    
    def getTablaG(self):
        return self.tabla
    
    def setTabla(self, simbolo):
        # Aqui va la verificacion de que no se declare una variable dos veces
        if simbolo.getID() in self.tabla:
            return Excepcion("Semantico", "Variable ya existente en este entorno.", simbolo.getFila(), simbolo.getColumna())
        self.tabla[simbolo.getID()] = simbolo
    
    def setTablaFuncion(self, simbolo):
        self.tabla[simbolo.getID()] = simbolo

    
    
    def getTabla(self, ide): # Aqui manejamos los entornos :3
        tablaActual = self
        while tablaActual != None:
            if ide in tablaActual.tabla:
                return tablaActual.tabla[ide]
            else:
                tablaActual = tablaActual.anterior
        return None
    
    def updateTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.getID() in tablaActual.tabla:
                tablaActual.tabla[simbolo.getID()].setValor(simbolo.getValor())
                # Si necesitan cambiar el tipo de dato
                # tablaActual.tabla[simbolo.getID()].setTipo(simbolo.getTipo())
                return None
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada.", simbolo.getFila(), simbolo.getColumna())


