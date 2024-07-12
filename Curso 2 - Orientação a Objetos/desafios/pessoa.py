class Pessoa:
    def __init__(self, nome , idade , profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return print(f'{self._nome} tem {self._idade} {'anos' if self._idade > 1 else 'ano' } de idade e trabalha com {self._profissao}')
    
    @property
    def aniversario(self):
        self._idade += 1

    def saudacao(self):
        return print(f'Olá {self._nome}, tudo bem com voce?')

