class No:
    def __init__(self, key: int, posicao: int):
        self.key = key
        self.posicao = posicao
        self.left: No | None = None
        self.right: No | None = None


class ArvoreBinaria:
    @staticmethod
    def inserir(raiz: No, key, posicao) -> No:
        novo: No = No(key, posicao)

        if raiz is None:
            return novo

        atual: No | None = raiz
        pai: No | None = raiz

        while atual is not None:
            pai = atual
            if key == atual.key:
                raise ValueError("Chave ja existente :(")

            if key < atual.key:
                atual = atual.left
            else:
                atual = atual.right
        if key < pai.key:
            pai.left = novo
        else:
            pai.right = novo

        return raiz

    @staticmethod
    def buscar(raiz: No, key: int):
        atual: No | None = raiz
        while atual is not None:
            if key == atual.key:
                return atual
            if key < atual.key:
                atual = atual.left
            else:
                atual = atual.right

        return None

    @staticmethod
    def menor(raiz: No):
        atual: No = raiz
        while atual.left != None:
            atual = atual.left

        return atual

    @staticmethod
    def excluir(raiz: No | None, key: int) -> No | None:
        if raiz is None:
            return None

        if key < raiz.key:
            raiz.left = ArvoreBinaria.excluir(raiz.left, key)
        elif key > raiz.key:
            raiz.right = ArvoreBinaria.excluir(raiz.right, key)
        else:
            if raiz.left is None and raiz.right is None:
                return None
            elif raiz.left is None:
                return raiz.right
            elif raiz.right is None:
                return raiz.left
            else:
                aux: No = ArvoreBinaria.menor(raiz.right)
                raiz.key = aux.key
                raiz.posicao = aux.posicao
                raiz.right = ArvoreBinaria.excluir(raiz.right, aux.key)

        return raiz

    @staticmethod
    def listar_em_ordem(raiz: No | None) -> list[No]:

        nos: list[No] = []

        def percorrer(atual: No | None) -> None:
            if atual is None:
                return atual
            percorrer(atual.left)

            nos.append(atual)

            percorrer(atual.right)

        percorrer(raiz)
        return nos
