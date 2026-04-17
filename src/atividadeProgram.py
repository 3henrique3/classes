# 1. Programa que verifique se o número é par e se é um número inteiro.

number = input("Type a number: ")

# isdigit() é um método que verifica se todos os caracteres são numéricos
if number.isdigit():
    number_int = int(number)
    number_par = number_int % 2 == 0
    number_impar_texto = "Ímpar"

if number_par:
    number_impar_texto = "Par"
    print(f"O número {number_int} é {number_impar_texto}.")

else:
    print("Você não digitou um número inteiro.")

# ou

try:
    numeroInteiro = int(number)
    if numeroInteiro % 2 == 0:
        print(f"O número {numeroInteiro} é par.")

    else:
        print(f"O número {numeroInteiro} é ímpar.")

except ValueError:
    print("Você não digitou um número inteiro.")


# 2. Verificar se o nome do usuário é curto, normal ou grande.
# Até 4 letras curto, entre 5 e 6 normal, e maior que 6 é grande.

nome = input("Type your name: ").replace(" ", "")
# .replace(" ", "") com esses argumentos remove espaços no início, entre as palavras e no fim. Além disso pode ser usado para substituir caracteres, depende do argumento.
# .strip remove espaços no início e no fim.

"""
if len(nome) == 0:
    print("Digite pelo menos uma letra.")

else:
    size = len(nome)
    if size <= 4:
        print(f"Seu nome {nome} é curto")

    elif size > 4 and size <= 6:
        print(f"Seu nome {nome} é curto")

    else: 
        print(f"Seu nome {nome} é grnade")
"""

# ou

try:
    nomeString = str(nome)

    if nomeString:
        nomeSize = len(nomeString)

        nomeSize_short = "Curto"

    if nomeSize < 4:
        print(f"O nome {nomeString} é {nomeSize_short}.")

    elif nomeSize > 4 and nomeSize <= 6:
        nomeSize_short = "Normal"
        print(f"O nome {nomeString} é {nomeSize_short}.")

    else:
        nomeSize_short = "Grande"
        print(f"O nome {nomeString} é {nomeSize_short}.")

except ValueError:
    print("O nomé não é string.")


# 3. 