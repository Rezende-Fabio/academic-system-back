from .Disciplina import Disciplina


class Curso:
    nomeCurso: str
    siglaCurso: str
    duracaoCurso: int
    grade: list[Disciplina]
    
    def set_nomeCurso(self, nomeCurso: str) -> None:
        self.nomeCurso = nomeCurso

    def set_siglaCurso(self, siglaCurso: str) -> None:
        self.siglaCurso = siglaCurso

    def set_duracaoCurso(self, duracao: int) -> None:
        self.duracaoCurso = duracao

    def set_grade(self, grade: list[Disciplina]) -> None:
        self.grade = grade

    def get_nomeCurso(self) -> str:
        return self.nomeCurso
    
    def get_siglaCurso(self) -> str:
        return self.siglaCurso
    
    def get_duracaoCurso(self) -> int:
        return self.duracaoCurso
    
    def get_grade(self) -> list[Disciplina]:
        return self.grade