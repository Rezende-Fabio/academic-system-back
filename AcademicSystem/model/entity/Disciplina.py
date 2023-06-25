
class Disciplina:
    idDisciplina: int
    siglaDisc: str
    nomeDisc: str
    preRequisito: list["Disciplina"]
    credito: int

    def set_idDisciplina(self, idDisciplina) -> None:
        self.idDisciplina = idDisciplina

    def set_siglaDisc(self, siglaDisc: str) -> None:
        self.siglaDisc = siglaDisc

    def set_nomeDisc(self, nomeDisc: str) -> None:
        self.nomeDisc = nomeDisc

    def set_preRequisito(self, preRequisito: list["Disciplina"]) -> None:
        self.preRequisito = preRequisito

    def set_credito(self, credito: int) -> None:
        self.credito = credito

    def get_idDisciplina(self) -> int:
        return self.idDisciplina

    def get_siglaDisc(self) -> str:
        return self.siglaDisc

    def get_nomeDisc(self) -> str:
        return self.nomeDisc

    def get_preRequisito(self) -> list["Disciplina"]:
        return self.preRequisito
    
    def get_credito(self) -> int:
        return self.credito