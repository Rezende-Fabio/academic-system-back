from .Inscricao import Inscricao


class ListaEspera:
    idLista: int
    listaEspera: list[Inscricao]
    ativoLista: bool

    def set_idLista(self, id: int) -> None:
        self.idLista = id

    def set_listaEspera(self, listaEspera: list[Inscricao]) -> None:
        self.listaEspera = listaEspera

    def set_ativoLista(self, ativoLista: bool) -> None:
        self.ativoLista = ativoLista

    def get_listaEspera(self) -> list[Inscricao]:
        return self.listaEspera
    
    def get_idLista(self) -> int:
        return self.idLista
    
    def get_ativoLista(self) -> bool:
        return self.ativoLista
      