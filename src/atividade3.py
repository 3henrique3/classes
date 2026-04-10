# Exercício de Fixação - Lógica de Programação em Python
# 07.04.2026
# Estudante: Pedro Henrique

# 1.
usuario = {}

def cadastrar_usuario(nome, idade, cidade):
    usuario['nome'] = nome
    usuario['idade'] = idade
    usuario['cidade'] = cidade

    print(f"Cadastrado: Nome: {usuario['nome']}; Idade: {usuario['idade']}; Cidade: {usuario['cidade']}")

nome = input("Digite o nome do usuário: ")
idade = int(input("Digite a idade do usuário: "))
cidade = input("Digite a cidade do usuário: ")

cadastrar_usuario(nome, idade, cidade)


# 2.
numeros = []

for i in range(5):
    number = int(input(f"Digite o {i+1}º número: "))
    numeros.append(number)

print(f"Lista de números: {numeros}")
print(f"Maior número:    {max(numeros)}")
print(f"Menor número:    {min(numeros)}")



# 3.
aluno = {}

def visualizar_aluno(nome, curso, periodo, media_final):
    aluno['nome'] = nome
    aluno['curso'] = curso
    aluno['periodo'] = periodo
    aluno['media_final'] = media_final

    print(f"Aluno: Nome: {aluno['nome']}; Curso: {aluno['curso']}; Período: {aluno['periodo']}; Média Final: {aluno['media_final']}")

nome = input("Informe o nome do(a) aluno(a): ")
curso = input("Informe o curso do(a) aluno(a): ")
periodo = input("Informe o período do(a) aluno(a): ")
media_final = float(input("Informe a média final do(a) aluno(a): "))

visualizar_aluno(nome, curso, periodo, media_final)


# 4.
nota_minima = 7
reprovado = 5

def verificar_aprovacao(nota):
    if nota >= nota_minima:
        return "Aprovado"
    
    elif nota < nota_minima and nota > reprovado:
        return "Recuperação"
    
    else:
        return "Reprovado"
    
print(verificar_aprovacao(int(input("Informe a nota: "))))


# 5.
def saudar(nome):
    return f"Hello, {nome}!"

print(saudar(str(input("Digite seu nome: "))))


# 6.
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

print(calcular_media([int(input(f"Digite a {i+1}ª nota: ")) for i in range(int(input("Digite a quantidade de notas: ")))]))


# 7.
def verificar_pares_impares(numero):
    for number in range(1, numero + 1):
        if number % 2 == 0:
            print(f"{number} - é par.")
        else:
            print(f"{number} - é ímpar.")

verificar_pares_impares(int(input("Digite um número: ")))


# 8.
soma = 0

while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    
    if num == 0:
        break
    else:
        soma += num

print(f"\nA soma dos números digitados é: {soma}")


# 9.
nomes = []

for i in range(3):
    nomes.append(input(f"Digite o {i+1} nome: "))

print(f"\nOlá, {nomes[0]}.")
print(f"Bonjour, {nomes[1]}.")
print(f"Hello, {nomes[2]}.")


# 10.
estoque = []

for i in range(int(input("Informe a quantidade de produtos para cadastrar: "))):
    nome = input(f"Informe o nome do {i+1}º produto: ")
    preco = float(input(f"Preço de {nome}: R$ "))
    quantidade = int(input(f"Quantidade: "))
    
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    estoque.append(produto)

print("Produtos cadastrados:")
for item in estoque:
    print(f"Produto: {item['nome']} | Preço: R$ {item['preco']} | Quantidade: {item['quantidade']}")

print("\nProdutos com estoque menor de 5 unidades:")

for item in estoque:
    if item['quantidade'] < 5:
        print(f"{item['nome']}: tem apenas {item['quantidade']} unidades.")




