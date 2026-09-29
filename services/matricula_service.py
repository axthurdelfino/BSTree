from decimal import Decimal

from models.aluno import Aluno
from models.matricula import Matricula
from models.modalidade import Modalidade
from models.professor import Professor
from persistence.repositorio import Repositorio


class MatriculaService:
    def __init__(
        self,
        repositorio: Repositorio,
        alunos: Repositorio,
        modalidades: Repositorio,
        professores: Repositorio,
    ):
        self.repositorio = repositorio
        self.alunos = alunos
        self.modalidades = modalidades
        self.professores = professores

    def buscar_aluno(self, codigo: int) -> Aluno:
        aluno = self.alunos.buscar(codigo)
        if aluno is None:
            raise ValueError("Aluno não encontrado.")
        return aluno

    def buscar_modalidade(self, codigo: int) -> Modalidade:
        modalidade = self.modalidades.buscar(codigo)
        if modalidade is None:
            raise ValueError("Modalidade não encontrada.")
        return modalidade

    def cadastrar(self, matricula: Matricula) -> Matricula:
        self.buscar_aluno(matricula.codigo_aluno)
        modalidade = self.buscar_modalidade(matricula.codigo_modalidade)
        if modalidade.total_alunos >= modalidade.limite_alunos:
            raise ValueError("A modalidade está sem vagas.")

        modalidade.total_alunos += 1
        self.repositorio.inserir(matricula)
        self.modalidades.atualizar(modalidade.codigo, modalidade)
        return matricula

    def buscar(self, codigo: int) -> Matricula:
        matricula = self.repositorio.buscar(codigo)
        if matricula is None:
            raise ValueError("Matrícula não encontrada.")
        return matricula

    def listar(self) -> list[Matricula]:
        return self.repositorio.listar()

    def atualizar(self, codigo: int, quantidade_aulas: int) -> Matricula:
        matricula = self.buscar(codigo)
        matricula.quantidade_aulas = quantidade_aulas
        return self.repositorio.atualizar(codigo, matricula)

    def excluir(self, codigo: int) -> Matricula:
        matricula = self.buscar(codigo)
        modalidade = self.buscar_modalidade(matricula.codigo_modalidade)
        modalidade.total_alunos -= 1
        self.repositorio.excluir(codigo)
        self.modalidades.atualizar(modalidade.codigo, modalidade)
        return matricula

    def faturamento(
        self, codigo_modalidade: int
    ) -> tuple[Modalidade, Professor, Decimal]:
        modalidade = self.buscar_modalidade(codigo_modalidade)
        professor = self.professores.buscar(modalidade.codigo_professor)
        if professor is None:
            raise ValueError("Professor da modalidade não encontrado.")

        total = Decimal(0)
        valor_aula = Decimal(str(modalidade.valor_aula))
        for matricula in self.listar():
            if matricula.codigo_modalidade == codigo_modalidade:
                total += valor_aula * matricula.quantidade_aulas
        return modalidade, professor, total
