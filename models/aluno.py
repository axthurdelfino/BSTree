from datetime import date
from math import isfinite


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
            raise ValueError("Código é obrigatório.")
        if not isinstance(codigo, int):
            raise TypeError("Código deve ser um número inteiro.")
        if codigo < 1:
            raise ValueError("Código deve ser maior ou igual a 1.")

        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if nome is None:
            raise ValueError("Nome é obrigatório.")
        if not isinstance(nome, str):
            raise TypeError("Nome deve ser texto.")
        nome = nome.strip()
        if not nome:
            raise ValueError("Nome deve ser preenchido.")

        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if data_nascimento is None:
            raise ValueError("Data de nascimento é obrigatório.")
        if type(data_nascimento) is not date:
            raise TypeError("Data de nascimento deve ser uma data, sem horário.")
        if data_nascimento > date.today():
            raise ValueError("Data de nascimento não pode estar no futuro.")

        self.__data_nascimento = data_nascimento

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso: float):
        if peso is None:
            raise ValueError("Peso é obrigatório.")
        if not isinstance(peso, (int, float)):
            raise TypeError("Peso deve ser um número.")
        try:
            peso = float(peso)
        except OverflowError:
            raise ValueError("Peso deve ser um número finito.") from None
        if not isfinite(peso):
            raise ValueError("Peso deve ser um número finito.")
        if peso <= 0:
            raise ValueError("Peso deve ser maior que zero.")

        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura: float):
        if altura is None:
            raise ValueError("Altura é obrigatório.")
        if not isinstance(altura, (int, float)):
            raise TypeError("Altura deve ser um número.")
        try:
            altura = float(altura)
        except OverflowError:
            raise ValueError("Altura deve ser um número finito.") from None
        if not isfinite(altura):
            raise ValueError("Altura deve ser um número finito.")
        if altura <= 0:
            raise ValueError("Altura deve ser maior que zero.")

        self.__altura = altura
