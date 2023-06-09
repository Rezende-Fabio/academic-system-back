from .Turma import Turma


class Professor:
    nomeProf: str
    prontuario: str
    turma: Turma

    def set_nomeProf(self, nomeProf: str) -> None:
        self.nomeProf = nomeProf

    def set_prontuario(self, prontuario: str) -> None:
        self.prontuario = prontuario

    def set_turma(self, turma: Turma) -> None:
        self.turma = turma

    def get_nomeProf(self) -> str:
        return self.nomeProf
    
    def get_prontuario(self) -> str:
        return self.prontuario
    
    def get_turma(self) -> Turma:
        return self.turma
