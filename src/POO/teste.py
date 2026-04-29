class ContaBancaria:
    def __init__(self, saldo_inicial: float = 0):
        # Usamos __ para tornar o saldo privado (encapsulamento)
        self.__saldo = saldo_inicial

    def depositar(self, valor: float):
        if valor <= 0:
            print("O depósito deve ser maior que 0.")
        else:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado!")

    def sacar(self, valor: float):
        if valor > self.__saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado!")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

# Uso:
conta = ContaBancaria(100) 
conta.depositar(50)        
conta.sacar(30)            
conta.mostrar_saldo()      


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor <= 0:
            raise ValueError("A idade deve ser maior que 0")
        self.__idade = valor

    def mostrarPessoa(self):
        return f"Nome: {self.nome} | Idade: {self.idade}"

p1 = Pessoa("Ana", 25)
p1.idade = -10
