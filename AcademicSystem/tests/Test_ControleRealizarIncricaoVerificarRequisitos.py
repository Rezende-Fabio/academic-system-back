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

#Mock da lista de ids que seram enviados para função de verificarRequisitos
@pytest.fixture
def listaIdOfertas():
    return [1, 5, 6]

#Mock com os dados que seram retornados na primeira posição da lista de OfertasDisciplina que é retornada a função
@pytest.fixture
def oferta1():
    disciplina = Disciplina()
    disciplina.set_idDisciplina(2)
    disciplina.set_nomeDisc("Desenvolvimento Web")
    disciplina.set_preRequisito([])
    disciplina.set_siglaDisc("DWE")
    disciplina.set_credito(4)

    professor = Professor()
    professor.set_idProfessor(2)
    professor.set_nomeProf("Luciano")
    professor.set_prontuario("BP301863")

    sala = Sala()
    sala.set_idSala(1)
    sala.set_local("A402")

    horario = Horario()
    horario.set_idHorario(1)
    horario.set_diaSemana("segunda")
    horario.set_horaInicio("19:00:00")
    horario.set_horaFim("22:35:00")

    turma = Turma()
    turma.set_idTurma(1)
    turma.set_qtdeMaximaAluno(40)
    turma.set_horario(horario)
    turma.set_professor(professor)
    turma.set_sala(sala)   

    oferta = OfertaDisciplina()
    oferta.set_idOferta(1)
    oferta.set_disciplina(disciplina)
    oferta.set_turma(turma)
    oferta.set_codigoOferta("DWE01")
    oferta.set_semestreAno("2023-1")
    oferta = oferta.toJson()

    return oferta

#Mock com os dados que seram retornados na segunda posição da lista de OfertasDisciplina que é retornada a função
@pytest.fixture
def oferta2():
    disciplina2 = Disciplina()
    disciplina2.set_idDisciplina(6)
    disciplina2.set_nomeDisc("Engenharia de Software")
    disciplina2.set_preRequisito([])
    disciplina2.set_siglaDisc("ESW")
    disciplina2.set_credito(4)

    professor2 = Professor()
    professor2.set_idProfessor(9)
    professor2.set_nomeProf("Rosalvo")
    professor2.set_prontuario("BP301870")

    sala2 = Sala()
    sala2.set_idSala(6)
    sala2.set_local("A505")

    horario2 = Horario()
    horario2.set_idHorario(1)
    horario2.set_diaSemana("quarta")
    horario2.set_horaInicio("20:55:00")
    horario2.set_horaFim("22:35:00")

    turma2 = Turma()
    turma2.set_idTurma(6)
    turma2.set_qtdeMaximaAluno(40)
    turma2.set_horario(horario2)
    turma2.set_professor(professor2)
    turma2.set_sala(sala2)   

    oferta2 = OfertaDisciplina()
    oferta2.set_idOferta(5)
    oferta2.set_disciplina(disciplina2)
    oferta2.set_turma(turma2)
    oferta2.set_codigoOferta("ESW01")
    oferta2.set_semestreAno("2023-1")
    oferta2 = oferta2.toJson()

    return oferta2

#Mock com os dados que seram retornados na terceira posição da lista de OfertasDisciplina que é retornada a função
@pytest.fixture
def oferta3():
    disciplina3 = Disciplina()
    disciplina3.set_idDisciplina(9)
    disciplina3.set_nomeDisc("Redes de Computadores")
    disciplina3.set_preRequisito([])
    disciplina3.set_siglaDisc("RCO")
    disciplina3.set_credito(4)

    professor3 = Professor()
    professor3.set_idProfessor(9)
    professor3.set_nomeProf("Rosalvo")
    professor3.set_prontuario("BP301870")

    sala3 = Sala()
    sala3.set_idSala(5)
    sala3.set_local("A502")

    horario3 = Horario()
    horario3.set_idHorario(1)
    horario3.set_diaSemana("quarta")
    horario3.set_horaInicio("19:00:00")
    horario3.set_horaFim("20:40:00")

    turma3 = Turma()
    turma3.set_idTurma(7)
    turma3.set_qtdeMaximaAluno(40)
    turma3.set_horario(horario3)
    turma3.set_professor(professor3)
    turma3.set_sala(sala3)   

    oferta3 = OfertaDisciplina()
    oferta3.set_idOferta(6)
    oferta3.set_disciplina(disciplina3)
    oferta3.set_turma(turma3)
    oferta3.set_codigoOferta("RCO01")
    oferta3.set_semestreAno("2023-1")
    oferta3 = oferta3.toJson()

    return oferta3   


class TestControleRealizarIncricaoVerificarRequisitos:

    # Testando a quantidade de OfertasDiciplinas
    def test_verificaRequisitosQuantidadeOfertas(self, listaIdOfertas):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.verificarRequisitos(listaIdOfertas)
        # Verifica a quantidade de OfertasDiciplinas que retornaram
        assert len(respControle[0]) == 3

    # Testando a quantidade de OfertasDiciplinas com a turma cheia retornaram
    def test_verificaRequisitosQuantidadeOfertasIndisponiveis(self, listaIdOfertas):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.verificarRequisitos(listaIdOfertas)
        # Verifica a quantidade de OfertasDiciplinas indisponiveis que retornaram
        assert len(respControle[1]) == 0

    # Testando os dados da primeira OfertasDiciplina retorna
    def test_verificaRequisitosOfertasRetornada1(self, listaIdOfertas, oferta1):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.verificarRequisitos(listaIdOfertas)
        # Verifica os dados da primeira oferta disciplina que foi retornada
        assert respControle[0][0] == oferta1

    # Testando os dados da segunda OfertasDiciplina retorna
    def test_verificaRequisitosOfertasRetornada2(self, listaIdOfertas, oferta2):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.verificarRequisitos(listaIdOfertas)
        # Verifica os dados da segunda oferta disciplina que foi retornada
        assert respControle[0][1] == oferta2

    # Testando os dados da terceira OfertasDiciplina retorna
    def test_verificaRequisitosOfertasRetornada3(self, listaIdOfertas, oferta3):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.verificarRequisitos(listaIdOfertas)
        # Verifica os dados da terceira oferta disciplina que foi retornada
        assert respControle[0][2] == oferta3