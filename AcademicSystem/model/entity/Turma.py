from .Professor import Professor
from .Horario import Horario
from .Sala import Sala


class Turma:
    idTurma: int
    qtdeMaximaAluno: int
    professor: Professor
    sala: Sala
    horario: Horario

    def set_idTurma(self, id: int) -> None:
        self.idTurma = id

    def set_qtdeMaximaAluno(self, qtdeMax: int) -> None:
        self.qtdeMaximaAluno = qtdeMax

    def set_professor(self, professor: Professor) -> None:
        self.professor = professor

    def set_sala(self, sala: Sala) -> None:
        self.sala = sala

    def set_horario(self, horario: Horario) -> None:
        self.horario = horario

    def get_idTurma(self) -> int:
        return self.idTurma

    def get_qtdeMaximaAluno(self) -> int:
        return self.qtdeMaximaAluno

    def get_professor(self) -> Professor:
        return self.professor

    def get_sala(self) -> Sala:
        return self.sala

    def get_horario(self) -> Horario:
        return self.horario    

    def toJson(self) -> dict:
        json = {
            "qtdeMaximaAluno": self.qtdeMaximaAluno,
            "idTurma": self.idTurma,
            "professor": self.professor.toJson(),
            "sala": self.sala.toJson(),
            "horario": self.horario.toJson(),
        }

        return json
