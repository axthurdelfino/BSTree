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

    def para_dict(self):
        return {
            "codigo_matricula": self.codigo_matricula,
            "codigo_aluno": self.codigo_aluno,
            "codigo_modalidade": self.codigo_modalidade,
            "quantidade_aulas": self.quantidade_aulas,
        }

    @classmethod
    def dict_para_obj(cls, reconstruir: dict):
        return cls(
            reconstruir["codigo_matricula"],
            reconstruir["codigo_aluno"],
            reconstruir["codigo_modalidade"],
            reconstruir["quantidade_aulas"],
        )

    @property
    def codigo_matricula(self):
        return self.__codigo_matricula

    @codigo_matricula.setter
    def codigo_matricula(self, codigo_matricula: int):
        if codigo_matricula is None:
            raise ValueError("Código da matrícula é obrigatório.")
        if not isinstance(codigo_matricula, int):
            raise TypeError("Código da matrícula deve ser um número inteiro.")
        if codigo_matricula < 1:
            raise ValueError("Código da matrícula deve ser maior ou igual a 1.")

        self.__codigo_matricula = codigo_matricula

    @property
    def codigo_aluno(self):
        return self.__codigo_aluno

    @codigo_aluno.setter
    def codigo_aluno(self, codigo_aluno: int):
        if codigo_aluno is None:
            raise ValueError("Código do aluno é obrigatório.")
        if not isinstance(codigo_aluno, int):
            raise TypeError("Código do aluno deve ser um número inteiro.")
        if codigo_aluno < 1:
            raise ValueError("Código do aluno deve ser maior ou igual a 1.")

        self.__codigo_aluno = codigo_aluno

    @property
    def codigo_modalidade(self):
        return self.__codigo_modalidade

    @codigo_modalidade.setter
    def codigo_modalidade(self, codigo_modalidade: int):
        if codigo_modalidade is None:
            raise ValueError("Código da modalidade é obrigatório.")
        if not isinstance(codigo_modalidade, int):
            raise TypeError("Código da modalidade deve ser um número inteiro.")
        if codigo_modalidade < 1:
            raise ValueError("Código da modalidade deve ser maior ou igual a 1.")

        self.__codigo_modalidade = codigo_modalidade

    @property
    def quantidade_aulas(self):
        return self.__quantidade_aulas

    @quantidade_aulas.setter
    def quantidade_aulas(self, quantidade_aulas: int):
        if quantidade_aulas is None:
            raise ValueError("Quantidade de aulas é obrigatório.")
        if not isinstance(quantidade_aulas, int):
            raise TypeError("Quantidade de aulas deve ser um número inteiro.")
        if quantidade_aulas < 1:
            raise ValueError("Quantidade de aulas deve ser maior ou igual a 1.")

        self.__quantidade_aulas = quantidade_aulas
