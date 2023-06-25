from .Disciplina import Disciplina


class Curso:
    idCurso: int
    nomeCurso: str
    siglaCurso: str
    duracaoCurso: int
    grade: list[Disciplina]
    ativoCurso: bool

    def set_idCurso(self, idCurso: int) -> None:
        self.idCurso = idCurso
    
    def set_nomeCurso(self, nomeCurso: str) -> None:
        self.nomeCurso = nomeCurso

    def set_siglaCurso(self, siglaCurso: str) -> None:
        self.siglaCurso = siglaCurso

    def set_duracaoCurso(self, duracao: int) -> None:
        self.duracaoCurso = duracao

    def set_grade(self, grade: list[Disciplina]) -> None:
        self.grade = grade

    def set_ativoCurso(self, ativoCurso: bool) -> None:
        self.ativoCurso = ativoCurso

    def get_idCurso(self) -> int:
        return self.idCurso

    def get_nomeCurso(self) -> str:
        return self.nomeCurso
    
    def get_siglaCurso(self) -> str:
        return self.siglaCurso
    
    def get_duracaoCurso(self) -> int:
        return self.duracaoCurso
    
    def get_grade(self) -> list[Disciplina]:
        return self.grade
    
    def get_ativoCurso(self) -> bool:
        return self.ativoCurso