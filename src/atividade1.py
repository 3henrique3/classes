""" Atividade 1 
Tema: Variáveis, Listas e Dicionários
"""

#1 Cadastro de alunos
def cadastrar():
    print("Cadastro de alunos")
    nome = str(input("\nInsira o nome do aluno matriculado: "))
    idade= int(input("Insira a idade do aluno: "))
    curso = str(input("Informe o curso que o aluno está matriculado: "))

    print("\nCadastro concluído.")
    print(f"Aluno: {nome} - Idade: {idade} - Curso: {curso}.")

cadastrar()

#2 Soma de valores
def somar():
    print("Calculadora - ")
    print("\nSoma: ")

    x = float(input("\nInforme um número para X: "))
    y = float(input("Informe um número para Y: "))
    z = x + y

    print(f"A soma de X + Y é: {z}")

somar()

#4 Atualizando lista
def listarCores():

    print("\nLista de Cores")
    cores = []
    
    cores.append(str(input("\nInsira a uma cor: ")))
    cores.append(str(input("\nInsira a segunda cor: ")))
    cores.append(str(input("\nInsira a terceira cor: ")))
    cores.append(str(input("\nInsira a quarta cor: ")))

    print(cores)

    print("\nAgora altera a segunda cor")
    cores[1] = str(input("\nAgora altera a segunda cor: "))

    print(cores)

listarCores()

#5 Lista de frutas
def verNotas():
    print("\nNotas do(a) aluno(a)")
    notas_aluno = []
    notas_aluno.append(int(input("\nInsira a primeira nota do(a) aluno(a): ")))
    notas_aluno.append(int(input("Insira a segunda nota do(a) aluno(a): ")))
    notas_aluno.append(int(input("Insira a terceira nota do(a) aluno(a): ")))

    quant_notas = len(notas_aluno)

    print(f"O(a) aluno tem: {quant_notas} notas inseridas no sistema.")

verNotas()


#6 Dicionário_Pessoa
def definirPessoa():
    
    print("\nDicionário_pessoa")

    pessoa1 = {
        "nome" : "Henrique",
        "idade" : 100,
        "city" : "Caruaru"
    }

    nomePessoa = pessoa1.get("nome")
    print(nomePessoa)

definirPessoa()

#7 Dicionário_Produto
def definirProduto():
    print("\nDicionário_produto")

    produto = {
        "nome" : "sabão",
        "preço" : 2.80,
        "quantidade" : 4
    }

    print(produto)

definirProduto()

#8 Dicionário_Aluno
def definirAluno():
    print("\nDicionário_aluno")

    aluno = {
        "nome" : "Henrique",
        "idade" : 100,
        "curso": ["Design Thinking", "Lógica de Programação", "Análise de Dados"]
    }

    print(aluno["nome"])
    print(aluno["curso"])

definirAluno()

#9 Manipulação de lista
def manipularLista():
    print("\nManipular_lista")

    numerosInt = [1, 2, 3]
    print(numerosInt)

    numerosInt.append(int(input("Insira mais um número inteirao na lista: ")))

    print(numerosInt)

manipularLista()

#10 Dicionário de Contatos
def adicionarEmail():
    print("\nAdicionar E-mail") 
    pessoa1 = {
        "nome" : "Henrique",
        "contato" : "8199999-9999"
    }

    print(pessoa1)

    pessoa1["email"] = str(input("Insira um e-mail para esse contato: "))

    print(pessoa1)

adicionarEmail()