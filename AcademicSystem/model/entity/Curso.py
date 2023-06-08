from .Disciplina import Disciplina

class Curso:
    nomeCurso: str
    siglaCurso: str
    duracaoCurso: int
    grade: list[Disciplina]
    