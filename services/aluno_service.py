from models.aluno import Aluno
from persistence.repositorio import Repositorio


class AlunoService:
    def __init__(self, repositorio: Repositorio, matriculas: Repositorio):
        self.repositorio = repositorio
        self.matriculas = matriculas

    def cadastrar(self, aluno: Aluno) -> Aluno:
        return self.repositorio.inserir(aluno)

    def buscar(self, codigo: int) -> Aluno:
        aluno = self.repositorio.buscar(codigo)
        if aluno is None:
            raise ValueError("Aluno não encontrado.")
        return aluno

    def listar(self) -> list[Aluno]:
        return self.repositorio.listar()

    def atualizar(self, codigo: int, aluno: Aluno) -> Aluno:
        return self.repositorio.atualizar(codigo, aluno)

    def excluir(self, codigo: int) -> Aluno:
        self.buscar(codigo)
        for matricula in self.matriculas.listar():
            if matricula.codigo_aluno == codigo:
                raise ValueError("Exclua as matrículas do aluno antes de excluí-lo.")
        return self.repositorio.excluir(codigo)
