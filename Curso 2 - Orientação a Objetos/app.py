from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça' , 'gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('JAPA', 'JAPONESA ')

restaurante_japones.alternar_estado()
restaurante_japones.receber_avaliacao('Gui', 10)
restaurante_japones.receber_avaliacao('Lais', 5)
restaurante_japones.receber_avaliacao('Emi', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()