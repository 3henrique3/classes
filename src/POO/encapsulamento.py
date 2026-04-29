# Encapsulamento é um dos pilares de POO
# Esse pilar visa proteger e controlar o acesso e o poder de modicação de dados de um objeto/classe.
# Esse pilar define as regras de como seus dados podem ser utilizados.

# Tipos de atributos
# (Nome da variável)

# public - nome
# protected - _nome
# private - __nome

# Example 1: public
class PessoaPublica:
    def __init__(self, nome: str, idade: int):

        self.nome = nome
        self.idade = idade
    
p1 = PessoaPublica(nome="Henrique", idade=100)

print(p1.nome)


# Example 2 - protected _variable
class PessoaProtegida:
    def __init__(self, nome: str, idade: int):

        self.nome = nome
        self._idade = idade
    
p2 = PessoaProtegida(nome="Henri", idade=99)
p2._idade = 98

print(p2._idade)


# Example 3 - private __variable
class PessoaPrivada:
    def __init__(self, nome: str, idade: int):

        self.nome = nome
        self.__idade = idade
    
    def mostrarIdade(self):
        return (f"Idade: {self.__idade}")
    
    
p3 = PessoaProtegida("Harry", 99)

print(p3.nome)
## print(p3.__idade) Só é possível acessar esse atributo dentro do método mostrarIdade() da própria classe.
print(p3.mostrarIdade())


# Example 4 - ContaBancária, depósito, saque, mostrar saldo
class ContaBancaria:
    def __init__(self, deposito: float, saldo: float, saque: float):
        self.deposito = deposito
        self.__saldo = saldo
        self._saque = saque


    def depositar():
        deposito = float(input("Informe quanto deseja depositar na sua conta: "))

        if deposito <= 0:
            raise ValueError("O deposito deve ser maior que 0")
        
        return deposito
    
    
conta1 = ContaBancaria.depositar()






    
        

