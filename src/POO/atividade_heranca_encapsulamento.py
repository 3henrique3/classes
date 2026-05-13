"""
Atividade Herança e Encapsulamento

Estudante: Pedro Henrique
06/07/2026
"""

"""
1. Um banco digital está expandindo seu sistema financeiro e percebeu a necessidade de reorganizar a estrutura das contas dos clientes. Atualmente, todas as contas possuem características em comum, como número da conta, titular e controle de saldo, porém cada tipo de conta possui comportamentos específicos dentro do sistema.

Além disso, a equipe identificou um problema grave: alguns desenvolvedores estavam acessando e alterando diretamente o saldo das contas, comprometendo a segurança das informações financeiras e permitindo operações inválidas.

Como desenvolvedor responsável pela nova arquitetura do sistema, crie uma solução orientada a objetos utilizando herança e encapsulamento para representar diferentes tipos de contas bancárias, garantindo reutilização de código, especialização de comportamentos e proteção adequada dos dados financeiros da aplicação. 
"""

class Conta:
    def __init__(self, numero_conta: int, titular: str):
        self._numero_conta = numero_conta
        self.__titular = titular

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def titular(self):
        return self.__titular


class Conta_poupanca(Conta):
    def __init__(self, numero_conta, titular, saldo: float):
        super().__init__(numero_conta, titular)
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, definir_saldo):
        if definir_saldo < 100:
            raise ValueError("O saldo da conta poupança deve ser maior ou igual a R$ 100,00.")
        
        self.__saldo = definir_saldo
    
    def sacar(self, saque):
        if saque <= 0 and saque > self.saldo:
            raise ValueError("O saque não pode ser maior que o seu saldo e menor que zero.")
        
        self.saldo -= saque
        print(f"Saque realizado da conta: {self.numero_conta}.")
        print(f"Saldo: {self.saldo}")

class Conta_corrente(Conta):
    def __init__(self, numero_conta, titular, saldo: float = 0):
        super().__init__(numero_conta, titular)
        
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, definir_saldo):
        if definir_saldo < 0:
            raise ValueError("O saldo da conta corrente não pode ser menor que zero.")
        
        self.__saldo = definir_saldo
    
    def depositar(self, deposito: float):
        if deposito <= 0:
            raise ValueError("O deposito não pode ser menor ou igual a zero.")
        
        self.saldo += deposito
        print(f"Deposito realizado na conta {self.numero_conta}")
        print(f"Saldo: {self.saldo}")

    def sacar(self, saque):
        if saque <= 0 and saque > self.saldo:
            raise ValueError("O saque não pode ser maior que o seu saldo e menor que zero.")
        
        self.saldo -= saque
        print(f"Saque realizado da conta: {self.numero_conta}.")
        print(f"Saldo: {self.saldo}")


conta1 = Conta_poupanca(1111, "Henrique", 10000.10)
conta1.sacar(100)

conta2 = Conta_corrente(2222, "Henri")
conta2.depositar(1999.99)
conta2.sacar(200.50)


"""
2. Uma instituição de ensino deseja modernizar seu sistema acadêmico. Atualmente, informações de alunos e professores estão sendo duplicadas em várias partes do código, 
dificultando manutenção e evolução do sistema. Pensando em reutilização de código e organização da aplicação, desenvolva uma estrutura orientada a objetos onde exista 
uma classe mais genérica representando pessoas da instituição e uma estrutura mais específica para os alunos, contendo características e comportamentos próprios do contexto acadêmico. 
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



    



    

        
