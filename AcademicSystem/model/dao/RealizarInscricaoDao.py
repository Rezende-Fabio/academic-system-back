from ..entity.Aluno import Aluno
from ..entity.Disciplina import Disciplina
from ..entity.OfertaDisciplina import OfertaDisciplina
from ..entity.Turma import Turma
from ..entity.Horario import Horario
from ..entity.Professor import Professor
from ..entity.Sala import Sala
from ..entity.Inscricao import Inscricao
from ..entity.ListaEspera import ListaEspera
from .Conexao import Conexao
from datetime import datetime
import sys

class RelizarInscricaoDao:

    def inserirInscricao(self, inscricao: Inscricao) -> bool:
        try:
            conexao = Conexao()
            conexao.conect()
            parametros = (
                inscricao.get_dataInscricao(),
                1,
                inscricao.get_aluno().get_idAluno(),
                inscricao.get_ofertaDisciplina().get_idOferta(),
            )
            conexao.execute(f"INSERT INTO inscricao (dataInscricao, ativoInscricao, idAlunoInsc, idOfertaInsc) VALUES (?, ?, ?, ?)", parametros)
            conexao.commit()
            return True
        except Exception as erro:
            print(sys.exc_info()[0], erro)
            return False


    def verificarDisciplinaAluno(self, aluno: Aluno, disciplinaConc: str) -> list[Disciplina]:
        conexao = Conexao()
        conexao.conect()
        cursoAluno = aluno.get_cursoMatruculado().get_idCurso()
        conexao.execute(f"SELECT * FROM disciplina disc WHERE disc.idCursoDisc = {cursoAluno} AND disc.siglaDisc NOT IN {disciplinaConc}")
        respDao = conexao.fetchall()
        listaDisciplina = []
        #Adiciona Disciplinas em uma lista
        for disc in respDao:
            disciplina = Disciplina()
            disciplina.set_idDisciplina(disc[0])
            disciplina.set_nomeDisc(disc[2])
            disciplina.set_siglaDisc(disc[1])
            disciplina.set_credito(disc[5])
            listaPreRec = []
            #Consulta os pré-requisitos da Disciplina
            for x in [3, 4]:
                preRec = self.consultaPreRequisito(disc[x])
                if preRec != None:
                    listaPreRec.append(preRec)

            disciplina.set_preRequisito(listaPreRec)
            listaDisciplina.append(disciplina)

        conexao.disconnect()
        return listaDisciplina


    def consultaPreRequisito(self, idPreRec: int) -> Disciplina:
        if idPreRec != None and idPreRec != 0:
            conexao = Conexao()
            conexao.conect()
            conexao.execute(f"SELECT * FROM disciplina disc WHERE disc.idDisciplina = {idPreRec}")
            respDao = conexao.fetchall()
            for disc in respDao:
                disciplina = Disciplina()
                disciplina.set_idDisciplina(disc[0])
                disciplina.set_nomeDisc(disc[2])
                disciplina.set_siglaDisc(disc[1])
                disciplina.set_credito(disc[5])

            conexao.disconnect()
            return disciplina
        else:
            return None
        

    def consultaOfertasDisciplina(self, disciplina: Disciplina) -> OfertaDisciplina:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM ofertaDisciplina ofert WHERE ofert.idDisciplinaOfert = {disciplina.get_idDisciplina()}")
        respDao = conexao.fetchall()
        if respDao:
            for oferta in respDao:
                ofertaDisciplina = OfertaDisciplina()
                ofertaDisciplina.set_idOferta(oferta[0])
                ofertaDisciplina.set_disciplina(disciplina)
                ofertaDisciplina.set_codigoOferta(oferta[2])
                ofertaDisciplina.set_semestreAno(oferta[1])
                ofertaDisciplina.set_turma(self.consultaTurma(oferta[4]))
            conexao.disconnect()
            return ofertaDisciplina
        
        else:
            return None
        

    def consultaOfertasId(self, id: int) -> OfertaDisciplina:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM ofertaDisciplina ofert WHERE ofert.idOfertaDisciplina = {id}")
        respDao = conexao.fetchall()
        for oferta in respDao:
            ofertaDisciplina = OfertaDisciplina()
            ofertaDisciplina.set_idOferta(oferta[0])
            ofertaDisciplina.set_disciplina(self.consultaDisciplina(oferta[5]))
            ofertaDisciplina.set_codigoOferta(oferta[2])
            ofertaDisciplina.set_semestreAno(oferta[1])
            ofertaDisciplina.set_turma(self.consultaTurma(oferta[4]))

        conexao.disconnect()
        return ofertaDisciplina
        
        
    def consultaDisciplina(self, idDisciplina: int) -> Disciplina:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM disciplina disc WHERE disc.idDisciplina = {idDisciplina}")
        respDao = conexao.fetchall()
        for disciplina in respDao:
            disciplinaOferta = Disciplina()
            disciplinaOferta.set_idDisciplina(disciplina[0])
            disciplinaOferta.set_siglaDisc(disciplina[1])
            disciplinaOferta.set_nomeDisc(disciplina[2])
            disciplinaOferta.set_credito(disciplina[5])
            listaPreRec = []
            #Consulta os pré-requisitos da Disciplina
            for x in [3, 4]:
                preRec = self.consultaPreRequisito(disciplina[x])
                if preRec != None:
                    listaPreRec.append(preRec)

            disciplinaOferta.set_preRequisito(listaPreRec)
        
        conexao.disconnect()
        return disciplinaOferta


    def consultaTurma(self, idTurma: int) -> Turma:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM turma turm WHERE turm.idTurma = {idTurma}")
        respDao = conexao.fetchall()
        for turma in respDao:
            turmaOferta = Turma()
            turmaOferta.set_idTurma(turma[0])
            turmaOferta.set_qtdeMaximaAluno(turma[1])
            turmaOferta.set_professor(self.consultaProfessor(turma[6]))
            turmaOferta.set_sala(self.consultaSala(turma[4]))
            turmaOferta.set_horario(self.consultaHorario(turma[5]))
        
        conexao.disconnect()
        return turmaOferta

    
    def consultaProfessor(self, idProfessor: int) -> Professor:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM professor prof WHERE prof.idProfessor = {idProfessor}")
        respDao = conexao.fetchall()
        for professor in respDao:
            professorTurma = Professor()
            professorTurma.set_idProfessor(professor[0])
            professorTurma.set_nomeProf(professor[1])
            professorTurma.set_prontuario(professor[2])
            professorTurma.set_ativoProfessor(professor[3])
        
        conexao.disconnect()
        return professorTurma
    

    def consultaSala(self, idSala: int) -> Sala:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM sala sala WHERE sala.idSala = {idSala}")
        respDao = conexao.fetchall()
        for sala in respDao:
            salaTurma = Sala()
            salaTurma.set_idSala(sala[0])
            salaTurma.set_local(sala[1])
            salaTurma.set_ativoSala(sala[2])

        conexao.disconnect()
        return salaTurma
    

    def consultaHorario(self, idHorario: int) -> Horario:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM horario hora WHERE hora.idHorario = {idHorario}")
        respDao = conexao.fetchall()
        for horario in respDao:
            horarioTurma = Horario()
            horarioTurma.set_idHorario(horario[0])
            horarioTurma.set_diaSemana(horario[1])
            horarioTurma.set_horaInicio(horario[2])
            horarioTurma.set_horaFim(horario[3])
            horarioTurma.set_ativoHorario(horario[4])

        conexao.disconnect()
        return horarioTurma
    

    def consultaListaEspera(self, idDiciplina: int) -> ListaEspera:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT * FROM listaDeEspera list WHERE list.idDiscList = {idDiciplina}")
        respDao = conexao.fetchall()
        for inscricao in respDao:
            listaDeEspera = ListaEspera()
            listaDeEspera.set_idLista(inscricao[0])
            listaDeEspera.set_ativoLista(inscricao[1])
            listaDeEspera.set_dataEntrada(inscricao[2])
            listaDeEspera.set_disciplina(self.consultaDisciplina(inscricao[4]))

        return listaDeEspera


    def consultaQtdeAlunosTurma(self, idOferta: int) -> int:
        conexao = Conexao()
        conexao.conect()
        conexao.execute(f"SELECT COUNT(*) FROM inscricao i INNER JOIN ofertaDisciplina o ON i.idOfertaInsc = o.idOfertaDisciplina WHERE o.idOfertaDisciplina = {idOferta};")

        respDao = conexao.fetchall()
        conexao.disconnect()

        if respDao:
            return respDao[0][0]
        else:
            return 0
        

    def inserirListaEspera(self, listaEspera: ListaEspera) -> bool:
        try:
            conexao = Conexao()
            conexao.conect()
            parametros = (
                1,
                datetime.now(),
                listaEspera.get_aluno().get_idAluno(),
                listaEspera.get_disciplina().get_idDisciplina()
            )
            conexao.execute(f"INSERT INTO listaDeEspera (ativoLista, entradaList, idAlunoList, idDiscList) VALUES (?, ?, ?, ?)", parametros)
            conexao.commit()
            return True
        except Exception as erro:
            print(sys.exc_info()[0], erro)
            return False
        

    def verificarAlunoLista(self, listaEspera: ListaEspera) -> int:
        try:
            conexao = Conexao()
            conexao.conect()
            conexao.execute(f"SELECT COUNT(*) FROM listaDeEspera list WHERE list.idAlunoList = {listaEspera.get_aluno().get_idAluno()} AND list.idDiscList = {listaEspera.get_disciplina().get_idDisciplina()}")
            respDao = conexao.fetchall()
            if respDao[0][0] > 0:
                return 1
            else:
                return 2
            
        except Exception as erro:
            print(sys.exc_info()[0], erro)
            return 3

