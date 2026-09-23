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
