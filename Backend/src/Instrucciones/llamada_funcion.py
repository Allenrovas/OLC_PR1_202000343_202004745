
from ..TablaSimbolos.Simbolo import Simbolo
from ..Abstract.abstract import Abstract
from ..TablaSimbolos.TablaSimbolos import TablaSimbolos
from ..TablaSimbolos.Excepcion import Excepcion


class Llamada_Funcion(Abstract):

    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.tipo = None
        super().__init__(fila, columna)

    def interpretar(self, arbol, tabla):
        result = arbol.getFuncion(self.nombre)
        esFuncion = True

        if result == None:
            struct = arbol.getTabla(self.nombre)
            if struct == None:
                return Excepcion("Semantico", "No se encontro la funcion: " + str(self.nombre), str(self.fila), str(self.columna))
            else:
                esFuncion = False
        if esFuncion:
            entorno = TablaSimbolos(arbol.getTsglobal())
            if len(self.parametros) == len(result.parametros):
                contador = 0
                for expresion in self.parametros:
                    resultE = expresion.interpretar(arbol, tabla)
                    if isinstance(resultE, Excepcion): return resultE
                    if result.parametros[contador]['tipo'] == expresion.tipo:
                        simbolo = Simbolo(str(result.parametros[contador]['id']), result.parametros[contador]['tipo'], resultE, self.fila, self.columna)

                        resultT = entorno.setTablaFuncion(simbolo)
                        if isinstance(resultT, Excepcion): return resultT
                    elif result.parametros[contador]['tipo'] == 'any' or expresion.tipo == 'any':
                        simbolo = Simbolo(str(result.parametros[contador]["id"]), expresion.tipo, resultE, self.fila, self.columna)
                        resultT = entorno.setTablaFuncion(simbolo)
                    else:
                        return Excepcion("Semantico", "Tipo de dato diferente en Parametros", str(self.fila), str(self.columna))
                    contador += 1
            else:
                return Excepcion("Semantico", "Numero de parametros incorrectos", str(self.fila), str(self.columna))

            value = result.interpretar(arbol, entorno) # me puede retornar un valor

            if isinstance(value, Excepcion): return value
            self.tipo = result.tipo
            return value
        else:
            struct = tabla.getTabla(self.nombre)
            dict = struct.getValor()
            diccionario = {}
            list = []
            tipos = []
            for parametros in self.parametros:
                result = parametros.interpretar(arbol, tabla)
                if parametros.tipo == None:
                    simbolo = Simbolo("",'any',result,self.fila,self.columna)
                    tipos.append('any')
                else:
                    simbolo = Simbolo("",parametros.tipo,result,self.fila,self.columna)
                    tipos.append(parametros.tipo)
                list.append(simbolo)
            self.tipo = 'struct'
            for x in dict:
                if dict[x].getTipo() == 'any':
                    diccionario[x] = list[0]
                elif dict[x].getTipo() == tipos[0]:
                    diccionario[x] = list[0]
                else:
                    return Excepcion("Semantico", "Tipo de dato diferente en Parametros", str(self.fila), str(self.columna))
                list.pop(0)
                tipos.pop(0)
            if len(list) > 0:
                return Excepcion("Semantico", "Numero de parametros incorrectos", str(self.fila), str(self.columna))
            aux = {'datos':diccionario}
            return aux
            