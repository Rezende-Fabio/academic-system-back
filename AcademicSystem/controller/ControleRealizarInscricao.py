from ..model.entity.OfertaDisciplina import OfertaDisciplina
from ..model.entity.Aluno import Aluno
from ..model.dao.RealizarInscricaoDao import RelizarInscricaoDao

class ControleRealizarInscricao:

    def filtrarOfertas(self, aluno: Aluno) -> list[OfertaDisciplina]:
        realizarInscricaoDao = RelizarInscricaoDao()
        #Consulta as Disiplinas do curso do Aluno
        disciplinasAluno = realizarInscricaoDao.verificarDisciplinaAluno(aluno)

        #Remove as disciplinas concluidas pelo Aluno
        for indice, disciplina in enumerate(disciplinasAluno):
            for disciplinaConc in aluno.get_disciplinasConcluidas():
                if disciplina.get_siglaDisc() == disciplinaConc.get_siglaDisc():
                    del disciplinasAluno[indice]

        print(disciplinasAluno)

        #Remove as disciplinas que tem pré-requisitos que não foram concluidos
        for indice, disciplina in enumerate(disciplinasAluno):
            if len(disciplina.get_preRequisito()) > 0:
                for preRec in disciplina.get_preRequisito():
                    for disciplinaConc in aluno.get_disciplinasConcluidas():
                        if preRec.get_siglaDisc() != disciplinaConc.get_siglaDisc():
                            del disciplinasAluno[indice]

        print(disciplinasAluno)     

        #Monta lista com as ofertas das Disciplinas
        listaOfertas = []
        for indice, disciplina in enumerate(disciplinasAluno):
            ofertaDisciplina = realizarInscricaoDao.consultaOfertas(disciplina)
            if ofertaDisciplina != None:
                listaOfertas.append(ofertaDisciplina)

        return listaOfertas


    def confirmarInscricao(self) -> None:
        pass

    def adicionarListaEspera(self) -> None:
        pass
