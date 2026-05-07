"""
Atividade Herança e Encapsulamento

Estudante: Pedro Henrique
06/07/2026
"""

# 1.
# Sistema de contas de banco
"""
Um banco digital está expandindo seu sistema financeiro e percebeu a necessidade de reorganizar a estrutura das contas dos clientes. Atualmente, todas as contas possuem características em comum, como número da conta, titular e controle de saldo, porém cada tipo de conta possui comportamentos específicos dentro do sistema.

Além disso, a equipe identificou um problema grave: alguns desenvolvedores estavam acessando e alterando diretamente o saldo das contas, comprometendo a segurança das informações financeiras e permitindo operações inválidas.

Como desenvolvedor responsável pela nova arquitetura do sistema, crie uma solução orientada a objetos utilizando herança e encapsulamento para representar diferentes tipos de contas bancárias, garantindo reutilização de código, especialização de comportamentos e proteção adequada dos dados financeiros da aplicação. 
"""

class Conta:
    def __init__(self, numero_conta: int, titular: str):
        self._numero_conta = numero_conta
        self.__titular = titular

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def titular(self):
        return self.__titular


class Conta_poupanca(Conta):
    def __init__(self, numero_conta, titular, saldo: float):
        super().__init__(numero_conta, titular)
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, definir_saldo):
        if definir_saldo < 100:
            raise ValueError("O saldo da conta poupança deve ser maior ou igual a R$ 100,00.")
        
        self.__saldo = definir_saldo
    
    def sacar(self, saque):
        if saque <= 0 and saque > self.saldo:
            raise ValueError("O saque não pode ser maior que o seu saldo e menor que zero.")
        
        self.saldo -= saque
        print(f"Saque realizado da conta: {self.numero_conta}.")
        print(f"Saldo: {self.saldo}")

class Conta_corrente(Conta):
    def __init__(self, numero_conta, titular, saldo: float = 0):
        super().__init__(numero_conta, titular)
        
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, definir_saldo):
        if definir_saldo < 0:
            raise ValueError("O saldo da conta corrente não pode ser menor que zero.")
        
        self.__saldo = definir_saldo
    
    def depositar(self, deposito: float):
        if deposito <= 0:
            raise ValueError("O deposito não pode ser menor ou igual a zero.")
        
        self.saldo += deposito
        print(f"Deposito realizado na conta {self.numero_conta}")
        print(f"Saldo: {self.saldo}")

    def sacar(self, saque):
        if saque <= 0 and saque > self.saldo:
            raise ValueError("O saque não pode ser maior que o seu saldo e menor que zero.")
        
        self.saldo -= saque
        print(f"Saque realizado da conta: {self.numero_conta}.")
        print(f"Saldo: {self.saldo}")


conta1 = Conta_poupanca(1111, "Henrique", 10000.10)
conta1.sacar(100)

conta2 = Conta_corrente(2222, "Henri")
conta2.depositar(1999.99)
conta2.sacar(200.50)


# 2.



    



    

        
