from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, portas):
        super().__init__(marca, modelo, cor)
        self._portas = portas

    def __str__(self):
        return super().__str__() +  f' e tem {self._portas}'
    
    def ligar_veiculo(self, estado):
        self._ligado = estado