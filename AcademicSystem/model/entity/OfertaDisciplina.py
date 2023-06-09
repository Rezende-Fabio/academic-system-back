from .Disciplina import Disciplina
from .Turma import Turma


class OfertaDisciplina:
    semestreAno: str
    codigoOferta: str
    disciplina: Disciplina
    turma: Turma

    def set_semestreAno(self, semestreAno: str) -> None:
        self.semestreAno = semestreAno

    def set_codigoOferta(self, codigoOferta: str) -> None:
        self.codigoOferta = codigoOferta

    def set_disciplina(self, disciplina: Disciplina) -> None:
        self.disciplina = disciplina

    def set_turma(self, turma: Turma) -> None:
        self.turma = turma

    def get_semestreAno(self) -> str:
        return self.semestreAno
    
    def get_codigoOferta(self) -> str:
        return self.codigoOferta
    
    def get_disciplina(self) -> Disciplina:
        return self.disciplina
    
    def get_turma(self) -> Turma:
        return self.turma