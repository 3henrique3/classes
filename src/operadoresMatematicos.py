# Operadores matemáticos

"""
Comentário

divisão / retorna um número de ponto flutuante
divisão interia // retorna um número um número inteiro
resto da divisão %
potência **

"""

# Calculadora

def somar():
    print("Soma: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x + y

    print(f"A soma de X + Y é: {z}")

def subtrair():
    print("Subtração: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x - y

    print(f"A subtração de X - Y é: {z}")

def dividir():
    print("Divisão: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x / y

    print(f"A divisão entre X e Y é: {z}")

def dividirInteiro():
    print("Divisão inteira: ")

    x = int(input("\nInforme um número para X: "))
    y = int(input("Informe um número para Y: "))
    z = x // y

    print(f"A divisão inteira entre X e Y é: {z}")

def restoDividir():
    print("Resto da divisão: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x % y

    print(f"O resto da divisão entre X e Y é: {z}")

def potenciar():
    print("Potenciação: ")

    x = int(input("\nInforme um número para X: "))
    y = int(input("Informe um número para Y: "))
    z = x ** y

    print(f"X potenciado com Y é: {z}")


def calcular():
