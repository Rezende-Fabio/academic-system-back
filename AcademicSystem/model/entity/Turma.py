from .Professor import Professor
from .Horario import Horario
from .Sala import Sala


class Turma:
    qtdeMaximaAluno: int
    professor: Professor
    sala: Sala
    horario: Horario

    def set_qtdeMaximaAluno(self, qtdeMax: int) -> None:
        self.qtdeMaximaAluno = qtdeMax

    def set_professor(self, professor: Professor) -> None:
        self.professor = professor

    def set_sala(self, sala: Sala) -> None:
        self.sala = sala

    def set_horario(self, horario: Horario) -> None:
        self.horario = horario

    def get_qtdeMaximaAluno(self) -> int:
        return self.qtdeMaximaAluno

    def get_professor(self) -> Professor:
        return self.professor

    def get_sala(self) -> Sala:
        return self.sala

    def get_horario(self) -> Horario:
        return self.horario    

    def verficaTurmaLotada(self) -> bool:
        pass

    def verificaQtdeAlunoMatriculado(self) -> bool:
        pass
