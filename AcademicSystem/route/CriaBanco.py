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


@criarBancoBlueprint.route("/teste")
def teste():
    controle = ControleRealizarInscricao()
    # Mock da Classe Curso
    curso = Curso()
    curso.set_duracaoCurso(6)
    curso.set_idCurso(1)
    curso.set_nomeCurso("Analise e Desenvolvimento de Sistemas")
    curso.set_siglaCurso("ADS")

    # Mock da Classe Disciplina que o aluno concluiu
    disciplina = Disciplina()
    disciplina.set_siglaDisc("GPR")
    disciplina.set_nomeDisc("Gestão de Projetos")
    disciplina.set_credito(4)
    disciplina.set_preRequisito([])

    # Mock da Classe Aluno
    aluno = Aluno()
    aluno.set_idAluno(1)
    aluno.set_cpf("51050601709")
    aluno.set_dataNasc(date.today())
    aluno.set_cursoMatruculado(curso)
    aluno.set_nomeAluno("Jose Alfonso")
    aluno.set_protuarioAluno("BP301845")
    aluno.set_disciplinasConcluidas([disciplina])

    controle.adicionarListaEspera(6, aluno)