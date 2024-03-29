from flask import Flask, jsonify, request
from typing import Dict, List
import json
from AnalizadorSintactico import *
from AnalizadorLexico import *
from src.Instrucciones.funcion import Funcion
from src.TablaSimbolos.Excepcion import Excepcion
from src.Instrucciones._return import Return
from src.Instrucciones.Break import Break
from src.Instrucciones.Continue import Continue
from flask_cors import CORS
import sys
sys.setrecursionlimit(10000000)

app = Flask(__name__)
CORS(app)


def getValores(anterior):
    actual = []
    for x in anterior:
        a = x.getValor()
        if isinstance(a, List):
            value = getValores(a)
            actual.append(value)
        elif isinstance(a, Dict):
            value = getValores2(a)
            actual.append(value)
        else:
            actual.append(x.getValor())
    return actual        

def getValores2( dict):
    val = "("
    for x in dict:
        a = dict[x].getValor()
        if isinstance(a, List):
            value = getValores(a)
            val += str(value) + ", "
        elif isinstance(a, Dict):
            value = getValores2(a)
            val += str(value) + ", "
        else:
            val += str(dict[x].getValor()) + ", "
    val = val[:-2]  
    val += ")"
    return val


@app.route('/', methods=['GET'])
def rutaInicial():
    return("Ruta inicial")

@app.route('/', methods=['POST'])
def rutaPost():
    objeto = {"Mensaje":"Prueba"}
    return(jsonify(objeto))

@app.route('/analisis', methods=['POST'])
def Analizador():
    
    global entrada
    global Excepciones
    global Tabla
    global Simbolos
    data = request.get_json()
    entrada = data['entrada']
    Tabla = {}
    
    
    instrucciones = parse(entrada)
    ast = Arbol(instrucciones)
    TsgGlobal = TablaSimbolos()
    ast.setTsglobal(TsgGlobal)
    agregarNativas(ast)

    for instruccion in ast.getInstr():
        if isinstance(instruccion, Funcion):
            ast.setFunciones(instruccion)

    for instruccion in ast.getInstr():
        if not (isinstance(instruccion, Funcion)):
            value = instruccion.interpretar(ast, TsgGlobal)
            if isinstance(value, Excepcion):
                ast.setExcepciones(value)
            if isinstance(value, Return):
                err = Excepcion("Semantico", "Return fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.setExcepciones(err)
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Break fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.setExcepciones(err)
            if isinstance(value, Continue):
                err = Excepcion("Semantico", "Continue fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.setExcepciones(err)
    
    
    
    for error in errores:
        ast.setExcepciones(error)
    for x in erroressintacticos:
        ast.setExcepciones(x)
        
    Excepciones = ast.getExcepciones()
    
    Simbolos = ast.getTsglobal().getTablaG()
    consola = ast.getConsola()
    return json.dumps(consola)
    
    '''
    instrucciones = parse(entrada)
    for instruccion in instrucciones:
        instruccion.interpretar(None, None)

    return("")
    '''

@app.route('/reportes', methods=['GET'])
def Reportes():
    global Simbolos
    global Excepciones

    listasimbolos = []
    for simbolo in Simbolos:
        aux = Simbolos[simbolo].getValor()
        tipo = Simbolos[simbolo].getTipo()
        tipo = getTipo(tipo)
        fila = Simbolos[simbolo].getFila()
        columna = Simbolos[simbolo].getColumna()
        if isinstance(aux, List):
            aux = getValores(aux)
            listaaux =[]
            listaaux.append(str(simbolo))
            listaaux.append(str(aux))
            listaaux.append('array')
            listaaux.append('global')
            listaaux.append(str(fila))
            listaaux.append(str(columna))
            listasimbolos.append(listaaux)
        elif isinstance(aux, Dict):
            aux = getValores2(aux)
            listaaux =[]
            listaaux.append(str(simbolo))
            listaaux.append(str(aux))
            listaaux.append('struct')
            listaaux.append('global')
            listaaux.append(str(fila))
            listaaux.append(str(columna))
            listasimbolos.append(listaaux)   
        else:
            listaaux =[]
            listaaux.append(str(simbolo))
            listaaux.append(str(aux))
            listaaux.append(tipo)
            listaaux.append('global')
            listaaux.append(str(fila))
            listaaux.append(str(columna))
            listasimbolos.append(listaaux)   
            
            
    auxerrores = []
    for x in Excepciones:
        auxerrores.append(x.toString())  
        
        
         
    return {"Simbolos":listasimbolos, "Errores":auxerrores} 
        
def getTipo(valor):
        # Reconocer el tipo de dato del valor 
        if (type(valor) == int):
            return 'number'
        elif (type(valor) == float):
            return  'number'
        elif (type(valor) == str):
            return 'string'
        elif (type(valor) == bool):
            return 'boolean'
        elif (type(valor) == list):
            return 'array'
        elif (type(valor) == dict):
            return 'struct'
                

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)