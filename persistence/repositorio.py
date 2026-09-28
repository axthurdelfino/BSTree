import json
from pathlib import Path

from structures.BST import ArvoreBinaria, No


class Repositorio:
    def __init__(self, path: str | Path, model, campo_chave: str):
        self.path: Path = Path(path)
        self.model = model
        self.campo_chave = campo_chave
        self.raiz: No | None = None

        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.touch(exist_ok=True)
        self.reconstruir_indice()

    def reconstruir_indice(self) -> None:
        self.raiz = None

        with self.path.open("r", encoding="utf-8") as arquivo:
            while True:
                posicao = arquivo.tell()
                linha = arquivo.readline()

                if not linha:
                    break

                if not linha.startswith("1|"):
                    continue

                registro = json.loads(linha[2:])
                chave = registro[self.campo_chave]
                self.raiz = ArvoreBinaria.inserir(self.raiz, chave, posicao)

    def incluir(self, registro):
        chave = getattr(registro, self.campo_chave)
        if ArvoreBinaria.buscar(self.raiz, chave) is not None:
            raise ValueError("Codigo Ja Existente")

        dados = registro.para_dict()
        linha_json = json.dumps(dados)
        with open(self.path, "a", encoding="utf-8") as arquivo:
            posicao = arquivo.tell()
            arquivo.write(f"1|{linha_json}\n")
            self.raiz = ArvoreBinaria.inserir(self.raiz, chave, posicao)

        return registro
