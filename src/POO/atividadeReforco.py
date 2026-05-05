"""
Atividade Prática em Python
Tema: Sistema Jedi de Missões Galácticas

Objetivo da atividade:
Trabalhar os conceitos de:
- Escopo
- Loop
- Condicionais
- Classes
- Orientação a Objetos com Encapsulamento

Contexto:
A Ordem Jedi precisa organizar informações sobre personagens da galáxia.
O sistema deverá permitir o cadastro de personagens, análise do lado da Força,
consulta de nível de força e alteração de dados usando encapsulamento.
"""


# =========================================================
# CLASSE PERSONAGEM
# =========================================================

class Personagem:
    """
    Classe responsável por representar um personagem do universo Star Wars.

    Nesta classe, os atributos estão privados usando dois underlines (__).
    Isso significa que eles não devem ser acessados diretamente fora da classe.

    O acesso e alteração dos dados será feito por meio de métodos getters e setters.
    """

    def __init__(self, nome, planeta, lado_forca, nivel_forca):
        """
        Método construtor.

        Ele é executado automaticamente quando um objeto da classe Personagem é criado.

        Parâmetros:
        nome: nome do personagem
        planeta: planeta de origem
        lado_forca: Jedi, Sith ou Neutro
        nivel_forca: valor entre 0 e 100
        """

        self.__nome = nome
        self.__planeta = planeta
        self.__lado_forca = "Neutro"
        self.__nivel_forca = 0

        # Usamos os setters no construtor para validar os dados recebidos.
        self.set_lado_forca(lado_forca)
        self.set_nivel_forca(nivel_forca)

    # =====================================================
    # GETTERS E SETTERS DO NOME
    # =====================================================

    def get_nome(self):
        """
        Retorna o nome do personagem.
        """
        return self.__nome

    def set_nome(self, nome):
        """
        Altera o nome do personagem.
        """
        if nome.strip() != "":
            self.__nome = nome
        else:
            print("Nome inválido. O nome não pode ser vazio.")

    # =====================================================
    # GETTERS E SETTERS DO PLANETA
    # =====================================================

    def get_planeta(self):
        """
        Retorna o planeta do personagem.
        """
        return self.__planeta

    def set_planeta(self, planeta):
        """
        Altera o planeta do personagem.
        """
        if planeta.strip() != "":
            self.__planeta = planeta
        else:
            print("Planeta inválido. O planeta não pode ser vazio.")

    # =====================================================
    # GETTERS E SETTERS DO LADO DA FORÇA
    # =====================================================

    def get_lado_forca(self):
        """
        Retorna o lado da Força do personagem.
        """
        return self.__lado_forca

    def set_lado_forca(self, lado_forca):
        """
        Altera o lado da Força do personagem.

        Apenas os valores Jedi, Sith ou Neutro são aceitos.
        Aqui usamos condicionais para validar a informação.
        """
        lado_forca = lado_forca.capitalize()

        if lado_forca == "Jedi" or lado_forca == "Sith" or lado_forca == "Neutro":
            self.__lado_forca = lado_forca
        else:
            print("Lado da Força inválido. Use apenas Jedi, Sith ou Neutro.")
            self.__lado_forca = "Neutro"

    # =====================================================
    # GETTERS E SETTERS DO NÍVEL DA FORÇA
    # =====================================================

    def get_nivel_forca(self):
        """
        Retorna o nível da Força do personagem.
        """
        return self.__nivel_forca

    def set_nivel_forca(self, nivel_forca):
        """
        Altera o nível da Força do personagem.

        O nível precisa estar entre 0 e 100.
        Aqui usamos condicionais para proteger o atributo privado.
        """
        if nivel_forca >= 0 and nivel_forca <= 100:
            self.__nivel_forca = nivel_forca
        else:
            print("Nível da Força inválido. Use um valor entre 0 e 100.")

    # =====================================================
    # MÉTODO PARA EXIBIR OS DADOS
    # =====================================================

    def exibir_dados(self):
        """
        Exibe os dados do personagem de forma organizada.
        """
        print("------------------------------------")
        print(f"Nome: {self.__nome}")
        print(f"Planeta: {self.__planeta}")
        print(f"Lado da Força: {self.__lado_forca}")
        print(f"Nível da Força: {self.__nivel_forca}")
        print("------------------------------------")


# =========================================================
# FUNÇÃO FORA DA CLASSE PARA TRABALHAR ESCOPO
# =========================================================


