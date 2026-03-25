# Loop For é um laço de repetição finito. (Início, meio e fim).
# Só utilizar quando possuir os valores necessários

# print 5 números
for numero in range(5):
    print(numero)
print("\n=================================")

# print de 1 a 5
for numero in range(1, 6):
    print(numero)
print("\n=================================")

# print de 1 a 10 com intervalo de 2 números.
for numero in range(1, 10, 2):
    print(numero)
print("\n=================================") 


# Loop for com condicional.






print("\n=================================")


# Loop for com string

# Aspas simples
for letras in 'fruta':
    print(letras)

print("\n=================================")


# Aspas duplas quando for alimentar uma variável.
palavraChave = str(input("Insira uma palavra: "))
for letras in palavraChave:
    print(letras)

print("\n=================================")