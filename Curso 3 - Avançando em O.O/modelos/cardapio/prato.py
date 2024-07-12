from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome , preco , descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
    
    def __str__(self):
        return self._nome 
    
    def aplicar_desconto(self, desconto=0):
        self._preco -= (self._preco * desconto/100)    