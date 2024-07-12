# Desafios Aula 2

# 1 
numero = int(input('\nDigite um numero: '))
if numero % 2 == 0:
    print(f"\nO numero {numero} é par!")
else:
    print(f"\nO numero {numero} é ímpar!")

# 2 
idade = int(input("\nDigite sua idade: "))

if 0 <= idade <=12 : 
    print(f"\nCom {idade} anos, voce é uma Criança!")
elif 13 <= idade <=18 : 
    print(f"\nCom {idade} anos, voce é um Adolescente!")
elif idade > 18 : 
    print(f"\nCom {idade} anos, voce é um Adulto!")
else : 
    print(f"\nIDADE INVÁLIDA")

# 3
usuario = input("\nDigite seu username: ")
senha = input("\nDigite sua senha: ")
user = 'WillianNog'
password = 'will123'
if user == usuario and password == senha:
    print(f"\nOlá Willian Nogueira, é bom ve-lô aqui novamente!")
elif user != usuario: 
    print('\nUsuario não encontrado no banco de dados!')     
elif senha != password:
    print('\nSenha incorreta! Tente novamente.')    

# 4
x = int(input("\nDigite a coordenada X: "))
y = int(input("\nDigite a coordenada Y: "))

def calcular_quadrante(x,y):
    if x > 0 and y > 0:
        print('\nPrimeira Quadrante')
    elif x < 0 and y > 0:
        print('\nSegundo Quadrante')
    elif x < 0 and y < 0:
        print('\nTerceiro Quadrante')
    elif x > 0 and y < 0:
        print('\nQuarto Quadrante')
    else:
        print('\nO ponto está localizado no eixo ou origem.')  

calcular_quadrante(x, y)

