from ..entity.Aluno import Aluno
from ..entity.Aluno import Disciplina
from datetime import datetime


class ListaEspera:
    idLista: int
    aluno: Aluno
    disciplina: Disciplina
    dataEntrada: datetime
    ativoLista: bool

    def set_idLista(self, id: int) -> None:
        self.idLista = id

    def set_aluno(self, aluno: Aluno) -> None:
        self.aluno = aluno

    def set_disciplina(self, disciplina: Disciplina) -> None:
        self.disciplina = disciplina

    def set_dataEntrada(self, dataEntrada: datetime) -> None:
        self.dataEntrada = dataEntrada

    def set_ativoLista(self, ativoLista: bool) -> None:
        self.ativoLista = ativoLista

    def get_aluno(self) -> Aluno:
        return self.aluno
    
    def get_disciplina(self) -> Disciplina:
        return self.disciplina
    
    def get_idLista(self) -> int:
        return self.idLista
    
    def get_dataEntrada(self) -> datetime:
        return self.dataEntrada
    
    def get_ativoLista(self) -> bool:
        return self.ativoLista
      