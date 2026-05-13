"""
Atividade Polimorfismo

12/05/2026

Estudante: Pedro Henrique


4 pilares da POO

Instruções
Uma escola técnica deseja desenvolver um sistema para gerenciar diferentes tipos de usuários da instituição, como alunos, 
professores e coordenadores. Todos possuem informações em comum, como nome, idade e e-mail, mas cada tipo de usuário também 
apresenta comportamentos específicos dentro do sistema.

O sistema deve ser organizado utilizando os quatro pilares da Programação Orientada a Objetos em Python. A estrutura deve permitir 
o reaproveitamento de características comuns entre os usuários, proteger dados sensíveis para que não sejam alterados diretamente, 
definir comportamentos obrigatórios que todas as categorias de usuário precisam implementar e permitir que um mesmo método apresente 
respostas diferentes de acordo com o tipo de usuário.

Com base nesse contexto, desenvolva uma solução orientada a objetos que utilize encapsulamento, herança, abstração e polimorfismo, 
representando corretamente os diferentes perfis de usuários da instituição e suas responsabilidades dentro do sistema.
"""

from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nome: str, idade: int, email: str):
        self._nome = nome
        self.__idade = idade
        self.__email = email


    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, atualizar_nome):
        if not atualizar_nome.strip():
            raise ValueError("Nome não pode ser vazio.")
        
        self._nome = atualizar_nome


    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, atualizar_idade):
        if not atualizar_idade and atualizar_idade <= 0:
            raise ValueError("A idade não pode ser vazia e menor ou igual a zero.")
        
        self.__idade = atualizar_idade
    

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, atualizar_email):
        if not atualizar_email.strip():
            raise ValueError("E-mail não pode ser vazio.")
        
        self.__email = atualizar_email

    
    @abstractmethod
    def acessar_sistema(self):
        pass

    @abstractmethod
    def exibir_usuario(self):
        pass


class Aluno(Usuario):
    def acessar_sistema(self):
        print(f"Acessar conta Aluno: {self.email}")
        print(f"Bem-vindo(a) {self.nome}")

    def exibir_usuario(self):
        print("\nDados do aluno")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")

class Professor(Usuario):
    def __init__(self, nome, idade, email, disciplina: str):
        super().__init__(nome, idade, email)

        self.__disciplina = disciplina


    @property
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter
    def disciplina(self, atualizar_disciplina):
        if not atualizar_disciplina.strip():
            raise ValueError("A disciplina não pode estar vazia.")
        
        self.__disciplina = atualizar_disciplina
    

    def acessar_sistema(self):
        print(f"Acessar conta Professor: {self.email}")
        print(f"Bem-vindo(a) Professor(a) {self.nome}")


    def exibir_usuario(self):
        print("\nDados do(a) Professor(a)")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
        print(f"Disciplina: {self.disciplina}")


    def preparar_aula(self):
        print(f"Preparando aula de {self.disciplina}.")


class Coordenador(Usuario):
    def __init__(self, nome, idade, email, departamento: str):
        super().__init__(nome, idade, email)

        self._departamento = departamento


    @property
    def departamento(self):
        return self._departamento
    
    @departamento.setter
    def departamento(self, atualizar_departamento):
        if not atualizar_departamento.strip():
            raise ValueError("O departamento não pode estar vazio.")
        
        self._departamento = atualizar_departamento
        

    def acessar_sistema(self):
        print(f"Acessar conta Coordenador(a): {self.email}")
        print(f"Bem-vindo(a) Coordenador(a) {self.nome}")


    def exibir_usuario(self):
        print("\nDados do(a) Coordenador(a)")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
        print(f"Departamento: {self.departamento}")


    def coordenar_dept(self):
        print(f"Coordenar rotina do departamento de {self.departamento}.")

aluno1 = Aluno("Henrique", 100, "henrique@henrique.org")
aluno1.acessar_sistema()
aluno1.exibir_usuario()

professor1 = Professor("Henri", 90, "henrique@henrique.org", "Matemática")
professor1.acessar_sistema()
professor1.exibir_usuario()
professor1.preparar_aula()

coordenador1 = Coordenador("Henri", 90, "henrique@henrique.org", "Administrativo")
coordenador1.acessar_sistema()
coordenador1.exibir_usuario()
coordenador1.coordenar_dept()






    
