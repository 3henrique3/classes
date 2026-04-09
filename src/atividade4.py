# ATIVIDADE - ESCOPO | DEF RECURSIVA

# 1 - Sistema de login
print("\Sistema de login - ")
usuario_nome = "tomate_quente"

def logar():
    usuario = str(input("Informe o seu usuário: "))

    while usuario != usuario_nome:
        print(f"Nome de usuário incorreto, tente novamente.")
        return logar()
    
    if usuario == usuario_nome:
        print(f"{usuario_nome} logado.")
        return

logar()
# Resposta: A variável usuario_nome é um escopo global porque é uma variável que pode ser acessada por todo o código, 
# porque ela está localizada fora de uma função, já se estivesse dentro de uma função, seria possível utilizá-la somente dentro dessa função.


# 2 - Controle de estoque
print("\nControle de estoque - ")
estoque_produto = 50
print(f"O estoque é de: {estoque_produto}")

def vender_produto(quantidade):

    global estoque_produto
    estoque_produto -= quantidade
    print(f"Estoque atual: {estoque_produto}.")

numero_vendas = int(input("Informe a quantidade de produtos vendidos: "))
venda = vender_produto(numero_vendas)
print(venda)

# Resposta: 
    


    

