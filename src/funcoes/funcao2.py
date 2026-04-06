# Funções em Python

def multiplicar(x: float, y: float):
    print("Multiplicação - ")
    print(f"\nA multiplicação de {x} x {y} é: {x * y}")


num1 = float(input("\nInforme um número para x: "))
num2 = float(input("\nInforme um número para y: "))

multiplicar(num1, num2)
