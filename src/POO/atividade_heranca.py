"""
Herança

Tema: Sistema de Funcionários de uma Empresa 

Você foi contratado para desenvolver parte de um sistema de gerenciamento de funcionários de uma empresa. O objetivo é utilizar corretamente os conceitos de herança para reaproveitar código e organizar melhor as entidades do sistema. 

QUESTÃO 1
Crie uma classe chamada Funcionario contendo os atributos: nome, idade e salário. 

QUESTÃO 2
Implemente um método chamado apresentar() na classe Funcionario que exiba os dados básicos do funcionário. 

QUESTÃO 3
Crie uma classe chamada Gerente que herde da classe Funcionario. 

QUESTÃO 4
Crie um objeto da classe Gerente e demonstre que ele consegue acessar os atributos e métodos herdados da classe Funcionario. 

QUESTÃO 5
Adicione à classe Gerente um método específico chamado liderar_equipe() que exiba uma mensagem informando que o gerente está liderando sua equipe. 

QUESTÃO 6
Crie uma classe chamada Desenvolvedor que herde da classe Funcionario. 

QUESTÃO 7
Adicione à classe Desenvolvedor um método chamado programar() que exiba uma mensagem informando que o desenvolvedor está programando. 

QUESTÃO 8
Modifique a classe Desenvolvedor para que ela possua também o atributo linguagem_programacao. Utilize o método super() para reaproveitar o construtor da classe pai. 

QUESTÃO 9
Crie um método na classe Desenvolvedor chamado mostrar_tecnologia() que exiba: nome do desenvolvedor, idade, salário e linguagem de programação utilizada. 

QUESTÃO 10
Explique, através de comentários no código, qual a vantagem de utilizar herança em vez de repetir os mesmos atributos e métodos em várias classes. 

QUESTÃO 11
Crie pelo menos: 1 objeto da classe Gerente e 2 objetos da classe Desenvolvedor. Teste todos os métodos criados. 

QUESTÃO 12
Demonstre, através de comentários no código, o papel do super() dentro da herança e explique por que ele evita repetição de código. 

DESAFIO EXTRA (INTERMEDIÁRIO)
Crie uma classe chamada Estagiario que herde de Funcionario e possua: atributo faculdade e método estudar(). Depois, teste o funcionamento completo da classe. 
"""

"""
Estudante: Pedro Henrique

05/05/2026
Atividade Herança
"""

# 1; 2
class Funcionario:
    def __init__(self, nome: str, idade: int, salario: float):
        self._nome = nome
        self.__idade = idade
        self.__salario = salario

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def salario(self):
        return self.__salario
    
    def apresentar(self):
        print(f"\nFuncionário(a): {self.nome}")
        print(f"Idade: {self.__idade}")
        print(f"Salário: {self.__salario}")

    
    @nome.setter
    def nome(self, cadastro_nome):
        if not cadastro_nome:
            raise ValueError("O nome não pode estar vazio.")
        
        self._nome = cadastro_nome

        
    