def contar_lados(personagens):
    """
    Função responsável por contar quantos personagens pertencem a cada lado da Força.

    Essa função reforça o conceito de escopo porque a lista personagens é recebida
    como parâmetro. Ou seja, ela não depende diretamente de uma variável global.

    Parâmetro:
    personagens: lista contendo objetos da classe Personagem
    """

    jedi = 0
    sith = 0
    neutro = 0

    for personagem in personagens:
        if personagem.get_lado_forca() == "Jedi":
            jedi += 1
        elif personagem.get_lado_forca() == "Sith":
            sith += 1
        else:
            neutro += 1

    print("\nResumo dos lados da Força:")
    print(f"Jedi: {jedi}")
    print(f"Sith: {sith}")
    print(f"Neutros: {neutro}")


# =========================================================
# FUNÇÃO PARA CADASTRAR PERSONAGENS
# =========================================================


def cadastrar_personagens():
    """
    Função responsável por cadastrar vários personagens.

    A lista personagens é criada dentro desta função.
    Isso também ajuda a trabalhar o conceito de escopo local.
    """

    personagens = []

    while True:
        print("\nCadastro de personagem da galáxia")

        nome = input("Digite o nome do personagem: ")
        planeta = input("Digite o planeta de origem: ")
        lado_forca = input("Digite o lado da Força (Jedi, Sith ou Neutro): ")

        try:
            nivel_forca = int(input("Digite o nível da Força de 0 a 100: "))
        except ValueError:
            print("Valor inválido. O nível da Força será definido como 0.")
            nivel_forca = 0

        personagem = Personagem(nome, planeta, lado_forca, nivel_forca)
        personagens.append(personagem)

        continuar = input("Deseja cadastrar outro personagem? (s/n): ").lower()

        if continuar != "s":
            break

    return personagens


# =========================================================
# FUNÇÃO DE MENU PRINCIPAL
# =========================================================


def menu(personagens):
    """
    Função responsável por exibir o menu principal do sistema.

    O menu usa loop para continuar executando até o usuário escolher sair.
    Também utiliza condicionais para verificar qual opção foi escolhida.
    """

    while True:
        print("\n========== MENU GALÁCTICO ==========")
        print("1 - Exibir todos os personagens")
        print("2 - Exibir apenas Jedi")
        print("3 - Exibir apenas Sith")
        print("4 - Exibir personagens com nível da Força acima de 80")
        print("5 - Alterar nível da Força de um personagem")
        print("6 - Contar lados da Força")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nTodos os personagens cadastrados:")
            for personagem in personagens:
                personagem.exibir_dados()

        elif opcao == "2":
            print("\nPersonagens Jedi:")
            encontrou = False

            for personagem in personagens:
                if personagem.get_lado_forca() == "Jedi":
                    personagem.exibir_dados()
                    encontrou = True

            if encontrou == False:
                print("Nenhum Jedi encontrado.")

        elif opcao == "3":
            print("\nPersonagens Sith:")
            encontrou = False

            for personagem in personagens:
                if personagem.get_lado_forca() == "Sith":
                    personagem.exibir_dados()
                    encontrou = True

            if encontrou == False:
                print("Nenhum Sith encontrado.")

        elif opcao == "4":
            print("\nPersonagens com nível da Força acima de 80:")
            encontrou = False

            for personagem in personagens:
                if personagem.get_nivel_forca() > 80:
                    personagem.exibir_dados()
                    encontrou = True

            if encontrou == False:
                print("Nenhum personagem com nível da Força acima de 80.")

        elif opcao == "5":
            nome_busca = input("Digite o nome do personagem que deseja alterar: ")
            encontrou = False

            for personagem in personagens:
                if personagem.get_nome().lower() == nome_busca.lower():
                    try:
                        novo_nivel = int(input("Digite o novo nível da Força de 0 a 100: "))
                        personagem.set_nivel_forca(novo_nivel)
                        print("Nível da Força atualizado com sucesso.")
                    except ValueError:
                        print("Valor inválido. Digite apenas números.")

                    encontrou = True
                    break

            if encontrou == False:
                print("Personagem não encontrado.")

        elif opcao == "6":
            contar_lados(personagens)

        elif opcao == "7":
            print("Sistema encerrado. Que a Força esteja com você!")
            break

        else:
            print("Opção inválida. Escolha uma opção do menu.")


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

"""
Este bloco representa o início da execução do programa.

Primeiro, os personagens são cadastrados.
Depois, a lista de personagens é enviada para o menu.
"""

print("====================================")
print(" SISTEMA JEDI DE MISSÕES GALÁCTICAS ")
print("====================================")

lista_personagens = cadastrar_personagens()
menu(lista_personagens)
