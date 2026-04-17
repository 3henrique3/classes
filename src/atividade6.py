# Atividade 5 - Tratamento de exceções com try/except
# Estudante: Pedro Henrique
# 15/04/2026

# 1. Receber um número e mostrar o valor em dobro.
# Caso não seja um número recebido retorne "Valor inválido par número inteiro."
print("\nNúmero em dobro - ")

number = input("Informe um número inteiro: ")

try:
    numeroInteiro = int(number)
    numeroDobro = numeroInteiro * 2

    if numeroInteiro:
        print(f"O número {numeroInteiro} em dobro é {numeroDobro}.")


except ValueError:
    print("Você não digitou um número inteiro.")


# 2. Solicitar ao usuário dois números inteiros para realizar a divisão.
# Tratar erro caso o usuário digite um número inválido ou tente dividir por zero.
print("\nDivisão - ")

num1 = input("Informe um número: ")
num2 = input("Informe mais um número: ")

try:
    numero_1 = int(num1)
    numero_2 = int(num2)

    if numero_1 and numero_2:
        divisao = numero_1 / numero_2
        print(f"{numero_1} dividido por {numero_2} é {divisao}.")
    
    elif numero_1 == 0 or numero_2 == 0:
        print("Não pode haver divisão por 0.")

    
except ZeroDivisionError:
    print("A divisão não pode ser com zero.")

except ValueError:
    print("Insira somente números inteiros.")


# 3. Receber a idade para verificar se é maior ou menor de idade, 
# e tratar erro caso não seja um número inteiro.
print("\nVerificação de idade - ")

idade = input("Informe sua idade: ")
try:
    idadeInteira = int(idade)

    if idadeInteira >= 18:
        print("Você é maior de idade.")

    else:
        print("Você é menor de idade.")
    
except ValueError:
    print("A idade deve ser um número inteiro.")


# 4. Receber um número decimal/float e retornar a raíz quadrada.
# Tratar erro caso não seja um número decimal/float.
print("\nRaíz quadrada de número decimal/float - ")

numero = input("Informe um número decimal: ")

try:
    numero_decimal_float = float(numero)
    raizQuadrada = numero_decimal_float ** 0.5

    if numero_decimal_float >= 0:
        print(f"A raíz quadrada de {numero_decimal_float} é {raizQuadrada}.")
        
    else:
        print("Não se calcula raíz quadrada de números negativos.")

except ValueError:
    print("Você não digitou um número decimal/float.")


# 5. Receber um número inteiro e verificar se é positivo, negativo ou zero.
# Tratar erro caso não seja um número inteiro.
print("\nVerificação de número positivo, negativo ou zero - ")

numero = input("Informe um número inteiro: ")

try:
    numeroInteiro = int(numero)

    if numeroInteiro > 0:
        print(f"O número {numeroInteiro} é positivo.")

    elif numeroInteiro < 0:
        print(f"O número {numeroInteiro} é negativo.")

    else:
        print("O número é zero.")

except ValueError:
    print("Você não digitou um número inteiro.")


# 6. Solicitar ao usuário que acesse um índice de uma lista com cinco nomes.
# Tratar erro caso o índice não exista (Índice inválido).
print("\Acessar índice de lista - ")

nome_lista = []

def criarLista():
    global nome_lista
    nome_lista.append(input("Informe um nome: "))

for i in range(5):
    print(f"\n{i+1}º nome: ")
    criarLista()


indice = input("\nInforme o número do índice onde está o nome na lista: ")

try:
    indice = int(indice)
    nome = nome_lista[indice]

    print(f"O nome no índice {indice} é {nome}.")

except IndexError:
    print("Índice inválido.")

except ValueError:
    print("Você não digitou um número inteiro.")



# 7. Solicitar ao usuário que acesse uma chave de um dicionário.
# Tratar erro caso a chave não exista (Chave inválida).
print("\nAcessar chave de dicionário - ")

aluno = {
    "nome": "Batman",
    "idade": 100,
    "curso": "Engenharia de Software",
}

opcao = input("Informe a chave do dicionário (nome, idade ou curso): ").lower()

try:    
    valor = aluno[opcao]
    print(f"O(a) {opcao} do(a) aluno(a) é: {valor}.")

except KeyError:
    print("Informação não encontrada.")


# 8. Solicitar ao usuário que dois números para multiplicar.
# Continuar pedindo números até que o usuário digite só números.
print("\nMultiplicação de números - ")

while True:
    numeros_lista = []

    for i in range(2):
        numero = input(f"Digite o {i+1}º número: ")
        numeros_lista.append(numero)


    num1 = numeros_lista[0]
    num2 = numeros_lista[1]

    try:
        num1_float = float(num1)
        num2_float = float(num2)

        multiplicacao = num1_float * num2_float

        print(f"A {num1_float} multiplicado por {num2_float} é: {multiplicacao}")
        break

    except ValueError:
        print("Você deve digitar apenas números.")



# 9. Solicitar ao usuário um número inteiro para calcular o fatorial.
# Tratar erro caso não seja uma entrada válida.
print("\nFatorial - ")

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * calcular_fatorial(n - 1)

number = input("Digite um número inteiro para calcular o fatorial: ")

try:
    numero = int(number)
    
    if numero < 0:
        print("Não se calcula fatorial de números negativos.")

    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")

except ValueError:
    print("Você não digitou um número inteiro.")



# 10. Solicitar ao usuário o salário mensal e a despesa para calcular o o saldo restante.
# Tratar erro caso não seja uma entrada válida.

print("\nDespesa - ")

while True:

    try:
        salario_mensal = float(input("Informe o seu salário mensal: "))
        despesa = float(input("Informe o valor da despesa: "))
        
        saldo_restante = salario_mensal - despesa
        
        print(f"\nSeu saldo restante é: R$ {saldo_restante}")
        break 
        
    except ValueError:
        print("Você não digitou números.")


