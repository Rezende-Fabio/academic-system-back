from AcademicSystem.model.entity.Inscricao import Inscricao
from AcademicSystem.model.entity.ListaEspera import ListaEspera
from ..model.entity.OfertaDisciplina import OfertaDisciplina
from ..model.entity.Aluno import Aluno
from ..model.dao.RealizarInscricaoDao import RelizarInscricaoDao
from datetime import datetime


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

        _break = False
        # Remove as disciplinas que tem pré-requisitos que não foram concluidos
        for indice, disciplina in enumerate(disciplinasAluno):
            if len(disciplina.get_preRequisito()) > 0:
                for preRec in disciplina.get_preRequisito():
                    for disciplinaConc in aluno.get_disciplinasConcluidas():
                        if preRec.get_siglaDisc() != disciplinaConc.get_siglaDisc():
                            del disciplinasAluno[indice]
                            _break = True
                            break
                        
                    if _break:
                        break

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
            return [1]
        else:
            # Veririfica choque de horario
            for oferta in listaOfertas:
                for oferta2 in listaOfertas:
                    if oferta.get_turma().get_idTurma() != oferta2.get_turma().get_idTurma(): #Verifica se é a mesma turma
                        if oferta.get_turma().get_horario().get_diaSemana() == oferta2.get_turma().get_horario().get_diaSemana(): #Verifica se é o mesmo dia na semana
                            if oferta.get_turma().get_horario().get_horaInicio() == oferta2.get_turma().get_horario().get_horaInicio(): #Verifica se a hora início é igual
                                if oferta.get_turma().get_horario().get_horaFim() == oferta2.get_turma().get_horario().get_horaFim(): #Verifica se a hora fim é igual
                                    return [2]
                            elif oferta.get_turma().get_horario().get_horaFim() == oferta2.get_turma().get_horario().get_horaFim():
                                return [2]
        
        return [[ofertaDisp.toJson() for ofertaDisp in listaOfertas], [ofertaInd.toJson() for ofertaInd in ofertasIndisponives]]


    def confirmarInscricao(self, listaIdsOfertas: list, aluno: Aluno) -> bool:
        realizarInscricaoDao = RelizarInscricaoDao()
        listaOfertas = []
        # Consulta as ofertas que foram selecinadas
        for id in listaIdsOfertas:
            oferta = realizarInscricaoDao.consultaOfertasId(id)
            listaOfertas.append(oferta)

        # Monta as inscrições
        listaInscricao = []
        for oferta in listaOfertas:
            inscricao = Inscricao()
            inscricao.set_ofertaDisciplina(oferta)
            inscricao.set_aluno(aluno)
            inscricao.set_dataInscricao(datetime.now())
            listaInscricao.append(inscricao)

        for inscricao in listaInscricao:
            realizarInscricaoDao.inserirInscricao(inscricao)

        return True


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
