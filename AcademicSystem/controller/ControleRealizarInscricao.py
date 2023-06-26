from AcademicSystem.model.entity.Inscricao import Inscricao
from AcademicSystem.model.entity.ListaEspera import ListaEspera
from ..model.entity.OfertaDisciplina import OfertaDisciplina
from ..model.entity.Aluno import Aluno
from ..model.dao.RealizarInscricaoDao import RelizarInscricaoDao


class ControleRealizarInscricao:

    def filtrarOfertas(self, aluno: Aluno) -> list[OfertaDisciplina]:
        realizarInscricaoDao = RelizarInscricaoDao()

        # Monta uma lista com todas as disciplinas que o aluno já concluiu
        where = "("
        for disciplinaConc in aluno.get_disciplinasConcluidas():
            where += f'"{disciplinaConc.get_siglaDisc()}", '
        where += ")"
        where = where.replace(", )", ")")

        # Consulta as Disiplinas que o aluno pode se inscrever
        disciplinasAluno = realizarInscricaoDao.verificarDisciplinaAluno(aluno, where)

        # Remove as disciplinas que tem pré-requisitos que não foram concluidos
        for indice, disciplina in enumerate(disciplinasAluno):
            if len(disciplina.get_preRequisito()) > 0:
                for preRec in disciplina.get_preRequisito():
                    for disciplinaConc in aluno.get_disciplinasConcluidas():
                        if preRec.get_siglaDisc() != disciplinaConc.get_siglaDisc():
                            del disciplinasAluno[indice]

        # Monta lista com as ofertas das Disciplinas
        listaOfertas = []
        for indice, disciplina in enumerate(disciplinasAluno):
            ofertaDisciplina = realizarInscricaoDao.consultaOfertasDisciplina(disciplina)
            if ofertaDisciplina != None:
                listaOfertas.append(ofertaDisciplina)

        return listaOfertas


    def verificarRequisitos(self, listaIdOfertas: list) -> list:
        realizarInscricaoDao = RelizarInscricaoDao()
        ofertasIndisponives = []
        listaOfertas = []
        # Consulta as ofertas que foram selecinadas
        for id in listaIdOfertas:
            oferta = realizarInscricaoDao.consultaOfertasId(id)
            listaOfertas.append(oferta)
        
        #  Verifica a quantidade de alunos nas turmas
        for oferta in listaOfertas:
            qtdAlunosTurma = realizarInscricaoDao.consultaQtdeAlunosTurma(oferta.get_turma().get_idTurma())
            if qtdAlunosTurma >= oferta.get_turma().get_qtdeMaximaAluno():
                ofertasIndisponives.append(oferta)
        
        # Soma os créditos das disciplias
        somaCredito = 0
        for oferta in listaOfertas:
            somaCredito += oferta.get_disciplina().get_credito()

        # Verifica se a quantidade de crédito é maior que 20
        if somaCredito > 20:
            return ([])
        else:
            diaSemana = ''
            horaInicio = None
            horaFim = None
            # Veririfica choque de horario
            for oferta in listaOfertas:
                if oferta.get_turma().get_horario().get_diaSemana() == diaSemana:
                    if oferta.get_turma().get_horario().get_horaInicio() == horaInicio and oferta.get_turma().get_horario().get_horaFim() == horaFim:
                        return ([])
                
                diaSemana = oferta.get_turma().get_horario().get_diaSemana()
                horaInicio = oferta.get_turma().get_horario().get_horaInicio()
                horaFim = oferta.get_turma().get_horario().get_horaFim()

        return [listaIdOfertas, ofertasIndisponives]


    def confirmarInscricao(self) -> bool:
        pass


    def adicionarListaEspera(self, insc: Inscricao) -> list:
        IDTURMA = insc.get_ofertaDisciplina().get_turma().get_idTurma()

        realizarInscricaoDao = RelizarInscricaoDao()
        qtdMaximaAlunos = realizarInscricaoDao.consultaTurma(IDTURMA).get_qtdeMaximaAluno()
        qtdAlunosTurma = realizarInscricaoDao.consultaQtdeAlunosTurma(IDTURMA)

        if qtdAlunosTurma == qtdMaximaAlunos:
            lista = ListaEspera()

            lista.set_listaEspera(insc)
            lista.set_ativoLista(True)

            return lista
