import os

restaurantes = [{'nome':"Sam's Pizza" , 'categoria':'Pizzaria' , 'ativo':True},
                {'nome':"Tropicalia" , 'categoria':'Japonesa' , 'ativo':False},
                {'nome':"Carro de Boi" , 'categoria':'Churrascaria' , 'ativo':True}]

def exibir_nome_do_programa():
    print("""
      ⟆Ꭿᑲ𝖮ᖇ ∈ⲭᖰᖇ∈⟆⟆
      """)

def exibir_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurantes')
    print('3 - Ativar/Desativar restaurante')
    print('4 - Sair\n')

def finalizando_app():
    exibir_subtitulo('Encerrando Programa\n')    

def opcao_invalida():
    print("opção invalida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa Função é Responsável por cadastrar um novo restaurante
    Inputs:
    -Nome do Rstaurante 
    -Categoria

    Output:
    -Adiciona um novo restaurante a lista de Restaurantes
        
    '''
    exibir_subtitulo('Cadastro de novos resataurantes')
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa Função é Responsável por listar todos os restaurantes'''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa Função é Responsável por Alternar o estado dos restaurantes'''
    exibir_subtitulo('Alternando estado do restaurante')
    print('\nRestaurentes Disponíveis')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f" - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}")
    print(f"\n")

    nome_restaurante = input('Escreva o nome do restaurante que deseja Alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if  nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado: 
        print('O restaunte não foi encontrado')   
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opcao_escolhida}') 

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()  
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:   
        opcao_invalida()     
        

def main ():
    os.system ("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()   