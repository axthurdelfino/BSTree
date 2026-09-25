class Modalidade:
    def __init__(
        self,
        codigo: int,
        descricao: str,
        codigo_professor: int,
        valor_aula: float,
        limite_alunos: int,
        total_alunos=0,
    ):
        self.codigo = codigo
        self.descricao = descricao
        self.codigo_professor = codigo_professor
        self.valor_aula = valor_aula
        self.limite_alunos = limite_alunos
        self.total_alunos = total_alunos

    def para_dict(self):
        return {
            "codigo": self.codigo,
            "descricao": self.descricao,
            "codigo_professor": self.codigo_professor,
            "valor_aula": self.valor_aula,
            "limite_alunos": self.limite_alunos,
            "total_alunos": self.total_alunos,
        }

    @classmethod
    def dict_para_obj(cls, restaurar: dict):
        return cls(
            restaurar["codigo"],
            restaurar["descricao"],
            restaurar["codigo_professor"],
            restaurar["valor_aula"],
            restaurar["limite_alunos"],
            restaurar["total_alunos"],
        )

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if codigo is None:
            raise ValueError("Codigo nao pode ser nulo")
        if not isinstance(codigo, int):
            raise TypeError("O codigo deve ser do tipo inteiro")
        if codigo <= 0:
            raise ValueError("Codigo deve ser maior que 0")

        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if descricao is None:
            raise ValueError("Descricao nao pode ser nula")
        if not isinstance(descricao, str):
            raise TypeError("A Descricao deve ser do tipo texto")

        descricao = descricao.strip()

        if not descricao:
            raise ValueError("Preencha o campo descricao")

        self.__descricao = descricao

    @property
    def codigo_professor(self):
        return self.__codigo_professor

    @codigo_professor.setter
    def codigo_professor(self, codigo_professor: int):
        if codigo_professor is None:
            raise ValueError("Codigo do professor nao pode ser nulo")
        if not isinstance(codigo_professor, int):
            raise TypeError("O Codigo do professor deve ser do tipo inteiro")
        if codigo_professor <= 0:
            raise ValueError("Codigo do professor deve ser maior que 0")

        self.__codigo_professor = codigo_professor

    @property
    def valor_aula(self):
        return self.__valor_aula

    @valor_aula.setter
    def valor_aula(self, valor_aula: float):
        if valor_aula is None:
            raise ValueError("Valor da Aula nao pode ser Nulo")
        if not isinstance(valor_aula, (int, float)):
            raise TypeError("O Valor da aula deve ser inteiro ou float")
        if valor_aula <= 0:
            raise ValueError("Valor da Aula deve ser Maior que 0")

        self.__valor_aula = float(valor_aula)

    @property
    def limite_alunos(self):
        return self.__limite_alunos

    @limite_alunos.setter
    def limite_alunos(self, limite_alunos: int):
        if limite_alunos is None:
            raise ValueError("Valor de limite alunos nao pode ser nulo")
        if not isinstance(limite_alunos, int):
            raise TypeError("O Valor de limite alunos deve ser inteiro")
        if limite_alunos <= 0:
            raise ValueError("Valor de limite alunos deve ser maior que 0")

        self.__limite_alunos = limite_alunos

    @property
    def total_alunos(self):
        return self.__total_alunos

    @total_alunos.setter
    def total_alunos(self, total_alunos: int):
        if not isinstance(total_alunos, int):
            raise TypeError("O Valor do total de alunos deve ser do tipo inteiro")
        if total_alunos < 0:
            raise ValueError("Total alunos deve ser maior ou igual a zero")
        if total_alunos > self.__limite_alunos:
            raise ValueError(
                "Essa modadelide esta sem vagas tente novamente mais tarde"
            )
        self.__total_alunos = total_alunos
