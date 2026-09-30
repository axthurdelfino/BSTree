from datetime import date


def ler_inteiro(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")


def ler_decimal(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Digite um número (exemplo: 1,75).")


def ler_texto(mensagem: str) -> str:
    return input(mensagem)


def ler_data(mensagem: str) -> date:
    while True:
        try:
            dia, mes, ano = map(int, input(mensagem).strip().split("/"))
            return date(ano, mes, dia)
        except ValueError:
            print("Digite uma data válida no formato DD/MM/AAAA.")


def confirmar_exclusao() -> bool:
    return input("Confirmar exclusão? [s/N]: ").strip().lower() == "s"


def executar_menu(titulo: str, acoes: dict) -> None:
    while True:
        print(f"\n=== {titulo} ===")
        for opcao, (descricao, _) in acoes.items():
            print(f"{opcao} - {descricao}")
        print("0 - Voltar / sair")
        opcao = input("Opção: ").strip()
        if opcao == "0":
            return
        if opcao not in acoes:
            print("Opção inválida.")
            continue
        try:
            acoes[opcao][1]()
        except (ValueError, TypeError) as erro:
            print(f"Não foi possível concluir: {erro}")
