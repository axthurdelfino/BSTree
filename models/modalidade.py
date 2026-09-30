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
        self.__total_alunos = 0
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
            raise ValueError("Código é obrigatório.")
        if not isinstance(codigo, int):
            raise TypeError("Código deve ser um número inteiro.")
        if codigo < 1:
            raise ValueError("Código deve ser maior ou igual a 1.")

        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if descricao is None:
            raise ValueError("Descrição é obrigatório.")
        if not isinstance(descricao, str):
            raise TypeError("Descrição deve ser texto.")
        descricao = descricao.strip()
        if not descricao:
            raise ValueError("Descrição deve ser preenchido.")

        self.__descricao = descricao

    @property
    def codigo_professor(self):
        return self.__codigo_professor

    @codigo_professor.setter
    def codigo_professor(self, codigo_professor: int):
        if codigo_professor is None:
            raise ValueError("Código do professor é obrigatório.")
        if not isinstance(codigo_professor, int):
            raise TypeError("Código do professor deve ser um número inteiro.")
        if codigo_professor < 1:
            raise ValueError("Código do professor deve ser maior ou igual a 1.")

        self.__codigo_professor = codigo_professor

    @property
    def valor_aula(self):
        return self.__valor_aula

    @valor_aula.setter
    def valor_aula(self, valor_aula: float):
        if valor_aula is None:
            raise ValueError("Valor da aula é obrigatório.")
        if not isinstance(valor_aula, (int, float)):
            raise TypeError("Valor da aula deve ser um número.")
        if valor_aula <= 0:
            raise ValueError("Valor da aula deve ser maior que zero.")

        self.__valor_aula = float(valor_aula)

    @property
    def limite_alunos(self):
        return self.__limite_alunos

    @limite_alunos.setter
    def limite_alunos(self, limite_alunos: int):
        if limite_alunos is None:
            raise ValueError("Limite de alunos é obrigatório.")
        if not isinstance(limite_alunos, int):
            raise TypeError("Limite de alunos deve ser um número inteiro.")
        if limite_alunos < 1:
            raise ValueError("Limite de alunos deve ser maior ou igual a 1.")
        if limite_alunos < self.__total_alunos:
            raise ValueError("O limite não pode ser menor que o total de alunos.")

        self.__limite_alunos = limite_alunos

    @property
    def total_alunos(self):
        return self.__total_alunos

    @total_alunos.setter
    def total_alunos(self, total_alunos: int):
        if total_alunos is None:
            raise ValueError("Total de alunos é obrigatório.")
        if not isinstance(total_alunos, int):
            raise TypeError("Total de alunos deve ser um número inteiro.")
        if total_alunos < 0:
            raise ValueError("Total de alunos deve ser maior ou igual a 0.")
        if total_alunos > self.__limite_alunos:
            raise ValueError("O total de alunos não pode ultrapassar o limite.")

        self.__total_alunos = total_alunos
