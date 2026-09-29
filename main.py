from pathlib import Path

from models.aluno import Aluno
from models.matricula import Matricula
from models.modalidade import Modalidade
from models.professor import Professor
from persistence.repositorio import Repositorio
from services.aluno_service import AlunoService
from services.matricula_service import MatriculaService
from services.modalidade_service import ModalidadeService
from services.professor_service import ProfessorService
from views.aluno_view import AlunoView
from views.entrada import executar_menu
from views.matricula_view import MatriculaView
from views.modalidade_view import ModalidadeView
from views.professor_view import ProfessorView


def main(pasta_dados: Path | None = None) -> None:
    if pasta_dados is None:
        pasta_dados = Path(__file__).resolve().parent / "data"

    alunos = Repositorio(pasta_dados / "alunos.txt", Aluno, "codigo")
    professores = Repositorio(pasta_dados / "professores.txt", Professor, "codigo_prof")
    modalidades = Repositorio(pasta_dados / "modalidades.txt", Modalidade, "codigo")
    matriculas = Repositorio(
        pasta_dados / "matriculas.txt", Matricula, "codigo_matricula"
    )

    aluno_view = AlunoView(AlunoService(alunos, matriculas))
    professor_view = ProfessorView(ProfessorService(professores, modalidades))
    modalidade_view = ModalidadeView(
        ModalidadeService(modalidades, professores, matriculas)
    )
    matricula_view = MatriculaView(
        MatriculaService(matriculas, alunos, modalidades, professores)
    )

    print("Bem-vindo à academia PowerOn!")
    executar_menu(
        "PowerOn — Menu principal",
        {
            "1": ("Alunos", aluno_view.menu),
            "2": ("Professores", professor_view.menu),
            "3": ("Modalidades", modalidade_view.menu),
            "4": ("Matrículas", matricula_view.menu),
            "5": ("Faturamento por modalidade", matricula_view.faturamento),
        },
    )


if __name__ == "__main__":
    main()
