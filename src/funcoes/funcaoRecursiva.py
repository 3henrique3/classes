# Uma função recursiva chama ela mesma para resolver um problema
# Ela é usada quando um problema é divido em partes menores iguais ao problema original

# Toda função recursiva precisa de dois elementos:
# - caso base: É a condição que faz a função parar. Sem o caso base a função entra em loop infinito.

# - Chamada recursiva: É o momento em que a função chama a si mesma mas com um valor menor ou mais próximo do caso base.


print("Example 1")
def somar_ate_100(x):

    if x < 100:
        # print(x) (Atua como o back-end)
        x += 1
        return somar_ate_100(x)
    else:
        return x

numeroTeste = 98
teste_recursao = somar_ate_100(numeroTeste)
print(teste_recursao)


print("\nExample 2")
def calcular_fatorial(x):
    # print(x)
    if x == 0 or x == 1: # Caso base
        return 1
    else:
        return x * calcular_fatorial(x -1) # Chamada recursiva
    
print(calcular_fatorial(5))


print("\nExample 3")
def contar_regressiva(x):
    print(x)
    if x == 0: # Caso base
        print("Fim da contagem.")
        return
    contar_regressiva(x - 1) # Chamada recursiva
    
contar_regressiva(10)


print("\nExample 4")
def sequenciar_fibonacci(x):
  print(x)
  if x <= 1:
      return x
  else:
      return sequenciar_fibonacci(x - 1) + sequenciar_fibonacci(x - 2)
  
print(sequenciar_fibonacci(100))


