from AcademicSystem.model.dao.Conexao import Conexao

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
            return {"message": "Não há disciplinas cadastradas"}

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
            return {"message": "Disciplina não encontrada"}
    except:
        return False