from datetime import datetime

class Horario:
    idHorario: int
    diaSemana: str
    horaInicio: datetime
    horaFim: datetime
    ativoHorario: bool

    def set_idHorario(self, id: int) -> None:
        self.idHorario = id

    def set_diaSemana(self, diaSemana: str) -> None:
        self.diaSemana = diaSemana

    def set_horaInicio(self, horaInicio: datetime) -> None:
        self.horaInicio = horaInicio

    def set_horaFim(self, horaFim: datetime) -> None:
        self.horaFim = horaFim

    def set_ativoHorario(self, ativo: bool) -> None:
        self.ativoHorario = ativo

    def get_idHorario(self) -> int:
        return self.idHorario

    def get_diaSemana(self) -> str:
        return self.diaSemana
    
    def get_horaInicio(self) -> datetime:
        return self.horaInicio
    
    def get_horaFim(self) -> datetime:
        return self.horaFim
    
    def get_ativoHorario(self) -> bool:
        return self.ativoHorario
    
    def toJson(self) -> dict:
        json = {
            "diaSemana": self.diaSemana,
            "horaInicio": self.horaInicio,
            "horaFim": self.horaFim,
        }

        return json