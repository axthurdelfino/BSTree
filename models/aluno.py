from datetime import date


class Aluno:
    def __init__(
        self, codigo: int, nome: str, data_nascimento: date, peso: float, altura: float
    ):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.altura = altura

    def calculo_imc(self) -> float:
        return self.peso / (self.altura * self.altura)

    def diagnostico_imc(self) -> str:
        imc = self.calculo_imc()

        if imc < 18.5:
            return "Abaixo do Peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        elif imc < 35:
            return "Obesidade grau 1"
        elif imc < 40:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"

    def para_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento.isoformat(),
            "peso": self.peso,
            "altura": self.altura,
        }

    @classmethod
    def dict_para_obj(cls, reconstruir: dict):
        return cls(
            reconstruir["codigo"],
            reconstruir["nome"],
            date.fromisoformat(reconstruir["data_nascimento"]),
            reconstruir["peso"],
            reconstruir["altura"],
        )

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if codigo is None:
            raise ValueError("O Codigo e obrigatorio")

        if not isinstance(codigo, int):
            raise TypeError("O Codigo deve ser um numero Inteiro")

        if codigo <= 0:
            raise ValueError("Codigo nao pode ser negativo nem 0")

        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if nome is None:
            raise ValueError("Nome e obrigatorio")

        if not isinstance(nome, str):
            raise TypeError("O Nome deve ser do tipo texto")

        nome = nome.strip()

        if not nome:
            raise ValueError("O nome tem que ser preenchido")

        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if data_nascimento is None:
            raise ValueError("Data e obrigatorio")

        if not isinstance(data_nascimento, date):
            raise TypeError("A Data de nascimento dever ser do tipo data")

        if data_nascimento > date.today():
            raise ValueError("Data de nascimento incorreta, esta no futuro.")

        self.__data_nascimento = data_nascimento

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso: float):
        if peso is None:
            raise ValueError("Peso eh obrigatorio")

        if not isinstance(peso, (int, float)):
            raise TypeError("Peso deve ser do tipo float")

        if 0 >= peso:
            raise ValueError("Peso deve ser maior que 0")

        self.__peso = float(peso)

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura: float):
        if altura is None:
            raise ValueError("Altura eh obrigatorio")

        if not isinstance(altura, (int, float)):
            raise TypeError("Altura deve ser do tipo float")

        if 0 >= altura:
            raise ValueError("Altura deve ser maior que 0")

        self.__altura = float(altura)
