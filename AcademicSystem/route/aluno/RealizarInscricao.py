from flask import Blueprint, request
from ...controller.ControleRealizarInscricao import ControleRealizarInscricao

realizarInscricaoBlue = Blueprint("realizarInscricao", __name__)

@realizarInscricaoBlue.route("/lista-ofertas", methods=["POST"])
def listaOfertas():
    data = request.get_json()
    return {"teste": 15}