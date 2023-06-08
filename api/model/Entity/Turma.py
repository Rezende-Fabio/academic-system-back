from .Aluno import Aluno
from .Inscricao import Incricao


class Turma:
    qtdeMaximaAluno: int
    listaMatriculados: list[Aluno]
    incricao: Incricao