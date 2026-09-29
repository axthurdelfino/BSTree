from models.modalidade import Modalidade
from models.professor import Professor
from persistence.repositorio import Repositorio


class ModalidadeService:
    def __init__(
        self,
        repositorio: Repositorio,
        professores: Repositorio,
        matriculas: Repositorio,
    ):
        self.repositorio = repositorio
        self.professores = professores
        self.matriculas = matriculas

    def cadastrar(self, modalidade: Modalidade) -> Modalidade:
        self.buscar_professor(modalidade.codigo_professor)
        if modalidade.total_alunos != 0:
            raise ValueError("Uma nova modalidade deve começar sem alunos.")
        return self.repositorio.inserir(modalidade)

    def buscar(self, codigo: int) -> Modalidade:
        modalidade = self.repositorio.buscar(codigo)
        if modalidade is None:
            raise ValueError("Modalidade não encontrada.")
        return modalidade

    def listar(self) -> list[Modalidade]:
        return self.repositorio.listar()

    def buscar_professor(self, codigo: int) -> Professor:
        professor = self.professores.buscar(codigo)
        if professor is None:
            raise ValueError("Professor não encontrado.")
        return professor

    def atualizar(self, codigo: int, modalidade: Modalidade) -> Modalidade:
        atual = self.buscar(codigo)
        self.buscar_professor(modalidade.codigo_professor)
        if modalidade.total_alunos != atual.total_alunos:
            raise ValueError("O total de alunos é controlado pelas matrículas.")
        return self.repositorio.atualizar(codigo, modalidade)

    def excluir(self, codigo: int) -> Modalidade:
        self.buscar(codigo)
        for matricula in self.matriculas.listar():
            if matricula.codigo_modalidade == codigo:
                raise ValueError("Exclua as matrículas antes de excluir a modalidade.")
        return self.repositorio.excluir(codigo)
