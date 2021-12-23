from collections import namedtuple
from flask import Flask, request, jsonify, make_response
import json


from flask.templating import render_template
from flask_cors import CORS, cross_origin
from functions.tesouro_direto import calcular_tesouro, getTitulos

app = Flask(__name__)
CORS(app)

@app.route("/tesouros", methods=["POST"])
def tesouro():
    try:
        req = request.get_json()
        Investimento = namedtuple('Investimento', ['bruto', 'total', 'imposto', "b3", "liquido"])
        fundo = calcular_tesouro(float(req["aporteInicial"]), float(req["aporteMensal"]), "Tesouro Prefixado 2026")
        investimento = Investimento(fundo[0], fundo[1], fundo[2],
                                    fundo[3], fundo[4])
        res = make_response(jsonify(investimento._asdict()), 200)
        return res
    except:
        return make_response(jsonify({}),500)


@app.route("/titulos", methods=['GET'])
def titulos():
    titulos = getTitulos()['Título']
    titulos_json = []
    for titulo in titulos:
        titulos_json.append(titulo)
    return jsonify(titulos_json)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)