from .Aluno import Aluno
from .Inscricao import Inscricao


class Turma:
    qtdeMaximaAluno: int
    listaMatriculados: list[Aluno]
    inscricao: Inscricao

    def set_qtdeMaximaAluno(self, qtdeMax: int) -> None:
        self.qtdeMaximaAluno = qtdeMax

    def set_listaMatriculados(self, listaMatriculados: list[Aluno]) -> None:
        self.listaMatriculados = listaMatriculados

    def set_inscricao(self, inscricao: Inscricao) -> None:
        self.inscricao = inscricao

    def get_qtdeMaximaAluno(self) -> int:
        return self.qtdeMaximaAluno
    
    def get_listaMatriculados(self) -> list[Aluno]:
        return self.listaMatriculados
    
    def get_inscricao(self) -> Inscricao:
        return self.inscricao

    def verficaTurmaLotada(self) -> bool:
        pass

    def verificaQtdeAlunoMatriculado(self) -> bool:
        pass
