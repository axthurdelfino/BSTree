from models.aluno import Aluno
from services.aluno_service import AlunoService
from views.entrada import (
    confirmar_exclusao,
    executar_menu,
    ler_data,
    ler_decimal,
    ler_inteiro,
    ler_texto,
)


class AlunoView:
    def __init__(self, service: AlunoService):
        self.service = service

    def menu(self) -> None:
        executar_menu(
            "Alunos",
            {
                "1": ("Cadastrar", self.cadastrar),
                "2": ("Buscar", self.buscar),
                "3": ("Listar", self.listar),
                "4": ("Atualizar", self.atualizar),
                "5": ("Excluir", self.excluir),
            },
        )

    def exibir(self, aluno: Aluno) -> None:
        print(f"\nAluno {aluno.codigo}: {aluno.nome}")
        print(f"Nascimento: {aluno.data_nascimento:%d/%m/%Y}")
        print(f"Peso: {aluno.peso:g} kg | Altura: {aluno.altura:g} m")
        print(f"IMC: {aluno.calculo_imc():.2f} — {aluno.diagnostico_imc()}")

    def ler_aluno(self, codigo: int) -> Aluno:
        return Aluno(
            codigo,
            ler_texto("Nome: "),
            ler_data("Nascimento (DD/MM/AAAA): "),
            ler_decimal("Peso (kg): "),
            ler_decimal("Altura (metros, exemplo 1,75): "),
        )

    def cadastrar(self) -> None:
        aluno = self.ler_aluno(ler_inteiro("Código do aluno: "))
        self.exibir(self.service.cadastrar(aluno))
        print("Aluno cadastrado.")

    def buscar(self) -> None:
        self.exibir(self.service.buscar(ler_inteiro("Código do aluno: ")))

    def listar(self) -> None:
        alunos = self.service.listar()
        if not alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            self.exibir(aluno)

    def atualizar(self) -> None:
        codigo = ler_inteiro("Código do aluno: ")
        self.exibir(self.service.buscar(codigo))
        print("Informe os novos dados. O código permanece igual.")
        self.exibir(self.service.atualizar(codigo, self.ler_aluno(codigo)))
        print("Aluno atualizado.")

    def excluir(self) -> None:
        codigo = ler_inteiro("Código do aluno: ")
        self.exibir(self.service.buscar(codigo))
        if confirmar_exclusao():
            self.service.excluir(codigo)
            print("Aluno excluído.")
