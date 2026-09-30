from models.matricula import Matricula
from services.matricula_service import MatriculaService
from views.entrada import confirmar_exclusao, executar_menu, ler_inteiro


class MatriculaView:
    def __init__(self, service: MatriculaService):
        self.service = service

    def menu(self) -> None:
        executar_menu(
            "Matrículas",
            {
                "1": ("Cadastrar", self.cadastrar),
                "2": ("Buscar", self.buscar),
                "3": ("Listar", self.listar),
                "4": ("Atualizar quantidade de aulas", self.atualizar),
                "5": ("Excluir", self.excluir),
            },
        )

    def exibir(self, matricula: Matricula) -> None:
        aluno = self.service.buscar_aluno(matricula.codigo_aluno)
        modalidade = self.service.buscar_modalidade(matricula.codigo_modalidade)
        print(f"\nMatrícula {matricula.codigo_matricula}")
        print(f"Aluno {aluno.codigo}: {aluno.nome}")
        print(f"Modalidade {modalidade.codigo}: {modalidade.descricao}")
        print(f"Quantidade de aulas: {matricula.quantidade_aulas}")

    def cadastrar(self) -> None:
        codigo = ler_inteiro("Código da matrícula: ")
        codigo_aluno = ler_inteiro("Código do aluno: ")
        aluno = self.service.buscar_aluno(codigo_aluno)
        print(f"Aluno: {aluno.nome}")
        codigo_modalidade = ler_inteiro("Código da modalidade: ")
        modalidade = self.service.buscar_modalidade(codigo_modalidade)
        print(f"Modalidade: {modalidade.descricao}")
        print(
            f"Vagas disponíveis: {modalidade.limite_alunos - modalidade.total_alunos}"
        )
        matricula = Matricula(
            codigo,
            codigo_aluno,
            codigo_modalidade,
            ler_inteiro("Quantidade de aulas: "),
        )
        self.exibir(self.service.cadastrar(matricula))
        print("Matrícula cadastrada.")

    def buscar(self) -> None:
        self.exibir(self.service.buscar(ler_inteiro("Código da matrícula: ")))

    def listar(self) -> None:
        matriculas = self.service.listar()
        if not matriculas:
            print("Nenhuma matrícula cadastrada.")
        for matricula in matriculas:
            self.exibir(matricula)

    def atualizar(self) -> None:
        codigo = ler_inteiro("Código da matrícula: ")
        self.exibir(self.service.buscar(codigo))
        quantidade = ler_inteiro("Nova quantidade de aulas: ")
        self.exibir(self.service.atualizar(codigo, quantidade))
        print("Matrícula atualizada.")

    def excluir(self) -> None:
        codigo = ler_inteiro("Código da matrícula: ")
        self.exibir(self.service.buscar(codigo))
        if confirmar_exclusao():
            self.service.excluir(codigo)
            print("Matrícula excluída. A vaga foi liberada.")

    def faturamento(self) -> None:
        codigo = ler_inteiro("Código da modalidade: ")
        modalidade, professor, total = self.service.faturamento(codigo)
        print(f"\nModalidade {modalidade.codigo}: {modalidade.descricao}")
        print(f"Professor {professor.codigo_prof}: {professor.nome}")
        print(f"Valor faturado pelas matrículas ativas: R$ {total:.2f}")
