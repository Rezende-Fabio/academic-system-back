from .Inscricao import Inscricao


class ListaEspera:
    listaEspera: list[Inscricao]

    def set_listaEspera(self, listaEspera: list[Inscricao]) -> None:
        self.listaEspera = listaEspera

    def get_listaEspera(self) -> list[Inscricao]:
        return self.listaEspera
    
    