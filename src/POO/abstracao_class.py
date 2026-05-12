# By Thallyta Robertta

"""
===========================================================
ABSTRAÇÃO EM PYTHON - CONTEXTO COMPLETO (MODELO DIDÁTICO)
===========================================================

Abstração é um dos pilares da Programação Orientada a Objetos (POO).

A ideia principal da abstração é:

ESCONDER complexidades desnecessárias
MOSTRAR apenas o que é essencial
DEFINIR estruturas obrigatórias para o sistema

Ou seja:
O usuário utiliza o objeto sem precisar conhecer
toda a lógica interna do funcionamento.

-----------------------------------------------------------
EXEMPLO DO MUNDO REAL
-----------------------------------------------------------

Imagine um carro.

Para dirigir, você precisa:
- volante
- acelerador
- freio
- marcha

Mas você NÃO precisa entender:
- combustão do motor
- pressão interna
- funcionamento do pistão
- sistema elétrico completo

O carro abstrai toda a complexidade.

-----------------------------------------------------------
ABSTRAÇÃO NA PROGRAMAÇÃO
-----------------------------------------------------------

Na programação fazemos exatamente isso.

Criamos estruturas simples para representar
comportamentos complexos.

A abstração ajuda a:

- organizar sistemas
- padronizar estruturas
- obrigar implementações
- esconder detalhes internos
- facilitar manutenção

-----------------------------------------------------------
O QUE É UMA CLASSE ABSTRATA?
-----------------------------------------------------------

Uma classe abstrata é uma classe que:

- serve como modelo
- não deve ser instanciada diretamente
- define métodos obrigatórios
- força padrão nas subclasses

Ela funciona como um CONTRATO.

-----------------------------------------------------------
IMPORTANDO RECURSOS DE ABSTRAÇÃO
-----------------------------------------------------------

Em Python usamos o módulo abc.

abc significa:
Abstract Base Classes
"""

from abc import ABC, abstractmethod


"""
-----------------------------------------------------------
CRIANDO UMA CLASSE ABSTRATA
-----------------------------------------------------------

Para transformar uma classe em abstrata:

1. herdamos de ABC
2. usamos @abstractmethod nos métodos obrigatórios
"""

class Animal(ABC):

    """
    Animal é uma classe abstrata.

    Ela representa uma estrutura genérica.

    Todo animal pode emitir som,
    mas cada animal faz isso de forma diferente.

    Portanto:
    Animal NÃO implementa diretamente o comportamento.
    Apenas define a obrigação.
    """

    @abstractmethod
    def emitir_som(self):
        """
        Método abstrato.

        Esse método NÃO possui implementação aqui.

        Ele funciona como uma regra obrigatória.

        Toda classe filha deverá implementar esse método.
        """
        pass


"""
-----------------------------------------------------------
IMPORTANTE:
CLASSES ABSTRATAS NÃO PODEM SER INSTANCIADAS
-----------------------------------------------------------

Isso significa que o código abaixo gera erro:

animal = Animal()

Porque a classe abstrata serve apenas como modelo.
"""

# animal = Animal()  # ERRO


"""
-----------------------------------------------------------
CLASSE FILHA IMPLEMENTANDO O MÉTODO ABSTRATO
-----------------------------------------------------------

Agora vamos criar classes concretas.

Essas classes herdam da classe abstrata
e implementam os métodos obrigatórios.
"""

class Cachorro(Animal):

    """
    Cachorro herda de Animal.

    Como Animal possui um método abstrato,
    Cachorro é OBRIGADO a implementar emitir_som().
    """

    def emitir_som(self):
        """
        Implementação específica do cachorro.
        """
        print("O cachorro latiu: au au!")


class Gato(Animal):

    """
    Gato também herda de Animal.

    Portanto, também precisa implementar emitir_som().
    """

    def emitir_som(self):
        print("O gato miou: miau!")


"""
-----------------------------------------------------------
CRIANDO OBJETOS DAS CLASSES CONCRETAS
-----------------------------------------------------------

Agora funciona normalmente,
porque as classes filhas implementaram
os métodos obrigatórios.
"""

cachorro = Cachorro()
gato = Gato()

cachorro.emitir_som()
gato.emitir_som()


"""
-----------------------------------------------------------
O QUE A ABSTRAÇÃO ESTÁ FAZENDO AQUI?
-----------------------------------------------------------

A abstração está:

- definindo padrão
- obrigando implementação
- organizando arquitetura
- garantindo consistência

Toda classe que herdar de Animal
SERÁ obrigada a possuir emitir_som().

-----------------------------------------------------------
ERRO COMUM DOS ALUNOS
-----------------------------------------------------------

Esquecer de implementar o método abstrato.
"""

class Passaro(Animal):

    """
    Essa classe gera erro se tentarmos instanciar,
    porque NÃO implementou emitir_som().
    """
    pass


# passaro = Passaro()  # ERRO


