from collections import namedtuple
from flask import Flask, request, jsonify, make_response
import json


from flask.templating import render_template
from functions.tesouro_direto import calcular_tesouro

app = Flask(__name__)

@app.route("/tesouros", methods=["POST"])
def tesouro():
    # req = request.get_json()
    # print(req)
    Investimento = namedtuple('Investimento', ['bruto', 'total', 'imposto', "b3", "liquido"])
    # fundo = calcular_tesouro(float(req["aporteInicial"]), float(req["aporteMensal"]), "TESOURO PREFIXADO 2026")
    investimento = Investimento(1500, 2000, 500,300,100)
    # res = make_response(jsonify(investimento._asdict()), 200)
    res = make_response(jsonify(investimento._asdict()), 200)
    return res


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)