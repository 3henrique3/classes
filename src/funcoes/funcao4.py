# Função para definir três variáveis, e os valores escolhidos precisam ter uma condição para dizer qual valor é maior, menor ou igual a dez.
print("Verificar Número - ")
def verificarNumber(x):
    if x == 10:
        return f"O número {x} é igual a 10."
    
    elif x < 10:
        return f"O número {x} é menor que 10."

    else:
        return f"O número {x} é maior 10."


num1 = float(input("Informe um número para x: "))
num2 = float(input("Informe um número para y: "))
num3 = float(input("Informe um número para z: "))

verificarNumber(num1)
verificarNumber(num2)
verificarNumber(num3)


# Verificar uma função que retorne apenas os números pares de uma lista
print("\nVerificar números pares de uma lista.")

listaNumbers = []

def criarLista():
    listaNumbers.append(int(input("\nInforme um valor para inserir na lista de números: ")))

criarLista()

def verificarLista():
    while True:
        if listaNumbers.__len__() < 10:
            criarLista()
        else:
            break


    for numeroPar in listaNumbers:
        if numeroPar % 2 == 0:
            print(f"\nO número {numeroPar} é par.")
        else:
            continue

verificarLista()


# Calcular a média dos valores de uma lista

