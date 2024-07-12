from abc import ABC , abstractmethod

class Veiculo(ABC):
    def __init__(self,marca, modelo, cor):
        self._marca = marca
        self._modelo = modelo
        self._cor = cor
        self._ligado = False

    def __str__(self):
        return f'O veículo modelo {self._modelo} da marca {self._marca} de cor {self._cor} está {'Ligado' if self._ligado else 'Desligado'}'
    
    @abstractmethod
    def ligar_veiculo(self):
        pass
