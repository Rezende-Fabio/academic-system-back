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

    insc = Inscricao()
    insc.set_aluno(aluno)
    insc.set_dataInscricao(date.today())
    insc.set_ofertaDisciplina(oferta)

    yield insc


class TestControleRealizarIncricaoFiltrarOferta:
    # Testando a quantidade de OfertasDiciplinas
    def test_filtrarOfertasQuantidadeOfertas(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        # Verifica a quantidade de OfertasDiciplinas que retornaram
        assert len(respControle) == 1

    # Testando semestreAno atributo de OfertasDiciplinas
    def test_filtrarOfertasAtributosSemestreAno(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            assert oferta.get_semestreAno() == "2023-1"

    # Testando codigoOferta atributo de OfertasDiciplinas
    def test_filtrarOfertasAtributosCodigo(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            assert oferta.get_codigoOferta() == "DWE01"

    # Testando os atributo crédito da instancia da Disciplina na OfertasDiciplina
    def test_filtrarOfertasAtributoDisciplinaCredito(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o credio Disciplina que está sendo ofertada
            assert oferta.get_disciplina().get_credito() == 4

    # Testando os atributo nome da instancia da Disciplina na OfertasDiciplina
    def test_filtrarOfertasAtributoDisciplinaNome(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o nome Disciplina que está sendo ofertada
            assert oferta.get_disciplina().get_nomeDisc() == "Desenvolvimento Web"

    # Testando os atributo pré-requisito da instancia da Disciplina na OfertasDiciplina
    def test_filtrarOfertasAtributoDisciplina(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o preRequisito Disciplina que está sendo ofertada
            assert oferta.get_disciplina().get_preRequisito() == 0

    # Testando os atributo pré-requisito da instancia da Disciplina na OfertasDiciplina
    def test_filtrarOfertasAtributoDisciplinaSigla(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica a siglaDisc Disciplina que está sendo ofertada
            assert oferta.get_disciplina().get_siglaDisc() == "DWE"

    # Testando os atributo quantide máxima de aluno da instancia da Turma na OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaQtdeMaxAluno(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica a qtdeMaximaAluno da turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_qtdeMaximaAluno() == 40

    # Testando os atributo local da instancia da Sala na Turma da OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaSalaLocal(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o local da Sala da Turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_sala().get_local() == "A402"

    # Testando os atributo Dia da semana da instancia do Horario na Turma da OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaHorarioDia(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o diaSemana do Horario da Turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_horario().get_diaSemana() == "segunda"

    # Testando os atributo Hoario de início da instancia do Horario na Turma da OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaHorarioHinicio(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o horaInicio do Horario da Turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_horario().get_horaInicio() == "19:00:00"

    # Testando os atributo Hoario de fim da instancia do Horario na Turma da OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaHorarioHfim(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o horaFim do Horario da Turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_horario().get_horaFim() == "22:35:00"

    # Testando os atributo Nome da instancia do Professor na Turma da OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaProfessorNome(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o nome do Professor da Turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_professor().get_nomeProf() == "Luciano"
            assert oferta.get_turma().get_professor().get_prontuario() == "BP301863"

    # Testando os atributo Prontuario da instancia do Professor na Turma da OfertasDiciplina
    def test_filtrarOfertasAtributoTurmaProfessorProntuario(self, aluno):
        controleRelizarInscricao = ControleRealizarInscricao()
        respControle = controleRelizarInscricao.filtrarOfertas(aluno)
        for oferta in respControle:
            # Verifica o prontuario do Professor da Turma que está instâncida na OfertaDisciplina
            assert oferta.get_turma().get_professor().get_prontuario() == "BP301863"


class TestControleRealizarIncricaoAdicionarListaEspera:
    def test_adicionarListaEspera(self, insc):
        controleRealizarInscricao = ControleRealizarInscricao()
        respControle = controleRealizarInscricao.adicionarListaEspera(insc)

        assert respControle

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