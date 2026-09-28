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

    def inserir(self, registro):
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

    def buscar(self, codigo):
        no = ArvoreBinaria.buscar(self.raiz, codigo)

        if no is None:
            return None
        with open(self.path, "r", encoding="utf-8") as arquivo:
            arquivo.seek(no.posicao)
            linha = arquivo.readline()
            dados = json.loads(linha[2:])

        return self.model.dict_para_obj(dados)

    def listar(self):
        nos_ordenados = ArvoreBinaria.listar_em_ordem(self.raiz)

        lista = []

        with open(self.path, "r", encoding="utf-8") as arquivo:
            for no in nos_ordenados:
                arquivo.seek(no.posicao)
                linha = arquivo.readline()
                dados = json.loads(linha[2:])
                objeto = self.model.dict_para_obj(dados)
                lista.append(objeto)

        return lista

    def excluir(self, codigo):
        no = ArvoreBinaria.buscar(self.raiz, codigo)

        if no is None:
            raise ValueError("Codigo nao encontrado")

        with open(self.path, "r+", encoding="UTF-8") as arquivo:
            arquivo.seek(no.posicao)
            linha = arquivo.readline()
            dados = json.loads(linha[2:])

            arquivo.seek(no.posicao)
            arquivo.write("0")

        self.raiz = ArvoreBinaria.excluir(self.raiz, codigo)

        return self.model.dict_para_obj(dados)

    def atualizar(self, codigo, registro_atualizado):
        no = ArvoreBinaria.buscar(self.raiz, codigo)

        if no is None:
            raise ValueError("Codigo nao encontrado")

        chave_atualizada = getattr(registro_atualizado, self.campo_chave)
        if chave_atualizada != codigo:
            raise ValueError("O codigo do registro nao pode ser alterado")

        dados = registro_atualizado.para_dict()
        linha_json = json.dumps(dados)

        with open(self.path, "r+", encoding="utf-8") as arquivo:
            arquivo.seek(0, 2)
            nova_posicao = arquivo.tell()
            arquivo.write(f"1|{linha_json}\n")
            arquivo.flush()

            arquivo.seek(no.posicao)
            arquivo.write("0")

        no.posicao = nova_posicao
        return registro_atualizado
