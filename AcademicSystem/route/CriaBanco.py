from datetime import date
from flask import Blueprint, jsonify, Response, flash
from ..model.dao.Schema import criaTabelas
import json

from ..controller.ControleRealizarInscricao import ControleRealizarInscricao
from ..model.entity.Aluno import Aluno
from ..model.entity.Disciplina import Disciplina
from ..model.entity.Curso import Curso

criarBancoBlueprint = Blueprint("criarBancoBlueprint", __name__)

@criarBancoBlueprint.route("/criaBanco")
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