"""
-----------------------------------------------------------
ABSTRAÇÃO NO MUNDO PROFISSIONAL
-----------------------------------------------------------

Abstração é extremamente utilizada em:

- APIs
- Frameworks
- Sistemas bancários
- Engines
- ORMs
- Microserviços
- Arquiteturas backend

Ela ajuda equipes inteiras
a seguirem o mesmo padrão.

-----------------------------------------------------------
EXEMPLO PROFISSIONAL - SISTEMA DE PAGAMENTO
-----------------------------------------------------------

Imagine um sistema financeiro.

Todo pagamento precisa:
- processar
- validar
- gerar comprovante

Mas cada forma de pagamento funciona diferente.

Então usamos abstração.
"""

class Pagamento(ABC):

    """
    Classe abstrata representando pagamentos.
    """

    @abstractmethod
    def processar_pagamento(self, valor):
        pass

    @abstractmethod
    def gerar_comprovante(self):
        pass


"""
-----------------------------------------------------------
IMPLEMENTAÇÃO CONCRETA - CARTÃO
-----------------------------------------------------------
"""

class PagamentoCartao(Pagamento):

    def processar_pagamento(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado no cartão.")

    def gerar_comprovante(self):
        print("Comprovante do cartão gerado.")


"""
-----------------------------------------------------------
IMPLEMENTAÇÃO CONCRETA - PIX
-----------------------------------------------------------
"""

class PagamentoPix(Pagamento):

    def processar_pagamento(self, valor):
        print(f"Pagamento PIX de R$ {valor:.2f} realizado.")

    def gerar_comprovante(self):
        print("Comprovante PIX gerado.")


cartao = PagamentoCartao()
pix = PagamentoPix()

cartao.processar_pagamento(500)
cartao.gerar_comprovante()

pix.processar_pagamento(250)
pix.gerar_comprovante()


"""
-----------------------------------------------------------
ABSTRAÇÃO + HERANÇA
-----------------------------------------------------------

Abstração normalmente trabalha junto com herança.

A classe abstrata funciona como classe pai.

As subclasses:
- herdam
- implementam
- especializam comportamentos

-----------------------------------------------------------
ABSTRAÇÃO + POLIMORFISMO
-----------------------------------------------------------

A abstração facilita polimorfismo.

Porque todas as subclasses seguem o mesmo padrão.
"""

pagamentos = [
    PagamentoCartao(),
    PagamentoPix()
]

for pagamento in pagamentos:
    pagamento.processar_pagamento(100)


"""
-----------------------------------------------------------
DIFERENÇA ENTRE ABSTRAÇÃO E ENCAPSULAMENTO
-----------------------------------------------------------

Muitos alunos confundem.

ABSTRAÇÃO:
esconde complexidade
define estrutura
cria contratos

ENCAPSULAMENTO:
protege dados
controla acesso
valida comportamento

-----------------------------------------------------------
EXEMPLO DIDÁTICO
-----------------------------------------------------------

Abstração:
"Todo veículo deve acelerar."

Encapsulamento:
"A velocidade não pode ser alterada livremente."

-----------------------------------------------------------
OUTRO EXEMPLO REAL
-----------------------------------------------------------

Classe abstrata:
Funcionario

Métodos obrigatórios:
- calcular_salario()
- bater_ponto()

Classes filhas:
- Desenvolvedor
- Designer
- Gerente

Cada classe implementa de forma diferente.

-----------------------------------------------------------
VANTAGENS DA ABSTRAÇÃO
-----------------------------------------------------------

- Padronização
- Organização
- Escalabilidade
- Reutilização
- Arquitetura limpa
- Facilidade de manutenção

-----------------------------------------------------------
DESVANTAGEM DO USO ERRADO
-----------------------------------------------------------

Abstração demais pode complicar o sistema.

Nem tudo precisa virar classe abstrata.

-----------------------------------------------------------
QUANDO USAR ABSTRAÇÃO?
-----------------------------------------------------------

Use abstração quando:

- existe padrão obrigatório
- várias classes compartilham comportamento
- você quer forçar implementação
- deseja organizar arquitetura
- existe relação conceitual forte

-----------------------------------------------------------
QUANDO EVITAR?
-----------------------------------------------------------

Evite abstração quando:

# existe apenas uma implementação
# não há necessidade de padronização
# a estrutura ficará mais complexa sem necessidade

-----------------------------------------------------------
ERROS COMUNS DOS ALUNOS
-----------------------------------------------------------

1. Instanciar classe abstrata

2. Esquecer de implementar método abstrato

3. Confundir abstração com encapsulamento

4. Criar abstrações sem necessidade

5. Usar abstração apenas porque "parece profissional"

-----------------------------------------------------------
RESUMO FINAL
-----------------------------------------------------------

Abstração = ESCONDER complexidade + DEFINIR padrão.

Classe abstrata:
- serve como modelo
- não gera objetos diretamente

@abstractmethod:
- cria obrigação nas subclasses

Subclasses:
- implementam os métodos obrigatórios

-----------------------------------------------------------
REGRA GERAL
-----------------------------------------------------------

Abstração não serve para esconder variável.
Serve para ORGANIZAR comportamento.

Ela define:
- o que deve existir
- como o sistema deve se comportar
- quais regras todas as subclasses devem seguir

Isso transforma código simples
em arquitetura profissional.
"""
