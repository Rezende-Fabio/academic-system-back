from flask import Blueprint, jsonify, Response, flash
from ..model.dao.Schema import criaTabelas
import json

crairBancoBlueprint = Blueprint("crairBanco", __name__)

@crairBancoBlueprint.route("/criaBanco")
def criaBanco():
    if criaTabelas():
        dict = {
            "msg": "Tabelas criadas com sucesso!"
        }
        data = json.dumps(dict)
        resp = Response(data, status=200, mimetype='application/json')
    else:
        dict = {
            "msg": "Erro"
        }
        data = json.dumps(dict)
        resp = Response(data, status=500, mimetype='application/json')

    return resp