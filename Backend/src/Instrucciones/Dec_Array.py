from ..TablaSimbolos.Simbolo import Simbolo
from ..TablaSimbolos.Excepcion import Excepcion
from typing import List
from ..Abstract.abstract import Abstract

class Declaracion_Array(Abstract):

    def __init__(self, tipo, identificador, dimensiones, fila, columna):
        self.tipo = tipo
        self.identificador = identificador
        self.dimensiones = dimensiones
        self.fila = fila
        self.columna = columna