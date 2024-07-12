from moto import Moto 
from carro import Carro

moto1 = Moto('Yamaha', 'Fazer 150cc', 'Laranja' , 'Casual')
moto2 = Moto('Honda', 'Hornet', 'Preto','Esportiva')
carro1 = Carro('Fiat','Uno', 'Amarelo', '4 portas')
carro2 = Carro('Dodge','Charger','Verde' , '2 portas')

def main():
    print(moto1)
    print(moto2)
    print(carro1)
    print(carro2)

    moto1.ligar_veiculo(True)
    print(f'\n{moto1}')

if __name__ == "__main__":
    main()