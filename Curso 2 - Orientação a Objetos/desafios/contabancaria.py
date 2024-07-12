class ContaBancaria:
    def __init__(self,titular,saldo=False):
        self._titular = titular
        self._saldo = saldo
    
    def __str__(self):
       return print(f'Títular: {self._titular.ljust(20)} | Saldo: {str(self._saldo)} {'reais'.ljust(20) if self._saldo else ''}')
    
    @property
    def ativar_conta(self):
        self._ativo = True
        return print(f'Agora a conta com Títular {self._titular} está ativa!')
    
    

conta1 = ContaBancaria('Willian' , 100)
conta2 = ContaBancaria('Jusé' , 10000)
conta3 = ContaBancaria('Maria')


conta1.__str__()
conta2.__str__()
conta3.__str__()


conta2.ativar_conta