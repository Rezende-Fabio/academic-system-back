from AcademicSystem.model.dao.Conexao import Conexao

#Função para criar as tabelas
def criaTabelas():

    conexao = Conexao()
    conexao.conect()
    try:
        #Tabela Usuaários
        conexao.execute("""CREATE TABLE IF NOT EXISTS usuario (
                            idUsuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            prontuario TEXT(10) NOT NULL,
                            senha TEXT(32) NOT NULL,
                            permissao INTEGER NOT NULL,
                            ativoUsuario BOOLEAN NOT NULL
                            );
                        """)
        
        #Tabelas Aluno
        conexao.execute("""CREATE TABLE IF NOT EXISTS aluno (
                            idAluno INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            nomeAluno TEXT(45) NOT NULL,
                            cursoMatriculado TEXT(45) NOT NULL,
                            cpf TEXT(11) NOT NULL,
                            dataNasc DATE NOT NULL,
                            ativoAluno BOOLEAN NOT NULL,
                            idUsuarioAlu INTEGER NOT NULL,
                            FOREIGN KEY (idUsuarioAlu) REFERENCES usuario (idUsuario)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            );
                        """)
        
        #Tabela Coordenador
        conexao.execute("""CREATE TABLE IF NOT EXISTS coordenador (
                            idCoordenador INTEGER NOT NULL PRIMARY KEY,
                            idUsuarioCoo INTEGER NOT NULL,
                            nome TEXT(45) NOT NULL,
                            ativoCoordenador BOOLEAN NOT NULL,
                            FOREIGN KEY (idUsuarioCoo) REFERENCES usuario (idUsuario)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            );
                        """)
        
        #Tabela Curso
        conexao.execute("""CREATE TABLE IF NOT EXISTS curso (
                            idCurso INTEGER NOT NULL PRIMARY KEY,
                            nome TEXT(45) NULL,
                            siglaCurso TEXT(45) NULL,
                            duracao INT NULL,
                            ativoCurso BOOLEAN NOT NULL
                            );
                        """)
        
        #Tabela Discipina
        conexao.execute("""CREATE TABLE IF NOT EXISTS disciplina (
                            idDisciplina INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            siglaDisc TEXT(5) NOT NULL,
                            nomeDisc TEXT(45) NOT NULL,
                            preReq1 INT NULL,
                            preReq2 INT NULL,
                            cretido INT NOT NULL,
                            ativoDisciplina BOOLEAN NOT NULL,
                            idCursoDisc INTEGER NOT NULL,
                            FOREIGN KEY (idCursoDisc) REFERENCES curso (idCurso)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            );
                        """)
        
        #Tabela Sala
        conexao.execute("""CREATE TABLE IF NOT EXISTS sala (
                        idSala INTEGER NOT NULL PRIMARY KEY,
                        local TEXT(45) NULL,
                        ativoSala BOOLEAN NOT NULL
                        );
                        """)

        #Tabela Horario
        conexao.execute("""CREATE TABLE IF NOT EXISTS horario (
                            idHorario INTEGER NOT NULL PRIMARY KEY,
                            diaSemana TEXT(14) NULL,
                            horaInicio TIME NULL,
                            horaFim TIME NULL,
                            ativoHorario BOOLEAN NOT NULL
                            );
                        """)
        
        #Tabela Professor
        conexao.execute("""CREATE TABLE IF NOT EXISTS professor (
                            idProfessor INTEGER NOT NULL PRIMARY KEY,
                            nome TEXT(45) NULL,
                            prontuario TEXT(10) NULL,
                            ativoProfessor BOOLEAN NOT NULL
                            );
                        """)
        
        #Tabelas Turma
        conexao.execute("""CREATE TABLE IF NOT EXISTS turma (
                            idTurma INTEGER NOT NULL PRIMARY KEY,
                            qtdeMaxAluno INT NULL,
                            turmacod TEXT(45) NULL,
                            ativoTurma BOOLEAN NOT NULL,
                            idSalaTur INTEGER NOT NULL,
                            idHoraTur INTEGER NOT NULL,
                            idProfTur INTEGER NOT NULL,
                            FOREIGN KEY (idSalaTur) REFERENCES sala
                            (idSala)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (idHoraTur) REFERENCES horario (idHorario)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (idProfTur) REFERENCES professor (idProfessor)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            );
                        """)
        
        #Tabela Oferta Disciplina
        conexao.execute("""CREATE TABLE IF NOT EXISTS ofertaDisciplina (
                            idOfertaDisciplina INTEGER NOT NULL PRIMARY KEY,
                            semestreAno TEXT(10) NULL,
                            codigoOferta TEXT(7) NULL,
                            ativoOferta BOOLEAN NOT NULL,
                            idTurmaOfert INTEGER NOT NULL,
                            idDisciplinaOfert INTEGER NOT NULL,
                            FOREIGN KEY (idTurmaOfert) REFERENCES turma (idTurma)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (idDisciplinaOfert) REFERENCES disciplina (idDisciplina)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            );
                            """)
        
        #Tabela Lista Espera
        conexao.execute("""CREATE TABLE IF NOT EXISTS listaDeEspera (
                            idlistaDeEspera INTEGER NOT NULL PRIMARY KEY,
                            ativoLista BOOLEAN NOT NULL
                            );
                        """)
        
        #Tabela Inscrição
        conexao.execute("""CREATE TABLE IF NOT EXISTS inscricao (
                            idInscricao INTEGER NOT NULL PRIMARY KEY,
                            dataIncricao DATE NULL,
                            ativoInscricao BOOLEAN NOT NULL,
                            idAlunoInsc INTEGER NOT NULL,
                            idTurmaInsc INTEGER NOT NULL,
                            idListaInsc INTEGER NOT NULL,
                            FOREIGN KEY (idAlunoInsc) REFERENCES aluno
                            (idAluno)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (idTurmaInsc) REFERENCES turma (idTurma)
                            ON DELETE CASCADE ON UPDATE CASCADE,
                            FOREIGN KEY (idListaInsc) REFERENCES listaDeEspera (idlistaDeEspera)
                            ON DELETE CASCADE ON UPDATE CASCADE
                            );
                        """)
        return True
    except:
        return False