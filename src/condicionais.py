# Estrutura Condicional
# True or false

# if (once)
# elif (many times)
# else (once)


print("Estrutura condicional")
LIMITE_VIA = 120
MINIMO_VIA = 80
velocidade = int(input("\nQual a velocidade do automóvel: "))

if velocidade > LIMITE_VIA:
    print("\nVelocidade acima do permitido.")

elif velocidade < MINIMO_VIA:
    print("\nVelocidade abaixo da via.")

else:
    print("\nContinue, velocidade permitida.")

print("\n==================================================================")


print("\nCondicional com booleano")

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
        print("Você está apto(a)!")
    
    else:
        print("Você não está apto(a).")

verificarCondicao()

# Múltiplos operadores de comparação