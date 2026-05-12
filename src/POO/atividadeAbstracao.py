"""
Estudante: Pedro Henrique

Atividade ABSTRAÇÃO

Instruções
QUESTÃO 1 

Uma empresa de streaming possui diferentes tipos de mídia em sua plataforma, como filmes, séries e documentários. Apesar de cada categoria possuir características específicas, todas precisam seguir comportamentos básicos dentro do sistema, como reproduzir conteúdo, pausar e exibir informações ao usuário.

Explique como o conceito de abstração poderia ajudar a organizar a estrutura desse sistema e padronizar o funcionamento das diferentes mídias. 

 

QUESTÃO 2 

Em um hospital, diferentes profissionais utilizam um sistema interno para registrar informações dos pacientes. Médicos, enfermeiros e recepcionistas possuem funções diferentes, mas todos precisam acessar determinadas funcionalidades obrigatórias do sistema.

Com base nesse cenário, explique como a abstração pode ser utilizada para criar uma estrutura organizada e padronizada para os diferentes tipos de usuários da aplicação. 

 

QUESTÃO 3 

Uma empresa de delivery trabalha com diferentes formas de entrega, como moto, bicicleta e carro. Cada modalidade realiza a entrega de maneira diferente, porém todas precisam seguir etapas obrigatórias do processo, como iniciar rota, entregar pedido e finalizar entrega.

Explique como a abstração poderia ser aplicada nesse sistema para garantir organização e reutilização de estrutura entre os diferentes tipos de entrega. 

 

QUESTÃO 4 

Uma plataforma de ensino online possui diferentes tipos de conteúdos educacionais, como vídeo-aulas, quizzes e materiais em PDF. Apesar das diferenças entre os formatos, todos precisam seguir algumas regras comuns da plataforma, como liberar acesso, registrar progresso e validar conclusão.

Explique como o conceito de abstração pode contribuir para a construção desse sistema. 

 

QUESTÃO 5 

Uma empresa de automação residencial desenvolve um sistema capaz de controlar diferentes dispositivos inteligentes, como lâmpadas, câmeras e ar-condicionado. Embora cada dispositivo possua comportamentos específicos, todos precisam se conectar ao sistema e responder a comandos básicos.

Com base nesse contexto, explique como a abstração poderia ser utilizada para representar esses dispositivos dentro da aplicação. 
"""

"""
1. Resposta: A abstração pode ser implementada nesse caso para que as classes filmes, séries e documentários sigam o padrão do streamimg que
é implementar os métodos definidos na classe pai, reproduzir conteúdo, pausar e exibir informações ao usuário.
"""
from abc import ABC, abstractmethod

class Streaming(ABC):
    @abstractmethod
    def reproduzir_conteudo(self):
        pass

    @abstractmethod
    def pausar(self):
        pass

    @abstractmethod
    def exibir_informacao(self):
        pass

class Filme(Streaming):
    def reproduzir_conteudo(self):
        print("Reproduzindo filme.")

    def pausar(self):
        print("Filme pausado.")

    def exibir_informacao(self):
        print("Exibindo informação do filme")

class Serie(Streaming):
    def reproduzir_conteudo(self):
        print("Reproduzindo episódio da série.")

    def pausar(self):
        print("Episódio da série pausado.")

    def exibir_informacao(self):
        print("Exibindo informação da série.")

class Documentario(Streaming):
    def reproduzir_conteudo(self):
        print("Reproduzindo documentário.")

    def pausar(self):
        print("Documentário pausado.")

    def exibir_informacao(self):
        print("Exibindo informação do documentário.")



"""
2. Resposta: A organização será a partir de uma classe pai que definirá acessos gerais, enquanto as subclasses criadas a partir dessa classe pai terão os mesmos acessos gerais,
porém cada uma com suas especificidades.
"""
class Funcionario(ABC):
    @abstractmethod
    def registrar_informacao_paciente(self):
        pass

class Medico(Funcionario):
    def registrar_informacao_paciente(self):
        print("Acesso Médico")

class Enfermaria(Funcionario):
    def registrar_informacao_paciente(self):
        print("Acesso Enfermaria")

class Recepcao(Funcionario):
    def registrar_informacao_paciente(self):
        print("Acesso Recepção")

"""
3. Resposta: A organização pode ser através de uma classe abstrata Transporte com o método abstrato entrega, as classes filhas da super classe Transporte herdariam o
método entrega, e a partir de cada subclasse seria definido formas diferentes de definir o método entrega.
"""
class Transporte(ABC):
    @abstractmethod
    def entrega(self):
        pass

class Moto(Transporte):
    def entrega(self):
        print("Moto iniciando rota")
        print("Entrega")



"""
4. Resposta: A abstração nesse caso se daria a partir da definição de uma classe abstrata ConteudoEducacional com os métodos abstratos video_aulas, quizzes e materialPDF
cada subclasse criada a partir da classe Conteudo
"""
