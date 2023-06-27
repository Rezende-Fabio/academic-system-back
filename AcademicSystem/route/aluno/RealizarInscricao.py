from flask import Blueprint, request, Response
from ...controller.ControleRealizarInscricao import ControleRealizarInscricao
from ...model.entity.Aluno import Aluno
from ...model.entity.Curso import Curso
from ...model.entity.Disciplina import Disciplina
import json

realizarInscricaoBlue = Blueprint("realizarInscricao", __name__)

@realizarInscricaoBlue.route("/lista-ofertas", methods=["POST"])
def listaOfertas():
    data = request.get_json()
    aluno = Aluno()
    curso = Curso()
    disciplina = Disciplina()
    aluno.toAluno(data)
    curso.toCurso(data["cursoMatriculado"])
    aluno.set_cursoMatruculado(curso)
    listaDisciplinasConc = []
    for disciplinaConc in data["disciplinasConcluidas"]:
        disciplina.toDisciplina(disciplinaConc)
        listaDisciplinasConc.append(disciplina)
    aluno.set_disciplinasConcluidas(listaDisciplinasConc)
    controleRealizarIsncricao = ControleRealizarInscricao()
    respControle = controleRealizarIsncricao.filtrarOfertas(aluno)
    listaOferta = [oferta.toJson() for oferta in respControle]
    return Response(json.dumps({"ofertas": listaOferta}), status=200, mimetype='application/json')


@realizarInscricaoBlue.route("/verifica-requisitos", methods=["POST"])
def verificarRequisitos():
    controleRealizarInscricao = ControleRealizarInscricao()
    data = request.get_json()
    respControler = controleRealizarInscricao.verificarRequisitos(data["listaIds"])
    if respControler[0] == 1:
        return Response(json.dumps({"info": "LIMITE", "msg": "Limite de crédito foi atingido."}), status=400, mimetype="application/json")
    elif respControler[0] == 2:
        return Response(json.dumps({"info": "CHOQUE", "msg": "A choque do horário entre as matérias selecionadas."}), status=400, mimetype="application/json")
    else:
        return Response(json.dumps({"ofertasDisponiveis": respControler[0], "ofertasIndisponiveis": respControler[1]}), status=200, mimetype="application/json")
    

@realizarInscricaoBlue.route("/confirma-incricao", methods=["POST"])
def cofirmarIncricao():
    controleRealizarInscricao = ControleRealizarInscricao()
    data = request.get_json()
    respControler = controleRealizarInscricao.verificarRequisitos(data["listaIds"])
    if respControler[0] == 1:
        return Response(json.dumps({"info": "LIMITE", "msg": "Limite de crédito foi atingido."}), status=400, mimetype="application/json")
    elif respControler[0] == 2:
        return Response(json.dumps({"info": "CHOQUE", "msg": "A choque do horário entre as matérias selecionadas."}), status=400, mimetype="application/json")
    else:
        return Response(json.dumps({"ofertasDisponiveis": respControler[0], "ofertasIndisponiveis": respControler[1]}), status=200, mimetype="application/json")