from datetime import datetime
from .Turma import Turma

class Horario:
    diaSemana: str
    horaInicio: datetime
    horaFim: datetime
    turma: Turma
