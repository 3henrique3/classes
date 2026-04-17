# try/except é uma estrutura de tratamento de exceções usada para evitar
# que o programa pare com erro quando ocorre um problema durante a execução
# Permite testar um bloco de código e definir o que deve acontecer caso ocorra erro.

# Tente executar esse código, exceto se ocorrer um erro.

# try:
    # Código que pode gerar erro
# except:
    # código executado se ocorrer erro

"""
Tipos mais comuns -

ERRO                  QUANDO OCORRE

ValueError            Conversão Inválida (int("abc"))
ZeroDivisionError     Divisão por zero
TypeError             Operações entre tipos incompatíveis
IndexError            Índice inexistente em lista
KeyError              Chave inexistente em dicionário
"""

number = input("Type a number: ")

"""
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
"""

try:
    number_int = int(number)
    number_par = number_int % 2 == 0
    number_impar_texto = "Ímpar"

    if number_par:
        number_impar_texto = "Par"

    print(f"O número {number_int} é {number_impar_texto}")

except ValueError:
    print("Você não digitou um número inteiro.")


# Encurtar mais o mesmo código
try:
    numeroInteiro = int(number)
    if numeroInteiro % 2 == 0:
        print(f"O número {numeroInteiro} é par.")

    else:
        print(f"O número {numeroInteiro} é ímpar.")

except ValueError:
    print("Você não digitou um número inteiro.")

    
