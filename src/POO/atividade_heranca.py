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

"""
Estudante: Pedro Henrique

05/05/2026
Atividade Herança
"""

# 1; 2; 3; 4; 5; 6; 7; 8; 9:
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
    
    @idade.setter
    def idade(self, cadastro_idade):
        if not cadastro_idade:
            raise ValueError("Idade inválida.")
        
        if cadastro_idade <= 0:
            raise ValueError("A idade não pode ser menor ou igual a zero.")
        
        self.__idade = cadastro_idade

    @salario.setter
    def salario(self, cadastro_salario):
        if not cadastro_salario:
            raise ValueError("Salário inválido.")
        
        if cadastro_salario <= 0:
            raise ValueError("O salário deve ser maior que zero.")
        
        self.__salario = cadastro_salario


class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)

        self._departamento = departamento

    @property
    def departamento(self):
        return self._departamento

    def liderar_equipe(self):
        print(f"\nO(a) gerente está liderando o departamento {self._departamento}")
    


gerente1 = Gerente(
    "Henrique",
    100,
    1000,
    "Faturamento"
)

gerente1.apresentar()
gerente1.liderar_equipe()


class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, salario, linguagem_programacao):
        super().__init__(nome, idade, salario)
        
        self._linguagem_programacao = linguagem_programacao
    
    @property
    def linguagem_programacao(self):
        return self._linguagem_programacao
    
    def mostrar_tecnologia(self):
        print(f"\nO(a) desenvolvedor(a): {self.nome} de idade {self.idade}, tem salário {self.salario} e experiência: {self.linguagem_programacao}.")


# 10.
# Resposta: Uma das principais vantanges de utilizar a Herança no código, é poder reaproveitar os atributos e métodos de outra
# classe e evitar redundância de código, tornando o código mais limpo.


# 11.
gerente2 = Gerente("Henrique", 1000, 4.500, "Comercial")
gerente2.apresentar()
gerente2.liderar_equipe()


desenvolvedor1 = Desenvolvedor("Henri", 20, 4000, "TypeScript")
desenvolvedor1.mostrar_tecnologia()

desenvolvedor2 = Desenvolvedor("Pedro", 30, 4000, "Java")
desenvolvedor2.mostrar_tecnologia()


# 12.
# Resposta: O super().__init__ permite criar a classe filha com os atributos e métodos da classe pai, além de poder sobrescrever esses atributos e métodos
# e criar novos atributos e métodos na classe filha.


class Estagiario(Funcionario):
    def __init__(self, nome, idade, salario, faculdade, curso):
        super().__init__(nome, idade, salario)

        self._faculdade = faculdade
        self._curso = curso

    @property
    def faculdade(self):
        return self._faculdade
        
    @property
    def curso(self):
        return self._curso

    def estudar(self):
        print(f"\nO(a) estagiário(a) estuda {self._curso} na instituição {self._faculdade}.")

estagiario1 = Estagiario("Henrique", 111, 1000.40, "UFPE", "Análise e Desenvolvimento de sistemas")
estagiario1.estudar()
    
    
