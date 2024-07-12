# 1
lista_numeros = [15, 29, 356, 42, 54] 
lista_nomes = ['Ana', 'Jack', 'Zoe', 'Gertrude']
lista_nascimento = [2000, 2014]

# 2
print('\nLista de numeros\n')
for item in lista_numeros:
    print(item)

print('\nLista de nomes\n')
for item in lista_nomes:
    print(item)

print('\nLista de nascimento\n')
for item in lista_nascimento:
    print(item)

# 3
soma_impares = 0
for item in lista_numeros:
    if item % 2 != 0:
        soma_impares += item        
print(f'\nO valor somado dos números Ímpares da lista de números é:', soma_impares, '\n')

# 4
lista_numeros_descrescente = sorted(lista_numeros, reverse=True)

print('\nLista de números em ordem decrescente\n')
for item in lista_numeros_descrescente:
    print(item)
print()

# 5
numero = int(input('Digite um número para saber a sua tabuada de 10: '))
print()
num = 0
while num <= 10:
    print(f'{numero} x {num} = {num * numero}')
    num = num + 1
print()

# 6
somatoria = 0 
lista_num = [15,12,43,467,5]
try:
    for item in lista_num:
        somatoria += item
    print(somatoria)
except:
    print('Número inválido')

print()

# 7 
soma = 0
media = 0
try:
    tamanho = len(lista_num)
    for item in lista_num:
        soma +=  item

    media = soma/tamanho
    print(media , '\n')    
except:
    print('Opção inválida ou lista vazia, comece novamente\n')    