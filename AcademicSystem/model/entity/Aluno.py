from .Disciplina import Disciplina
from datetime import date
from .Curso import Curso


class Aluno:
    idAluno: int
    nomeAluno: str
    protuarioAluno: str
    dataNasc: date
    cpf: str
    cursoMatruculado: Curso
    disciplinasConcluidas: list[Disciplina]
    ativoAluno: bool

    def set_idAluno(self, id: int) -> None:
        self.idAluno = id

    def set_nomeAluno(self, nomeAluno: str) -> None:
        self.nomeAluno = nomeAluno

    def set_protuarioAluno(self, protuarioAluno: str) -> None:
        self.protuarioAluno = protuarioAluno

    def set_dataNasc(self, dataNasc: date) -> None:
        self.dataNasc = dataNasc

    def set_cpf(self, cpf: str) -> None:
        self.cpf = cpf

    def set_cursoMatruculado(self, cursoMatruculado: Curso) -> None:
        self.cursoMatruculado = cursoMatruculado

    def set_disciplinasConcluidas(self, disciplinasConcluidas: list[Disciplina]) -> None:
        self.disciplinasConcluidas = disciplinasConcluidas

    def set_ativoAluno(self, ativoAluno: bool) -> None:
        self.ativoAluno = ativoAluno

    def get_idAluno(self) -> int:
        return self.idAluno

    def get_nomeAluno(self) -> str:
        return self.nomeAluno
    
    def get_protuarioAluno(self) -> str:
        return self.protuarioAluno
    
    def get_dataNasc(self) -> date:
        return self.dataNasc

    def get_cpf(self) -> str:
        return self.cpf
    
    def get_cursoMatruculado(self) -> Curso:
        return self.cursoMatruculado
    
    def get_disciplinasConcluidas(self) -> list[Disciplina]:
        return self.disciplinasConcluidas
    
    def get_ativoAluno(self) -> bool:
        return self.ativoAluno
    
    def toAluno(self, json: dict) -> None:
        self.idAluno = json["idAluno"]
        self.nomeAluno = json["nomeAluno"]
        self.cpf = json["cpf"]
        self.protuarioAluno = json["protuarioAluno"]
        self.dataNasc = json["dataNasc"]
