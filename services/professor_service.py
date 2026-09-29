from models.professor import Professor
from persistence.repositorio import Repositorio


class ProfessorService:
    def __init__(self, repositorio: Repositorio, modalidades: Repositorio):
        self.repositorio = repositorio
        self.modalidades = modalidades

    def cadastrar(self, professor: Professor) -> Professor:
        return self.repositorio.inserir(professor)

    def buscar(self, codigo: int) -> Professor:
        professor = self.repositorio.buscar(codigo)
        if professor is None:
            raise ValueError("Professor não encontrado.")
        return professor

    def listar(self) -> list[Professor]:
        return self.repositorio.listar()

    def atualizar(self, codigo: int, professor: Professor) -> Professor:
        return self.repositorio.atualizar(codigo, professor)

    def excluir(self, codigo: int) -> Professor:
        self.buscar(codigo)
        for modalidade in self.modalidades.listar():
            if modalidade.codigo_professor == codigo:
                raise ValueError("O professor ainda está vinculado a uma modalidade.")
        return self.repositorio.excluir(codigo)
