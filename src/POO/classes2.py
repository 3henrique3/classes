"""
Uma classe Animal de estimação
a cat, a dog and a parrot

Methods:
- Properties: name, size and espécie;
- Métodos: eat(), sleep() and play(), 
- Obs.: O método eat() deve receber um parâmetro que representa o tipo de alimento que o animal come;
- Obs.: O método brincar() deve receber um parâmetro que representa o tipo de brinquedo com o qual o animal brinca.
- Obs.: O método sleep() deve print a message indicando que o animal está dormindo.
- Crie três instâncias da classe Animal, uma para cada animal de estimação.

"""

class Animal:
    def __init__(self, nome: str, peso: int, especie: str):
        self.nome = nome
        self.peso = peso
        self.especie = especie

    def eat(self):
        if self.especie == "gato":
            return (f"O seu gato {self.name} está comendo peixe.")
        
        elif self.especie == "cachorro":
            return (f"O seu cachorro {self.name} está comendo carne.")
        
        else:
            return (f"O seu papagaio {self.name} está comendo ração.")
        
    def sleep(self):
        if self.especie == "gato":
            return (f"O seu gato {self.name} está dormindo.")
        
        elif self.especie == "cachorro":
            return (f"O seu cachorro {self.name} está dormindo.")
        
        else:
            return (f"O seu papagaio {self.name} está dormindo.")
        
    def play(self):
        if self.especie == "gato":
            return (f"O seu gato {self.name} está brincando com o arranhador.")
        
        elif self.especie == "cachorro":
            return (f"O seu cachorro {self.name} está brincando com a bola.")
        
        else:
            return (f"O seu papagaio {self.name} está brincando no playground.")
        
    def descreverAnimal(self):
        return (f"O seu animal de estimação {self.nome} é um {self.especie} e pesa {self.peso}.")
    

animal1 = Animal(
    nome = str(input("\nInforme o nome do seu animal de estimação: ")),
    peso = int(input("Informe o peso do seu animal de estimação: ")),
    especie = str(input("Informe a especie do seu animal de estimação: ")),
)

animal2 = Animal(
    nome = str(input("\nInforme o nome do seu animal de estimação: ")),
    peso = int(input("Informe o peso do seu animal de estimação: ")),
    especie = str(input("Informe a especie do seu animal de estimação: ")),
)

animal3 = Animal(
    nome = str(input("\nInforme o nome do seu animal de estimação: ")),
    peso = int(input("Informe o peso do seu animal de estimação: ")),
    especie = str(input("Informe a especie do seu animal de estimação: ")),
)

print(animal1.descreverAnimal())
print(animal2.descreverAnimal())
print(animal3.descreverAnimal())


while True:
    print("\nAnimal de estimação - ")
    print("Digite 1 para selecionar o animal 1.")
    print("Digite 2 para selecionar o animal 2.")
    print("Digite 3 para selecionar o animal 3.")
    print("Digite 0 para sair.")

    menu = int(input("\nDigite o número da opção: "))

    if menu == 1:
        animal = animal1
        
        while True:
            print("\nAnimal de estimação - ")
            print("Digite 1 para selecionar o animal 1.")
            print("Digite 2 para selecionar o animal 2.")
            print("Digite 3 para selecionar o animal 3.")
            print("Digite 0 para sair.")



