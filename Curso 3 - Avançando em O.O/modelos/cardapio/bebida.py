from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, name, preco , tamanho):
        super().__init__(name, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome 

    def aplicar_desconto(self, desconto=0):
        self._preco -= (self._preco * desconto/100)    