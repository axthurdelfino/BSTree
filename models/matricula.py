class Matricula:
    def __init__(
        self,
        codigo_matricula: int,
        codigo_aluno: int,
        codigo_modalidade: int,
        quantidade_aulas: int,
    ):
        self.codigo_matricula = codigo_matricula
        self.codigo_aluno = codigo_aluno
        self.codigo_modalidade = codigo_modalidade
        self.quantidade_aulas = quantidade_aulas
