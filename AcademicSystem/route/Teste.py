from flask import Blueprint, jsonify, Response, flash
import json

testeBlueprint = Blueprint("teste", __name__)

@testeBlueprint.route("/")
def teste():
    dict = {
        "nome": "TESTE",
        "idade": 15,
        "cpf": "510.560.152-08"
    }
    data = json.dumps(dict)
    resp = Response(data, status=200, mimetype='application/json')
    return resp