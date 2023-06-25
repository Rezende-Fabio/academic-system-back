from datetime import datetime
from .Aluno import Aluno
from .OfertaDisciplina import OfertaDisciplina


class Inscricao:
    dataInscricao: datetime
    aluno: Aluno
    ofertaDisciplina: OfertaDisciplina

    def set_dataInscricao(self, dataInscricao: datetime) -> None:
        self.dataInscricao = dataInscricao

    def set_aluno(self, aluno: Aluno) -> None:
        self.aluno = aluno

    def set_ofertaDisciplina(self, ofertaDisciplina: OfertaDisciplina) -> None:
        self.ofertaDisciplina = ofertaDisciplina

    def get_dataInscricao(self) -> datetime:
        return self.dataInscricao
    
    def get_aluno(self) -> Aluno:
        return self.aluno
    
    def get_ofertaDisciplina(self) -> OfertaDisciplina:
        return self.ofertaDisciplina

    def verificaChoqueHorario(self) -> bool:
        pass

    def verificaLimiteCredito(self) -> bool:
        pass