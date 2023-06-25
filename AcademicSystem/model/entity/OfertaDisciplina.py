from .Disciplina import Disciplina
from .Turma import Turma


class OfertaDisciplina:
    idOferta: int
    semestreAno: str
    codigoOferta: str
    disciplina: Disciplina
    turma: Turma
    ativoOferta: bool

    def set_idOferta(self, id: int) -> None:
        self.idOferta = id

    def set_semestreAno(self, semestreAno: str) -> None:
        self.semestreAno = semestreAno

    def set_codigoOferta(self, codigoOferta: str) -> None:
        self.codigoOferta = codigoOferta

    def set_disciplina(self, disciplina: Disciplina) -> None:
        self.disciplina = disciplina

    def set_turma(self, turma: Turma) -> None:
        self.turma = turma

    def set_ativoOferta(self, ativoOferta: bool) -> None:
        self.ativoOferta = ativoOferta

    def get_idOferta(self) -> int:
        return self.idOferta

    def get_semestreAno(self) -> str:
        return self.semestreAno
    
    def get_codigoOferta(self) -> str:
        return self.codigoOferta
    
    def get_disciplina(self) -> Disciplina:
        return self.disciplina
    
    def get_turma(self) -> Turma:
        return self.turma
    
    def get_ativoOferta(self) -> bool:
        return self.ativoOferta
    
    def toJson(self) -> dict:
        json = {
            "idOferta": self.idOferta,
            "semestreAno": self.semestreAno,
            "disciplina": self.disciplina.toJson(),
            "codigoOferta": self.codigoOferta,
            "turma": self.turma.toJson()
        }

        return json