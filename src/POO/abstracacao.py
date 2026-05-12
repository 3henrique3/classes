"""
11/05/2026

Abstração:

É um dos conceitos de POO que foca em ocultar detalhes complexos de implementação expondo apenas o essencial.

- Esconder: Complexidade desnecessária para o usuário
- Mostra: Apenas o que é essencial
- Define: As estruturas obrigatórias para o sistema

o usuário utiliza o  objetos sem precisar conhecer toda a estrutura.


Ex.: Carro
Para dirigir precisamos conhecer freio, acelerar...

Não precisamos conhecer pressão interna, combustão do motor...

O carro abstrai toda a complexidade que existe nele.


Na programação fazemos isso, criando estruturas simples para representar comportamentos complexos.

abstração ajuda:

- Organizar sistemas
- Padronizar estruturas
- Obrigar imolementações
- Esconder detalhes internos
- Facilitar manutenção


Classe abstrata:
- Serve como modelo
- Não deve ser instanciada diretamente
- Define métodos obrigatórios
- Força o padrão nas subclasses

De forma simples, ela funciona como um contrato (interface).

Criando uma classe abstrata:
Para transformar uma classe em abstrata:
1. Herdar da biblioteca/módulo ABC
2. Utilizar o o @abstracmethod nos métodos obrigatórios
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Animal é uma classe abstrata. Ela representa uma estrutura genérica, todo animal pode
    emitir som, mas cada animal faz de forma diferente...

    Portando não implementa diretamente o comportamento/método, apenas define a abstração.
    """

    @abstractmethod
    def emitir_som(self):
        pass
        """
        Método abstrato, esse método não possui implementação ele funciona como uma regra obrigatória
        e toda classe filha deverá implementar esse método.
        """

    """
    @abstractmethod
    def comer(self):
        pass
    """

# animal1 = Animal() - Forma errada de chamar

class Gato(Animal):
    def emitir_som(self):
        # print ou return
        print("Meow")

    def comer(self):
        print("O gato está comendo.")
        

class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au")

class Passaro(Animal):
    def emitir_som(self):
        print("Psi Psi")


gato = Gato()
gato.emitir_som()
gato.comer()

cachorro = Cachorro()
cachorro.emitir_som()

passaro = Passaro()
passaro.emitir_som()

"""
Sistema de pagamento - Exemplo profissional

Todo pagamento precisa:
- Processar
- Validar
- Gerar comprovante

Sem esquecer que cada pagamento funciona de maneira diferente.
Por isso, utilizamos a abstração.
"""

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self):
        pass

    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def gerar_comprovante(self):
        pass


class CashPagamento(Pagamento):
    print("\nPagamento em dinheiro.")

    def processar(self, compra, cash):
        if compra <= 0:
            raise ValueError("A compra deve ser maior que zero.")
        
        if cash < compra:
            raise ValueError("Dinheiro insuficiente.")

    
        print("Pagamento processado.")

    def validar(self, compra):
        print(f"Compra no valor de R$ {compra} realizada em dinheiro ")

    def gerar_comprovante(self, compra, cash):
        troco = cash - compra

        print("\nComprovante de pagamento")
        print(f"O valor da sua compra é {compra:.f}.")
        print(f"Pagamento realizado em dinheiro R$ {cash}")
        print(f"Troco no valor de R$ {troco}")

pagamentoDinheiro = CashPagamento()
pagamentoDinheiro.processar(compra = float(input("Informe o valor da sua compra: ")),
    cash = float(input("Informe o quanto está pagando em dinheiro: ")))

pagamentoDinheiro.validar()
pagamentoDinheiro.gerar_comprovante()
