pessoas = [
    {'nome':'Jose', 'idade':'70', 'cidade':'Araguaia'},
    {'nome':'Willian', 'idade':'23', 'cidade':'Uberlandia'},
    {'nome':'Ana', 'idade':'23', 'cidade':'Patos de Minas'}
]

def listar_pessoas():
    for pessoa in pessoas:
        profissao = pessoa.get('profissao', '')  # Usar get para evitar KeyError
        print(pessoa['nome'], '|', pessoa['idade'], 'anos |', pessoa['cidade'], '|', profissao)

def alterar_idade():
    opt_pessoa = input('Diga o nome da pessoa que quer alterar a idade:\n')
    nova_idade = input("Digite a nova idade da pessoa:\n")
    for pessoa in pessoas:
        if pessoa['nome'] == opt_pessoa:
            pessoa['idade'] = nova_idade

def adicionar_profissao():
    opt_pessoa = input('Diga o nome da pessoa que quer adicionar uma profissão:\n')
    profissao = input("Digite a profissão da pessoa:\n")
    for pessoa in pessoas:
        if pessoa['nome'] == opt_pessoa:
            pessoa['profissao'] = profissao

def deletar_todas_profissoes():
    print('Deletando Profissoes...')
    for pessoa in pessoas:
        if 'profissao' in pessoa:
            del pessoa['profissao']


listar_pessoas()

adicionar_profissao()

listar_pessoas()

deletar_todas_profissoes()

listar_pessoas()
