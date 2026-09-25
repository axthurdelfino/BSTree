class Professor:
    def __init__(self, codigo_prof: int, nome: str, endereco: str, telefone: str):
        self.codigo_prof = codigo_prof
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def para_dict(self):
        return {
            "codigo_prof": self.codigo_prof,
            "nome": self.nome,
            "endereco": self.endereco,
            "telefone": self.telefone,
        }

    @classmethod
    def dict_para_obj(cls, reconstruir: dict):
        return cls(
            reconstruir["codigo_prof"],
            reconstruir["nome"],
            reconstruir["endereco"],
            reconstruir["telefone"],
        )

    @property
    def codigo_prof(self):
        return self.__codigo_prof

    @codigo_prof.setter
    def codigo_prof(self, codigo_prof: int):
        if codigo_prof is None:
            raise ValueError("Insira o codigo do Professor")

        if not isinstance(codigo_prof, int):
            raise TypeError("O Valor inserido deve ser inteiro")

        if codigo_prof <= 0:
            raise ValueError("Codigo deve ser maior que 0")

        self.__codigo_prof = codigo_prof

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if nome is None:
            raise ValueError("Insira um nome")
        if not isinstance(nome, str):
            raise TypeError("O Valor inserido deve ser do tipo texto")

        nome = nome.strip()

        if not nome:
            raise ValueError("O Nome deve ser preenchido")

        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if endereco is None:
            raise ValueError("Insira um endereco")
        if not isinstance(endereco, str):
            raise TypeError("O Valor inserido deve ser do tipo texto")

        endereco = endereco.strip()

        if not endereco:
            raise ValueError("O Endereco deve ser preenchido")

        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: str):
        if telefone is None:
            raise ValueError("Insira um Telefone")

        if not isinstance(telefone, str):
            raise TypeError("O valor inserido deve obedecer o formato telefone")

        telefone = telefone.strip()

        if not telefone:
            raise ValueError("Preencha o campo Telefone")

        self.__telefone = telefone
