# Herança em Python

"""
Herança é um dos pilares de POO que tem como ideia principal:
- Reutilizar/reaproveitar códigos
- Criar classes mais específicas a partir de classes gerais
- Organizar melhor entidades(classes) que possuem caracterísicas em comum

Ou seja quando várias classes possuem atributos e métodos parecidos,
podemos criar uma classe principal, chamada classe Pai/ classe Base/ Superclasse.

A partir disso, podemos criar classes que herdam essas caracteríscas, serão
chamadas de classe Filha/ classe Derivada/ Subclasse.

Real world example:
- School system

Todos os usuários possuem:
- Superclasse: Usuario(nome, idade e e-mail)

Existem tipos diferentes de usuários:
- Subclasses: Aluno; Professor; Coordenador, cada um com atributos e métodos específicos.

class ClasseFilha(ClassePai):
    pass
    
"""

class Usuario:
    def __init__(self, nome, idade, email):
        self._nome = nome
        self.__idade = idade
        self._email = email

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def email(self):
        return self._email
    
    @nome.setter
    def nome(self, cadastrar_nome):
        if not cadastrar_nome:
            raise ValueError("O nome não pode estar vazio.")
        
        self._nome = cadastrar_nome

    def andar(self):
        print(f"{self._nome} está andando.")

    def apresentar(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self.__idade}")
        print(f"E-mail: {self._email}") 


class Aluno(Usuario):
    def correr():
        print("Correndo")

usuario1 = Usuario("Henrique", 100, "irnhe@google.com")
usuario1.andar()

class Professor(Usuario):
    def __init__(self, nome, idade, email, disciplina):
        super().__init__(nome, idade, email)

        self._disciplina = disciplina

    def ensinar(self):
        print(f"O(a) Professor(a) {self._nome} está dando aula de {self._disciplina}")


professor1 = Professor("Henri", 90, "irnhe@outlook.com", "DevOps")
professor1.ensinar()


class Coordenador(Usuario):
    def __init__(self, nome, idade, email, curso, matricula):
        super().__init__(nome, idade, email)

        self._curso = curso
        self._matricula = matricula
    
    def apresentarCoordenador(self):
        print(f"O(a) coordenador(a) {self._nome} de matrícula {self._matricula}, está resposável pelo curso {self._curso}.")

coord1 = Coordenador("Thallyta", 30, "thallyta@google.com", "Análise de dados", 11101)
coord1.apresentarCoordenador()