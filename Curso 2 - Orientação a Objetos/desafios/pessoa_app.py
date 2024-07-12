from pessoa import Pessoa

pessoa1 = Pessoa("Willian", 24 , 'TI' )
pessoa2 = Pessoa(nome='Bia', idade=1 , profissao='Desing')

pessoa1.saudacao()
pessoa1.__str__()
print('''
''')
pessoa2.saudacao()
pessoa2.__str__()