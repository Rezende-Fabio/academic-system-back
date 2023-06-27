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
def insc():
    prof = Professor()
    prof.set_idProfessor(1)
    prof.set_nomeProf("Wilson Vendramel")
    prof.set_prontuario("BP123456")

    horario = Horario()
    horario.set_idHorario(1)
    horario.set_diaSemana("quarta")
    horario.set_horaInicio("19:00:00")
    horario.set_horaFim("22:35:00")
    horario.set_ativoHorario(True)

    sala = Sala()
    sala.set_idSala(1)
    sala.set_ativoSala(True)
    sala.set_local("A402")

    turma = Turma()
    turma.set_qtdeMaximaAluno(40)
    turma.set_professor(prof)
    turma.set_horario(horario)
    turma.set_sala(sala)

    # Mock da Classe Disciplina
    disciplina = Disciplina()
    disciplina.set_siglaDisc("GPR")
    disciplina.set_nomeDisc("Gestão de Projetos")
    disciplina.set_credito(4)
    disciplina.set_preRequisito([])

    oferta = OfertaDisciplina()
    oferta.set_idOferta(1)
    oferta.set_disciplina(disciplina)
    oferta.set_semestreAno("2023-1")
    oferta.set_turma(turma)
    oferta.set_ativoOferta(True)
    oferta.set_codigoOferta("teste")

    # Mock da Classe Curso
    curso = Curso()
    curso.set_duracaoCurso(6)
    curso.set_idCurso(1)
    curso.set_nomeCurso("Analise e Desenvolvimento de Sistemas")
    curso.set_siglaCurso("ADS")

    # Mock da Classe Aluno
    aluno = Aluno()
    aluno.set_idAluno(1)
    aluno.set_cpf("51050601709")
    aluno.set_dataNasc(date.today())
    aluno.set_cursoMatruculado(curso)
    aluno.set_nomeAluno("Jose Alfonso")
    aluno.set_protuarioAluno("BP301845")
    aluno.set_disciplinasConcluidas([disciplina])

    insc = Inscricao()
    insc.set_aluno(aluno)
    insc.set_dataInscricao(date.today())
    insc.set_ofertaDisciplina(oferta)

    yield insc


class TestControleRealizarIncricaoAdicionarListaEspera:
    def test_adicionarListaEspera(self, insc):
        controleRealizarInscricao = ControleRealizarInscricao()
        respControle = controleRealizarInscricao.adicionarListaEspera(insc)

        assert respControle