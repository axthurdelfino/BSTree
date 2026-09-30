from models.modalidade import Modalidade
from services.modalidade_service import ModalidadeService
from views.entrada import (
    confirmar_exclusao,
    executar_menu,
    ler_decimal,
    ler_inteiro,
    ler_texto,
)


class ModalidadeView:
    def __init__(self, service: ModalidadeService):
        self.service = service

    def menu(self) -> None:
        executar_menu(
            "Modalidades",
            {
                "1": ("Cadastrar", self.cadastrar),
                "2": ("Buscar", self.buscar),
                "3": ("Listar", self.listar),
                "4": ("Atualizar", self.atualizar),
                "5": ("Excluir", self.excluir),
            },
        )

    def exibir(self, modalidade: Modalidade) -> None:
        professor = self.service.buscar_professor(modalidade.codigo_professor)
        print(f"\nModalidade {modalidade.codigo}: {modalidade.descricao}")
        print(f"Professor {professor.codigo_prof}: {professor.nome}")
        print(f"Valor da aula: R$ {modalidade.valor_aula:.2f}")
        print(f"Alunos: {modalidade.total_alunos}/{modalidade.limite_alunos}")

    def ler_modalidade(self, codigo: int, total_alunos: int = 0) -> Modalidade:
        descricao = ler_texto("Descrição: ")
        codigo_professor = ler_inteiro("Código do professor: ")
        professor = self.service.buscar_professor(codigo_professor)
        print(f"Professor: {professor.nome}")
        return Modalidade(
            codigo,
            descricao,
            codigo_professor,
            ler_decimal("Valor da aula (R$): "),
            ler_inteiro("Limite de alunos: "),
            total_alunos,
        )

    def cadastrar(self) -> None:
        modalidade = self.ler_modalidade(ler_inteiro("Código da modalidade: "))
        self.exibir(self.service.cadastrar(modalidade))
        print("Modalidade cadastrada.")

    def buscar(self) -> None:
        self.exibir(self.service.buscar(ler_inteiro("Código da modalidade: ")))

    def listar(self) -> None:
        modalidades = self.service.listar()
        if not modalidades:
            print("Nenhuma modalidade cadastrada.")
        for modalidade in modalidades:
            self.exibir(modalidade)

    def atualizar(self) -> None:
        codigo = ler_inteiro("Código da modalidade: ")
        atual = self.service.buscar(codigo)
        self.exibir(atual)
        print("Informe os novos dados. Código e total de alunos permanecem iguais.")
        modalidade = self.ler_modalidade(codigo, atual.total_alunos)
        self.exibir(self.service.atualizar(codigo, modalidade))
        print("Modalidade atualizada.")

    def excluir(self) -> None:
        codigo = ler_inteiro("Código da modalidade: ")
        self.exibir(self.service.buscar(codigo))
        if confirmar_exclusao():
            self.service.excluir(codigo)
            print("Modalidade excluída.")
