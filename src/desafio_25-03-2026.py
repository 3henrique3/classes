# Desafio 25/03/2026
# Loop

passo_a_passo = [
    "1 - Retirar o macaco do carro",
    "2 - Afrouxa os parafusos do pneu",
    "3 - Iça o carro com o macaco",
    "4 - Terminar de desparafusar",
    "5 - Retirar o pneu furado",
    "6 - Colocar o estepe no eixo",
    "7 - Parafusar o pneu",
    "8 - Abaixar o carro",
    "9 - Retirar o macaco do carro",
    "10 - Guardar o macaco",
    "11 - Guardar o pneu furado",
]

for passo in passo_a_passo:
    print(f"Troca de pneu: {passo}")
    opcao = int(input(f"Você concluiu o passo {passo}? Digite 1 para sim ou 0 para não: "))

    while opcao != 1:
        print("Você deve concluir esse passo antes de continuar.")
        opcao = int(input(f"Você concluiu o passo {passo}? Digite 1 para sim ou 0 para não: "))
