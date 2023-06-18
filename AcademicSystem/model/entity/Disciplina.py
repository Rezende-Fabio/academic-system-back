from .Curso import Curso

class Disciplina:
    siglaDisc: str
    nomeDisc: str
    preRequisito: list["Disciplina"]
    credito: int
    curso: Curso

    def set_siglaDisc(self, siglaDisc: str) -> None:
        self.siglaDisc = siglaDisc

    def set_nomeDisc(self, nomeDisc: str) -> None:
        self.nomeDisc = nomeDisc

    def set_preRequisito(self, preRequisito: list["Disciplina"]) -> None:
        self.preRequisito = preRequisito

    def set_credito(self, credito: int) -> None:
        self.credito = credito

    def set_curso(self, curso: Curso) -> None:
        self.curso = curso

    def get_siglaDisc(self) -> str:
        return self.siglaDisc

    def get_nomeDisc(self) -> str:
        return self.nomeDisc

    def get_preRequisito(self) -> list["Disciplina"]:
        return self.preRequisito
    
    def get_credito(self) -> int:
        return self.credito
    
    def get_curso(self) -> Curso:
        return self.curso