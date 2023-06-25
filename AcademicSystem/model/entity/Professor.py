
class Professor:
    idProfessor: int
    nomeProf: str
    prontuario: str
    ativoProfessor: bool

    def set_idProfessor(self, idProfessor: int) -> None:
        self.idProfessor = idProfessor

    def set_nomeProf(self, nomeProf: str) -> None:
        self.nomeProf = nomeProf

    def set_prontuario(self, prontuario: str) -> None:
        self.prontuario = prontuario

    def set_ativoProfessor(self, ativo: bool) -> None:
        self.ativoProfessor = ativo

    def get_nomeProf(self) -> str:
        return self.nomeProf
    
    def get_prontuario(self) -> str:
        return self.prontuario
    
    def get_idProfessor(self) -> int:
        return self.idProfessor
    
    def get_ativoProfessor(self) -> bool:
        return self.ativoProfessor
