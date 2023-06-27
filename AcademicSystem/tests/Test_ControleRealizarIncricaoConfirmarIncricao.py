from AcademicSystem.controller.ControleRealizarInscricao import (
    ControleRealizarInscricao,
)
from AcademicSystem.model.entity.Horario import Horario
from AcademicSystem.model.entity.Professor import Professor
from AcademicSystem.model.entity.OfertaDisciplina import OfertaDisciplina
from AcademicSystem.model.entity.Aluno import Aluno
from AcademicSystem.model.entity.Curso import Curso
from AcademicSystem.model.entity.Disciplina import Disciplina
from datetime import date
from AcademicSystem.model.entity.Inscricao import Inscricao
from AcademicSystem.model.entity.Sala import Sala
from AcademicSystem.model.entity.Turma import Turma
import pytest
from unittest import TestCase


@pytest.fixture
def aluno():
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

    yield aluno

#Mock dos ids das ofertas que o aluno vai se increver
@pytest.fixture
def listaIdsOfertas():
    return [5, 6, 1]

class TestControleRealizarIncricaoConfirmarIncricao:

    #Verifica 
    def test_verifiaRetornoConfirmarIncricao(self, aluno, listaIdsOfertas):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.confirmarInscricao(listaIdsOfertas, aluno)
        assert respControle == True