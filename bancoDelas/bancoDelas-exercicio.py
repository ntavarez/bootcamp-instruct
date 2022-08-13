class Banco():
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal
    
class ContaCorrente():
    def __init__(self, saldo):
        self._saldo = saldo
    
    def saque(self, saque_valor):
        self._saldo = self._saldo - saque_valor
    
    def deposito(self, deposito_valor):
        self._saldo = self._saldo + deposito_valor

class TitularHomem(Banco,ContaCorrente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def get_nome(self): 
        return self._nome

    def set_nome(self, nome): 
        self._nome = nome
    
    def get_telefone(self): 
        return self._telefone

    def set_telefone(self, telefone): 
        self._telefone = telefone

    def get_renda_mensal(self): 
        return self._renda_mensal

    def set_renda_mensal(self, renda_mensal): 
        self._renda_mensal = renda_mensal

    def saque(self, conta, saque_valor):
        if  saque_valor > conta._saldo:
            print(f'{self._nome}, não foi possível efetuar o saque: valor maior que o saldo disponível em conta! Saldo atual: R$ {conta._saldo:.2f}')
        else:
            conta._saldo = conta._saldo - saque_valor
            print(f'{self._nome}, saque de R$ {saque_valor:.2f} efetuado com sucesso! Saldo atual: R$ {conta._saldo:.2f}')
    
    def deposito(self, conta, deposito_valor):
        conta._saldo = conta._saldo + deposito_valor
        print(f'{self._nome}, depósito de R$ {deposito_valor:.2f} efetuado com sucesso! Saldo atual: R$ {conta._saldo:.2f}')

class TitularMulher(Banco,ContaCorrente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.cheque_especial = self._renda_mensal
        self.limite = -self._renda_mensal
        self.limite_acumulado = 0.00
    
    def get_nome(self): 
        return self._nome

    def set_nome(self, nome): 
        self._nome = nome
    
    def get_telefone(self): 
        return self._telefone

    def set_telefone(self, telefone): 
        self._telefone = telefone

    def get_renda_mensal(self): 
        return self._renda_mensal

    def set_renda_mensal(self, renda_mensal): 
        self._renda_mensal = renda_mensal
    
    def saque(self, conta, saque_valor):
        if saque_valor > conta._saldo and (conta._saldo - saque_valor) < 0:
            limite_utilizado = conta._saldo - saque_valor
            conta._saldo = 0

            if limite_utilizado > self.limite and limite_utilizado < 0 and (limite_utilizado + self.limite_acumulado) > self.limite:
                self.limite_acumulado = self.limite_acumulado + limite_utilizado
                restante_cheque = (self.limite) - (self.limite_acumulado)

                print(f'{self._nome}, saque de R$ {saque_valor:.2f} efetuado com sucesso! Saldo atual: R$ {conta._saldo:.2f} [Atenção, valor retirado do Cheque Especial! ** Limite total: R$ {abs(self.limite):.2f} Limite utilizado: R$ {abs(self.limite_acumulado):.2f} Limite restante: R$ {abs(restante_cheque):.2f} **]')
            else:
                print(f'{self._nome}, não foi possível efetuar o saque: valor solicitado maior do que saldo em conta e limite do Cheque Especial! Saldo atual: R$ {conta._saldo:.2f}')
        else:
            conta._saldo = conta._saldo - saque_valor
            print(f'{self._nome}, saque de R$ {saque_valor:.2f} efetuado com sucesso! Saldo atual: R$ {conta._saldo:.2f}')

    def deposito(self, conta, deposito_valor):
        conta._saldo = conta._saldo + deposito_valor
        print(f'{self._nome}, depósito de R$ {deposito_valor:.2f} efetuado com sucesso! Saldo atual: R$ {conta._saldo:.2f}')


conta_1 = ContaCorrente(0.00)
conta_2 = ContaCorrente(0.00)

homem = TitularHomem('Diogo','999999-9999', 5500.00)
homem.saque(conta_1, 10.00)
homem.deposito(conta_1, 500.00)
homem.saque(conta_1, 400.00)
homem.deposito(conta_1, 500.50)
homem.saque(conta_1, 700.00)

mulher = TitularMulher('Natália','888888-8888', 8400.00)
mulher.deposito(conta_2, 8000.00)
mulher.saque(conta_2, 450.00)
mulher.deposito(conta_2, 300.00)
mulher.saque(conta_2, 9000.00)
mulher.saque(conta_2, 600.00)
mulher.saque(conta_2, 7000.00)

