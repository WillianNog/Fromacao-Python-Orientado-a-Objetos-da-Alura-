from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia' , 5.0 , 'Grande')
prato_paozinho = Prato('Paozinho' , 2.0 , 'O melhor pão da cidade, com patê de frango caseiro')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

bebida_suco.aplicar_desconto(8)
prato_paozinho.aplicar_desconto(5)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()