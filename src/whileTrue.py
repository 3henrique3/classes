# Laço de repetição While True













# While True com string

resposta = ""

while resposta != "sair":
    resposta = input("Type anything ou sair para encerrar o sistema: ")


print("\n-------------------------------------")

# While True com condicionais
print("While True com valor ")
saldo = float(input("\nInforme um valor maior que 0 para o seu saldo: "))

while saldo > 0:
    print(f"\nSeu saldo é de R$ {saldo}")
    debito = float(input("Informe o valor da compra: "))

    if debito < saldo:
        saldo -= debito
        print(f"\nCompra realizada no valor de {debito}")
        print(f"Saldo atual {saldo}")
    else:
        print("\nSaldo insuficiente para a compra.")
        break


# Examples
# Iteração
contador1 = 0
while contador1 <= 10:
    print(contador1)
    contador1 += 1

# Efeito contrário
contador2 = 10
while contador2 >= 1:
    print(contador2)
    contador2 -= 1

# Loop de input de string até não ficar vazio
palavra = ""
while palavra == "":
    # Entra como string, porque palavra defini como string.
    palavra = input("Digite qualquer palavra: ")
    print(f"Palavra cadastrada: {palavra}")


# Somar número até digitar zero
soma = 0

while True:
    numero = int(input(f"Digite um número para somar com {soma}: "))
    if numero != 0:
        print(f"O número atual é {soma}")
        soma += numero
        print(f"Somado com {numero} = {soma}")
    else:
        print("O número deve ser maior que zero.")
        break

# Calculadora While True

def somar():
    print("Soma: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x + y

    print(f"\nA soma de X + Y é: {z}")

def subtrair():
    print("Subtração: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x - y

    print(f"\nA subtração de X - Y é: {z}")

def multiplicar():
    print("Multiplicação: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x * y

    print(f"\nA multiplicação de X * Y é: {z}")

def dividir():
    print("Divisão: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))

    if y != 0:
        z = x / y
        print(f"\nA divisão entre X/Y é: {z}")
    else:
        print("Erro: Um número não pode ser dividido por 0.")

while True:
    print("\nCalculadora - ")
    print("Digite 1 para somar.")
    print("Digite 2 para subtrair.")
    print("Digite 3 para multiplicar.")
    print("Digite 4 para dicidir.")
    print("Digite 0 para sair.")

    menu = int(input("\nDigite o número da opção da calculadora: "))
    
    if menu == 1:
        somar()
    elif menu == 2:
        subtrair()
    elif menu == 3:
        multiplicar()
    elif menu == 4:
        dividir()
    elif menu == 5:
        break
    else:
        print("Opção inválida.")