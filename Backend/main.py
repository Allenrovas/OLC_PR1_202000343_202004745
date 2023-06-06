from flask import Flask, jsonify, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def rutaInicial():
    return("Un saludo a Liza Sosa")

@app.route('/', methods=['POST'])
def rutaPost():
    objeto = {"Mensaje":"Prueba"}
    return(jsonify(objeto))

@app.route('/analisis', methods=['POST'])
def Analizador():
    return("Un saludo a Liza Sosa")

@app.route('/reportes', methods=['GET'])
def Reportes():
    return("Un saludo a Liza Sosad desde reportes")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)