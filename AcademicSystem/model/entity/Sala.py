from .Turma import Turma


class Sala:
    local: str
    turma: Turma

    def set_local(self, local: str) -> None:
        self.local = local

    def set_turma(self, turma: Turma) -> None:
        self.turma = turma

    def get_local(self) -> str:
        return self.local
    
    def get_turma(self) -> Turma:
        return self.turma