from models.professor import Professor
from services.professor_service import ProfessorService
from views.entrada import confirmar_exclusao, executar_menu, ler_inteiro, ler_texto


class ProfessorView:
    def __init__(self, service: ProfessorService):
        self.service = service

    def menu(self) -> None:
        executar_menu(
            "Professores",
            {
                "1": ("Cadastrar", self.cadastrar),
                "2": ("Buscar", self.buscar),
                "3": ("Listar", self.listar),
                "4": ("Atualizar", self.atualizar),
                "5": ("Excluir", self.excluir),
            },
        )

    def exibir(self, professor: Professor) -> None:
        print(f"\nProfessor {professor.codigo_prof}: {professor.nome}")
        print(f"Endereço: {professor.endereco} | Telefone: {professor.telefone}")

    def ler_professor(self, codigo: int) -> Professor:
        return Professor(
            codigo,
            ler_texto("Nome: "),
            ler_texto("Endereço: "),
            ler_texto("Telefone: "),
        )

    def cadastrar(self) -> None:
        professor = self.ler_professor(ler_inteiro("Código do professor: "))
        self.exibir(self.service.cadastrar(professor))
        print("Professor cadastrado.")

    def buscar(self) -> None:
        self.exibir(self.service.buscar(ler_inteiro("Código do professor: ")))

    def listar(self) -> None:
        professores = self.service.listar()
        if not professores:
            print("Nenhum professor cadastrado.")
        for professor in professores:
            self.exibir(professor)

    def atualizar(self) -> None:
        codigo = ler_inteiro("Código do professor: ")
        self.exibir(self.service.buscar(codigo))
        print("Informe os novos dados. O código permanece igual.")
        self.exibir(self.service.atualizar(codigo, self.ler_professor(codigo)))
        print("Professor atualizado.")

    def excluir(self) -> None:
        codigo = ler_inteiro("Código do professor: ")
        self.exibir(self.service.buscar(codigo))
        if confirmar_exclusao():
            self.service.excluir(codigo)
            print("Professor excluído.")
