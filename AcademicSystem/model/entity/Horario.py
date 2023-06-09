from datetime import datetime
from .Turma import Turma


class Horario:
    diaSemana: str
    horaInicio: datetime
    horaFim: datetime
    turma: Turma

    def set_diaSemana(self, diaSemana: str) -> None:
        self.diaSemana = diaSemana

    def set_horaInicio(self, horaInicio: datetime) -> None:
        self.horaInicio = horaInicio

    def set_horaFim(self, horaFim: datetime) -> None:
        self.horaFim = horaFim

    def set_turma(self, turma: Turma) -> None:
        self.turma = turma

    def get_diaSemana(self) -> str:
        return self.diaSemana
    
    def get_horaInicio(self) -> datetime:
        return self.horaInicio
    
    def get_horaFim(self) -> datetime:
        return self.horaFim
    
    def get_turma(self) -> Turma:
        return self.turma