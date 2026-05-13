"""
Estudante: Pedro Henrique

13/05/2026

OBJETIVO DO PROJETO 

Cada equipe deverá desenvolver um sistema de delivery em Python que permita simular o funcionamento básico de uma plataforma de pedidos.

O sistema deverá permitir:
• cadastrar informações;
• visualizar menus;
• realizar pedidos;
• calcular valores;
• organizar dados utilizando classes e objetos. 


FUNCIONALIDADES MÍNIMAS 

Cadastro de produtos
Exemplo:
• nome;
• preço;
• categoria.

Cadastro de usuários
Exemplo:
• cliente;
• entregador.

Realização de pedidos
O cliente deverá conseguir:
• visualizar produtos;
• escolher itens;
• calcular valor total;
• finalizar pedido.

Controle do pedido
O sistema deverá informar:
• pedido recebido;
• em preparação;
• saiu para entrega;
• entregue.


DIFERENCIAIS 

As equipes que quiserem podem adicionar:
• login;
• sistema de desconto;
• histórico de pedidos;
• cardápio mais organizado;
• relatórios;
• sistema de avaliação;
• salvamento em arquivo. 
"""

from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, atualizar_nome):
        if not atualizar_nome.strip():
            raise ValueError("O nome não pode estar vazio.")
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, atualizar_email):
        if not atualizar_email.strip():
            raise ValueError("O e-mail não pode estar vazio.")
        
    @abstractmethod
    def acessar_sistema(self):
        pass


class Cliente(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def acessar_sistema(self):
        print(f"Acesso do cliente: ")
        print(f"Bem-vindo {self.nome}")
        print(f"E-mail: {self.email}")


class Entregador(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)

    def acessar_sistema(self):
        print(f"Acesso do entregador: ")
        print(f"Bem-vindo {self.nome}")
        print(f"E-mail: {self.email}")


class Produto():
    def __init__(self, nome_produto: str, preco: float, categoria: str):
        self.__nome_produto = nome_produto
        self.__preco = preco
        self.__categoria = categoria


    @property
    def nome_produto(self):
        return self.__nome_produto
    
    @nome_produto.setter
    def nome_produto(self, atualizar_nome):
        if atualizar_nome.strip() != "":
            self.__nome = atualizar_nome

        else:
            raise ValueError("O nome do produto não pode estar vazio.")
    

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, atualizar_preco):
        if atualizar_preco <= 0:
            raise ValueError("O preço do produto não pode ser igual ou menor que 0.")
        
        else:
            self.__preco = atualizar_preco

    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, atualizar_categoria):
        if atualizar_categoria.strip() != "":
            self.__categoria = atualizar_categoria

        else:
            raise ValueError("A categoria do produto não pode estar vazio.")


def cadastrar_usuario():

    usuarios = []

    while True: 
        print("\nCadastro de usuários: ")

        perfil = str(input("\nInforme o tipo de perfil do usuário, Somente Cliente ou Entregador: "))
        perfil = perfil.capitalize()

        if perfil == "Cliente":
            nome_cliente = str(input("Informe o nome do cliente: "))
            email_cliente = str(input("Informe o e-mail do cliente: "))

            cliente = Cliente(nome_cliente, email_cliente)
            usuarios.append(cliente)
        
        elif perfil == "Entregador":
            nome_entregador = str(input("Informe o nome do entregador: "))
            email_entregador = str(input("Informe o e-mail do entregador: "))

            entregador = Entregador(nome_entregador, email_entregador)
            usuarios.append(entregador)

        continuar = str(input("Deseja cadastrar mais um usuário, use s para sim ou n para não? ")).lower()

        if continuar != "s":
            break

    return usuarios


def menu_delivery(usuarios):
    print("\nMenu Delivery")

cadastrar_usuario()

lista_usuario = cadastrar_usuario()


    
