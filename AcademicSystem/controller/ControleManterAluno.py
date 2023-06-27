from AcademicSystem.model.entity.Aluno import Aluno

class ControleManterAluno:

    def mostrarAlunos(self) -> list[Aluno]:
        pass

    def apresentaAlunoDetalhado(self, id: int) -> Aluno:
        pass

    def cadastrarAluno(self, nome: str, curso: str) -> None:
        pass

    def removerAluno(self, id: int) -> bool:
        pass

    def editarAluno(self, id: int) -> None:
        pass