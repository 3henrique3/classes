# 29.04.2026
# Atividade de encapsulamento
# Estudante: Pedro Henrique

# 1. Explique o que é encapsulamento e qual o seu objetivo em POO

"""
Encapsulamento é um dos pilares da Programação orientada que define as regras de como uma classe e seus objetos podem ser acessados,
tem como principal objetivo controlar o acesso de classes e objetos, e quem pode acessá-los e modificá-los. 
"""

# 2. Crie classes que possui atributos públicos, protegidos e privados. 
# Descreva a diferença entre esses três tipos de atributos e quando cada um deve ser utilizado.

class Objeto:
    def __init__(self, nome: str, tipo: int, uso: str):
        self.nome = nome  # Atributo public pode ser acessado por todo o projeto

        self._tipo = tipo # Atributo protected que não impede significativamente o seu uso, é só uma sinalização de que este atributo deve ser acessado 
        # somente nessa classe e suas subclasses, somente uso interno.

        self.__uso = uso # Atributo private que só pode ser acessado através da classe em que foi criado 



# 3. Analise a seguinte situação:
# Uma classe permite que qualquer parte do sistema altere diretamente o valor de um atributo crítico.
# Explique quais problemas isso pode gerar em um sistema real.

# Resposta: Na classe Objeto há o atributo public "nome" que pode ser acessado por todo o projeto, mas isso deve ser tratado com cuidado, porque
# qualquer outra classe pode acessá-la, e modificá-la, se pensar em um projeto que demanda níveis de acessos controlados, onde o colaborador 1
# não poderia ter os mesmos acessos do colaborador 2.



# 4. Uma equipe de marketing decidiu utilizar apenas atributos públicos em todas as classes do sistema.
# Crie uma classe para cadastro de lead e avalie essa decisão e discuta se ela é adequada ou não, justificando sua resposta.

class cadastroLead:
    def __init__(self, nome: str, cargo: str, salario: float):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def cadastrar_lead(self):
        self.nome = str(input("Informe o nome: "))
        self.cargo = str(input("Informe o cargo: "))
        self.salario = float(input("Informe o salario: "))

# Algumas informações devem ser mantidas em controle privado, para evitar que sejam modificadas por outras partes do projeto (outras classes),
# porque assim garantimos a integridade dos dados, em que somente as partes autorizadas devem acessá-las, se todas as partes puderem 
# acessar esses atributos, poderia gerar um ruído de informações e alterações acidentais.



# 5. Considerando um sistema bancário onde o saldo pode ser alterado diretamente por qualquer desenvolvedor.
# Descreva os riscos dessa abordagem e como o encapsulamento poderia resolver esses problemas.

# Resposta: O risco está na liberdade dada a toda parte do projeto em que qualquer desenvolvedor do projeto pode acessar e alterar esse saldo,
# tornar esse atributo privado garante a integridade e a proteção do código, impedindo que esse atributo seja acessado diretamente fora da 
# sua classe.



# 6. Explique o papel do underscore (_) em atributos e métodos em Python. Ele realmente impede o acesso ou tem outro objetivo?

# Resposta: O uso de um único sublinhado no constructor da classe self._nome torna o atributo protected, isso significa que ele deve
# ser acessado internamente, pela mesma classe ou subclasses, mas não impede que possa ser acessado por todo o código, é somente uma sinalização.



# 7. Explique o que acontece quando utilizamos dois underscores (__) em um atributo. Qual o objetivo dessa abordagem?

# Resposta: O uso de dois sublinhados no constructor da classe self.__nome torna o atributo private, isso significa que esse atributo só pode ser
# ser acessado dentro da mesma classe, impedindo o seu acesso no resto do código que não seja através da sua classe.



# 8. Em um sistema de cadastro de usuários, é necessário garantir que a idade nunca seja negativa.
# Explique como o encapsulamento pode ser utilizado para garantir essa regra.

class Pessoa:                
    def __init__(self, nome: str, idade: int):                
        self.nome = nome
        self.__idade = idade

        if idade <= 0:
            raise ValueError("A idade deve ser maior que 0")             
                
    def mostrarPessoa(self):                
        return (f"Seu nome é {self.nome} e a sua idade é {self.__idade}")      


pessoa1 = Pessoa(
    nome = str(input("Informe o seu nome: ")),
    idade = int(input("Informe a sua idade: "))
)

print(pessoa1.mostrarPessoa())

# Resposta: A idade é um atributo privado, portanto só pode ser acessada na mesma classe em que foi criada.
# Há uma verificação para o atributo idade impedindo que haja a instância do objeto da classe Pessoa se não estiver passado por
# essa regra.



# 9. Escolha um sistema e decida quais atributos devem ser públicos e quais devem ser protegidos ou privados.
# Explique quais critérios você utilizaria para tomar essa decisão.

class Pessoa:
    def __init__(self, codigo: int, nome: str, idade: int):                
        self.codigo = codigo # public para poder utilizar e acessar o codigo em todo o projeto, para 
        self._nome = nome
        self.__idade = idade


