from .Disciplina import Disciplina

class Aluno:
    nomeAluno: str
    protuarioAluno: str
    cursoMatruculado: str
    disciplinasConcluidas: list[Disciplina]