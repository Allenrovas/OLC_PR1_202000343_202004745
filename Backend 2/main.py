from flask import Flask, jsonify, request
import json
from AnalizadorSintactico import *

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def rutaInicial():
    return("Ruta inicial")

@app.route('/', methods=['POST'])
def rutaPost():
    objeto = {"Mensaje":"Prueba"}
    return(jsonify(objeto))

@app.route('/analisis', methods=['POST'])
def Analizador():
    data = request.get_json()
    entrada = data['entrada']
    

    instrucciones = parse(entrada)
    for instruccion in instrucciones:
        instruccion.interpretar(None, None)

    

    return("")

@app.route('/reportes', methods=['GET'])
def Reportes():
    return("Reportes")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)