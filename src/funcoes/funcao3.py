# Função com parâmetros

print("\nSaudação -")
def saudar(nome: str):
    return "Bonjour, %s!" % nome

saudacao = saudar("Roger")

print(saudacao + " Comment ça va?")

print("\nSomar -")
def somar(x: float, y):
    return f"O resultado da soma de {x} + {y} é: {x + y}."

par1 = somar(10, 10)
par2 = somar(30, 1)

print(par1)
print(par2)

print("\nProfissão -")
def empregar(nome):
    p = ""

    if nome == "Henrique":
        p = "Programador"

    else:
        p = "Go study..."
    
    return p

profissao = empregar(str(input("\nInforme o seu nome: ")))
profissao2 = empregar(str(input("Informe um outro nome: ")))

print(profissao)
print(profissao2)



