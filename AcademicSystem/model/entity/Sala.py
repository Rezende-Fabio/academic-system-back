

class Sala:
    idSala: int
    local: str
    ativoSala: bool

    def set_idSala(self, idSala: int) -> None:
        self.idSala = idSala

    def set_local(self, local: str) -> None:
        self.local = local

    def set_ativoSala(self, ativo: bool) -> None:
        self.ativoSala = ativo

    def get_idSala(self) -> int:
        return self.idSala

    def get_local(self) -> str:
        return self.local
    
    def get_ativoSala(self) -> int:
        return self.ativoSala
    
    def toJson(self) -> dict:
        json = {
            "local": self.local
        }

        return json