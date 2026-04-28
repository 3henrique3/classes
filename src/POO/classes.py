# Classes
# Em Poo classes são os moldes que definirão os atributos e métodos que um objeto deve seguir

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        # pass é usado para quando não temos ainda as definições dos atributos/objetos e o pass permite a classe estar vazia.

        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def mostrarPessoa(self):
        return (f"O nome da pessoa é {self.nome} {self.sobrenome}, e sua idade é {self.idade}.")
    
pessoa1 = Pessoa(
    nome = str(input("Informe o seu nome: ")),
    sobrenome = str(input("Informe o seu sobrenome: ")),
    idade = int(input("Informe a sua idade: ")),
)

print(pessoa1.mostrarPessoa())
print(type(Pessoa))


# Crie uma classe que contenha portas, motor, teto solar, marca, preço. Depois crie objetos que sejam instâncias dessa classe
# Métodos:
# - IPVA: Calcular o IPVA (4% do valor do carro) Retorne esse valor
# - Econômico? Um método que informe se o carro é econômico (condição: motor <= 1.0)

class Carro:
    def __init__(self, portas: int, motor: float, preco: float, marca: str, teto_solar = False):
        self.portas = portas
        self.motor = motor
        self.marca = marca
        self.preco = preco
        self.teto_solar = teto_solar


    def comprarCarro(self):
        if self.preco > 80.000:
            return "Aí tem grana..."

        else:
            return "Débito, crédito ou financiamento?"


    def ativar_teto_solar(self):
        if self.teto_solar == False:
            self.teto_solar = True
            return "Ativando teto solar..."

        else:
            return "Teto solar já está ativado."
        

    def descreverCarro(self):
        return (f"O carro da marca: {self.marca} e motor {self.motor} custa {self.preco}")
    
    
    def verificarEconomico(self):
        if self.motor <= 1.0:
            return "O carro é econômico."
        
        else:
            return "O carro não é econômico."

    def calcularIPVA(self):
        ipva = self.preco * 0.04
        
        return f"O IPVA do carro de modelo {self.marca} custa {ipva}"


carro1 = Carro(
    portas = int(input("Informe quantas portas tem o carro: ")),
    motor = float(input("Informe o tipo do motor do carro: ")),
    marca = str(input("Informe o nome da marca do carro: ")),
    preco = float(input("Informe o preço do carro: ")),
)

print(carro1.descreverCarro())
print(f"O Carro tem {carro1.portas} portas")

print(carro1.comprarCarro())
print(carro1.ativar_teto_solar())
print(carro1.calcularIPVA())
print(carro1.verificarEconomico())
print(carro1.ativar_teto_solar())
