from .Conexao import Conexao

def LerDisciplinas():
    conexao = Conexao()
    conexao.conect()

    disciplinas = []

    try:
        conexao.execute("select * from disciplina;")

        rows = conexao.fetchall()

        if rows:
            for item in range(len(rows)):
                disciplinas.append(
                    {
                        "idDisc": rows[item][0],
                        "siglaDisc": rows[item][1],
                        "nomeDisc": rows[item][2],
                        "preReq1": rows[item][3],
                        "preReq2": rows[item][4],
                        "ativo": rows[item][5],
                        "idCursoDisc": rows[item][6],
                    }
                )

            conexao.disconnect()
            return disciplinas
        else:
            return {"statusCode": 201, "message": "Não há disciplinas cadastradas"}

    except:
        return False


def LerDisciplinasPorID(id):
    conexao = Conexao()
    conexao.conect()

    try:
        conexao.execute(f"select * from disciplina where idDisciplina={id};")

        disciplina = conexao.fetchall()

        if disciplina:
            for item in range(len(disciplina)):
                conexao.disconnect()
                return {
                    "idDisc": disciplina[item][0],
                    "siglaDisc": disciplina[item][1],
                    "nomeDisc": disciplina[item][2],
                    "preReq1": disciplina[item][3],
                    "preReq2": disciplina[item][4],
                    "ativo": disciplina[item][5],
                    "idCursoDisc": disciplina[item][6],
                }
        else:
            return {"statusCode": 201, "message": "Disciplina não encontrada"}
    except:
        return False


def CadastrarDisciplina(sigla, nome, preReq1, preReq2, ativo, idCurso):
    conexao = Conexao()
    conexao.conect()

    try:
        sql = "INSERT INTO disciplina (siglaDisc, nomeDisc, preReq1, preReq2, ativo, idCursoDisc) VALUES (?, ?, ?, ?, ?, ?)"
        parametros = (
            sigla,
            nome,
            bool(preReq1),
            bool(preReq2),
            int(ativo),
            int(idCurso),
        )

        if conexao.execute(sql, parametros):
            conexao.commit()
            conexao.disconnect()

            return True
    except:
        return False


def AtualizarDisciplina(sigla, nome, preReq1, preReq2, ativo, idCurso):
    conexao = Conexao()
    conexao.conect()

    try:
        sql = "UPDATE disciplina SET siglaDisc = ? WHERE idDisciplina = ?"
        parametros = (
            sigla,
            nome,
            bool(preReq1),
            bool(preReq2),
            int(ativo),
            int(idCurso),
        )

        if conexao.execute(sql, parametros):
            conexao.commit()
            conexao.disconnect()

            return True
    except:
        return False


def DeletarDiscipina(id):
    conexao = Conexao()
    conexao.conect()

    try:
        sql = "DELETE FROM disciplina WHERE idDisciplina=?;"
        parametros = (id)

        if conexao.execute(sql, parametros):
            conexao.commit()
            conexao.disconnect()

            return True
        
    except:
        return False