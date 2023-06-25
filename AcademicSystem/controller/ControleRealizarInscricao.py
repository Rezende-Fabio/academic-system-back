from AcademicSystem.model.entity.Inscricao import Inscricao
from AcademicSystem.model.entity.ListaEspera import ListaEspera
from ..model.entity.OfertaDisciplina import OfertaDisciplina
from ..model.entity.Aluno import Aluno
from ..model.dao.RealizarInscricaoDao import RelizarInscricaoDao


class ControleRealizarInscricao:
    def filtrarOfertas(self, aluno: Aluno) -> list[OfertaDisciplina]:
        realizarInscricaoDao = RelizarInscricaoDao()
        # Consulta as Disiplinas do curso do Aluno
        disciplinasAluno = realizarInscricaoDao.verificarDisciplinaAluno(aluno)

        # Remove as disciplinas concluidas pelo Aluno
        for indice, disciplina in enumerate(disciplinasAluno):
            for disciplinaConc in aluno.get_disciplinasConcluidas():
                if disciplina.get_siglaDisc() == disciplinaConc.get_siglaDisc():
                    del disciplinasAluno[indice]

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


    def confirmarInscricao(self, listaIdOfertas: list) -> list:
        realizarInscricaoDao = RelizarInscricaoDao()
        ofertasIndisponives = []
        listaOfertas = []
        # Consulta as ofertas que foram selecinadas
        for id in listaIdOfertas:
            oferta = realizarInscricaoDao.consultaOfertasId(id)
            listaOfertas.append(oferta)
        
        # Soma os créditos das disciplias
        somaCredito = 0
        for oferta in listaOfertas:
            somaCredito += oferta.get_disciplina().get_credito()

        # Verifica se a quantidade de crédito é maior que 20
        if somaCredito > 20:
            return []
        else:
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
