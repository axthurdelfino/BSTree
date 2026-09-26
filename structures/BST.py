class No:
    def __init__(self, key, posicao):
        self.key = key
        self.posicao = posicao
        self.left: No | None = None
        self.right: No | None = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz: No | None = None

    def inserir(self, key, posicao):
        no = No(key, posicao)

        if self.raiz is None:
            self.raiz = no
            return self.raiz

        atual = self.raiz
        pai = atual

        while atual is not None:
            pai = atual
            if key == atual.key:
                raise ValueError("Chave ja existente :(")

            if key < atual.key:
                atual = atual.left
            else:
                atual = atual.right
        if key < pai.key:
            pai.left = no
        else:
            pai.right = no

        return self.raiz
