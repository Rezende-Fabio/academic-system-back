from .Disciplina import Disciplina


class Aluno:
    nomeAluno: str
    protuarioAluno: str
    cursoMatruculado: str
    disciplinasConcluidas: list[Disciplina]

    def set_nomeAluno(self, nomeAluno: str) -> None:
        self.nomeAluno = nomeAluno

    def set_protuarioAluno(self, protuarioAluno: str) -> None:
        self.protuarioAluno = protuarioAluno

    def set_cursoMatruculado(self, cursoMatruculado: str) -> None:
        self.cursoMatruculado = cursoMatruculado

    def set_disciplinasConcluidas(self, disciplinasConcluidas: list[Disciplina]) -> None:
        self.disciplinasConcluidas = disciplinasConcluidas

    def get_nomeAluno(self) -> str:
        return self.nomeAluno
    
    def get_protuarioAluno(self) -> str:
        return self.protuarioAluno
    
    def get_cursoMatruculado(self) -> str:
        return self.cursoMatruculado
    
    def get_disciplinasConcluidas(self) -> list[Disciplina]:
        return self.disciplinasConcluidas