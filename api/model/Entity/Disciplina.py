import Disciplina
from .Curso import Curso

class Disciplina:
    siglaDisc: str
    nomeDisc: str
    preRequisito: list[Disciplina]
    credito: int
    curso: Curso