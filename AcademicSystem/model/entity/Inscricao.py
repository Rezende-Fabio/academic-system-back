from datetime import datetime
from .Aluno import Aluno
from.OfertaDisciplina import OfertaDisciplina


class Incricao:
    dataInscricao: datetime
    aluno: Aluno
    ofertaDisciplina: OfertaDisciplina