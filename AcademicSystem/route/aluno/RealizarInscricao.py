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