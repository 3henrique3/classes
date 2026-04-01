# def Funções são utilizadas para criar funções em Python
# Funções são blocos de código que executam uma tarefa
# São usadas para evitar repetiçõa de código

# Parâmetros são informações que a função recebe para poder executar uma função.
def printarNome(nome = str(input("Insira o seu nome: "))):
    if nome != str:
        print(f"Olá, {nome}")

printarNome()

def imprimirNome(nome: str):
    print(f"Olá, {nome}")

# Laço de repetição
print("")
while True:
    nome = input("Digite seu nome: ")

    if nome.isalpha():
        # .strip() para remover espaços vazios
        imprimirNome(nome)
        break
    else:
        print("O nome deve conter apenas letras.")


def printarNome(nome):
    print(f"Olá, {nome}")

printarNome("Henri")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descreverCarro(self):
        return f"{self.marca, self.modelo}"

carro1 = Carro("Toyota", "Corolla")
carro2 = Carro("Honda", "Civic")

print(carro1.descreverCarro())



class Smartphone:
    def __init__(self, marca, ligado = False):
        self.marca = marca
        self.ligado = ligado
        self.bateria = 10 # Bateria inicial
        self.volume = 50 # Volume inicial


    def ligar(self):
        if self.bateria == 0:
            print(f"{self.marca} sem bateria para ligar.")
            return
        if self.ligado == True:
            print(f"{self.marca} Já está ligado.")
            return
        
    # def desligar(self):
    #   if not self.ligado
    
    def carregar_bateria(self, carga: int):
        if self.bateria == 100:
            print(f"Bateria carregada.")
            return
        
        while self.bateria < 100:
            self.bateria += carga
            print(f"Bateria: {self.bateria}")

        print(f"{self.marca} carregou até completar {self.bateria}.")

    
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 10
            print(f"{self.marca} aumentando volume para {self.volume}")
            return
        
    def diminuir_volume(self):
        if self.volume < 100:
            self.volume -= 10
            print(f"{self.marca} diminuindo volume para {self.volume}")
            return
        
celular1 = Smartphone("Motorola", "True")
celular1.carregar_bateria(10)

