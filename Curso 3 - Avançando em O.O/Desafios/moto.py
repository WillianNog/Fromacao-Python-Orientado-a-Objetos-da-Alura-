from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, tipo):
        super().__init__(marca, modelo,cor)
        self._tipo = tipo
    
    
    def __str__(self):
        return super().__str__() + f' e é do tipo {self._tipo}'

    def ligar_veiculo(self, estado):
        print(f'\nLigando {self._modelo} {self._cor}')
        self._ligado = estado
        print(f'{self._modelo} está {'Ligado' if self._ligado else 'Desligado'}!')
