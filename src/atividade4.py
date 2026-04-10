# ATIVIDADE 4 - ESCOPO | DEF RECURSIVA
# Estudante: Pedro Henrique

# 1 - Sistema de login
print("\n1 -Sistema de login - ")
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
# Resposta: A variável usuario_nome faz parte do escopo global porque é uma variável que pode ser acessada por todo o código, 
# porque ela está localizada fora de uma função, já se estivesse dentro de uma função, seria parte do escopo local e 
# só poderia ser utilizada dentro dessa função.


# 2 - Controle de estoque
print("\n2 -Controle de estoque - ")
estoque_produto = 50
print(f"O estoque é de: {estoque_produto}")

def vender_produto(quantidade):

    global estoque_produto
    estoque_produto -= quantidade
    print(f"Estoque atual: {estoque_produto}.")

numero_vendas = int(input("Informe a quantidade de produtos vendidos: "))
vender_produto(numero_vendas)

# Resposta: Fora da função a variável global pode ser alterada diretamente. 
# Dentro da função, é necessário usar a palavra reservada global para indicar que a variável pertence ao 
# escopo global.


# 3 - Sistema de notas
print("\n3 - Sistema de notas - ")
nota_minima = 7

def verificar_aprovacao(nota):
    if nota >= nota_minima:
        print("Aprovado(a).")
    else:
        print("Reprovado(a).")

verificar_aprovacao(float(input("Informe a nota do aluno: ")))

# Resposta: Qualquer variável declarada fora de uma função é considerada uma variável global


# 4 - Controle de acesso
print("\n4 - Controle de acesso - ")

def criar_senha():
    senha_temporaria = "321"
    return senha_temporaria

print(senha_temporaria)

# Resposta: A variável senha_temporária foi declarada dentra da função, por ser um escopo local, 
# a variável não pode ser acessada fora da função

# Funcionaria se chamar a função na qual a variável foi declarada print(criar_senha())


# 5 - Sistema de caixa
print("\n5 - Sistema de caixa - ")

caixa = 1000

def vender(quantidade):
    global caixa
    print(f"Quantidade: {caixa}")

    caixa -= quantidade
    print(f"Quantidade depois da venda: {caixa}")

vender(int(input("Informe a quantidade vendida: ")))

# Resposta: Deve ser utilizado uma variável de escopo global para a caixa, podendo ser acessada e 
# modificada em diferentes partes do código, como na função vender.
# Devemos usar a palavra reservada global e o nome da variável na funçãopara indicar que
# estamos alterarando uma variável do escopo global, porque sem usar o global dentro da função, o python
# entende que a variável está sendo declarada dentro do escopo local da função.


# 6 - Contagem de parcelas
print("\n6 - Contagem de parcelas - ")
def contar_parcelas(x):
    print(x)
    if x == 0:
        return 0
    contar_parcelas(x - 1)

contar_parcelas(int(input("Informe o número de parcelas: ")))


# 7 - Contagem de níveis de um jogo
print("\n7 - Contagem de níveis de um jogo - ")

def avancar_nivel(nivel):
    if nivel == 0:
        print(f"Nível {nivel} - Você chegou ao nível final")
    else:
        print(f"Nível {nivel}.")
        avancar_nivel(nivel - 1)

avancar_nivel(int(input("Informe o seu nível: ")))

# Resposta: O caso base da função recursiva é parar quando o nível for 0.


# 8 - Soma de Compras 
print("\n8 - Soma de Compras")

def somar_compras(quantidade_produtos):
    if quantidade_produtos == 0:
        return 0
    
    else:
        valor = float(input(f"Digite o valor de cada produto {quantidade_produtos}: "))
        
        return valor + somar_compras(quantidade_produtos - 1)

total = int(input("Informe a quantidade de produtos:  "))
resultado = somar_compras(total)

print(f"\nO valor da compra é: R$ {resultado}")

# Resposta: Usar função recursiva em tarefas repetitivas deixa o código mais simples e limpo, 
# dividindo o problema.


# 9 - Contagem de pessoas em uma fila
print("\n9 - Contagem de pessoas em uma fila - ")

def contar_fila(quantidade_pessoas):
    if quantidade_pessoas == 0 or quantidade_pessoas < 0:
        print("Fila vazia")
    else:
        print(f"Quantidade de pessoas na fila: {quantidade_pessoas}")
        contar_fila(quantidade_pessoas - 1)

contar_fila(int(input("Informe a quantidade de pessoas na fila: ")))


# 10 - Atualização de sistema
print("\n10 - Atualização de sistema - ")

def atualizar_sistema(versao):
    if versao == 10 or versao > 10:
        print(f"Versão {versao} Sistema atualizado.")
    else:
        print(f"Atualizando para a versão {versao}.")
        atualizar_sistema(versao + 1)

atualizar_sistema(int(input("Informe a versão do sistema: ")))

# Resposta: A chamada recursiva para quando a função atende ao caso base que é iterar até 10.
    

