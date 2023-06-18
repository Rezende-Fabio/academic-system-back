from AcademicSystem.model.entity.Disciplina import Disciplina
from AcademicSystem.model.entity.Curso import Curso


class ControleManterDisciplina:

    def mostrarDisciplinas(self) -> list[Disciplina]:
        pass

    def cadastrarDisciplina(self, siglaDisc: str, nomeDisc: str, preRequisito: list[Disciplina], curso: Curso) -> None:
        pass

    def mostrarDisciplinaDetalhado(self, id: int) -> Disciplina:
        pass

    def removerDisciplina(self, id: int) -> None:
        pass

    def editarDisciplina(self, id: int) -> None:
        pass