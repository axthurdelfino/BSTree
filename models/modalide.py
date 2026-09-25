class Modalidade:
    def __init__(
        self,
        codigo: int,
        descricao: str,
        codigo_professor: int,
        valor_aula: float,
        total_alunos=0,
    ):
        self.codigo = codigo
        self.descricao = descricao
        self.codigo_professor = codigo_professor
        self.valor_aula = valor_aula
