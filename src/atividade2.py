# Atividade - Condicionais e Loop FOR em Python

#1, 2 e 4
def verificarCondicao():
    renda = float(input("\nQual a sua renda mensal: "))
    nomeLimpo = str(input("\nPossui nome limpo? Use 's' para Sim ou 'n' para Não: "))

    if renda >= 1000 and nomeLimpo == "s":
        rendaPermitida = True
        semNegativacao = True
    elif renda >= 1000 and nomeLimpo == "n":
        rendaPermitida = True
        semNegativacao = False
    elif renda < 1000 and nomeLimpo == "s":
        rendaPermitida = False
        semNegativacao = True
    else:
        rendaPermitida = False
        semNegativacao = False
    
    if rendaPermitida and semNegativacao:
        print("Você está apto(a) para Quintas da Colina.")
    
    else:
        print("Você não está apto(a) para Quintas da Colina.")

verificarCondicao()
print("\n=================================")



#3
def verificarNumero():
    numero = int(input("\nInsira um número inteiro: "))
    numeroPar = numero % 2

    if numero >= 0 and numeroPar == 0:
        print(f"\nO número {numero} é par.")
    elif numero < 0 :
        print(f"\nO número não pode ser negativo.")
    else:
        print(f"\nO número {numero} é ímpar.")

verificarNumero()
print("\n=================================")


#5 e 6
for numero in range(1, 10, 2):
    print(numero)
print("\n=================================")

#7 e 8
def repetirFinito():
    palavra = "fruta"
    for letra in palavra:
        if letra == "f":
            print(f"{letra} - letra 1")
        elif letra == "r":
            print(f"{letra} - letra 2")
        elif letra == "u":
            print(f"{letra} - letra 3")
        elif letra == "t":
            print(f"{letra} - letra 4")
        elif letra == "a":
            print(f"{letra} - letra 5")

repetirFinito()
print("\n=================================")

#9 e 10
def repetirVerificacao():
    for number in range(1, 11):
        if number % 2 == 0:
            print(f"{number} - é par.")
        else:
            print(f"{number} - é ímpar.")

repetirVerificacao()

        

