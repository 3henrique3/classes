# By Thallyta Robertta

"""
===========================================================
POLIMORFISMO EM PYTHON - CONTEXTO COMPLETO
===========================================================

Polimorfismo é um dos pilares da Programação Orientada a Objetos (POO).

A palavra polimorfismo vem da ideia de:

POLI = muitas
MORFISMO = formas

Ou seja:
Polimorfismo significa "muitas formas".

Na programação, isso quer dizer que objetos diferentes
podem responder ao mesmo método de formas diferentes.

-----------------------------------------------------------
EXEMPLO DO MUNDO REAL
-----------------------------------------------------------

Imagine o comando:

emitir_som()

Esse mesmo comando pode ser usado para vários animais.

Mas cada animal responde de uma forma:

Cachorro - late
Gato - mia
Pássaro - canta

O comando é o mesmo.
O comportamento muda de acordo com o objeto.

Isso é polimorfismo.

-----------------------------------------------------------
POLIMORFISMO NA PROGRAMAÇÃO
-----------------------------------------------------------

Na programação, o polimorfismo permite que diferentes classes
tenham métodos com o mesmo nome, mas com comportamentos diferentes.

Isso deixa o sistema mais flexível, organizado e escalável.

-----------------------------------------------------------
EXEMPLO 1 - POLIMORFISMO COM MÉTODOS DE MESMO NOME
-----------------------------------------------------------
"""

class Cachorro:
    def emitir_som(self):
        print("O cachorro latiu: au au!")


class Gato:
    def emitir_som(self):
        print("O gato miou: miau!")


class Passaro:
    def emitir_som(self):
        print("O pássaro cantou: piu piu!")


cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

cachorro.emitir_som()
gato.emitir_som()
passaro.emitir_som()


"""
-----------------------------------------------------------
O QUE ACONTECEU AQUI?
-----------------------------------------------------------

Todos os objetos possuem o método emitir_som().

Mas cada classe implementa esse método de uma forma diferente.

O nome do método é o mesmo.
A resposta é diferente.

Isso é polimorfismo.

-----------------------------------------------------------
EXEMPLO 2 - POLIMORFISMO COM LISTA DE OBJETOS
-----------------------------------------------------------

Podemos colocar objetos diferentes dentro de uma lista
e chamar o mesmo método para todos.

O Python identifica automaticamente qual comportamento executar.
"""

animais = [cachorro, gato, passaro]

for animal in animais:
    animal.emitir_som()


"""
-----------------------------------------------------------
POR QUE ISSO É IMPORTANTE?
-----------------------------------------------------------

Sem polimorfismo, precisaríamos fazer várias verificações:

se for cachorro, faça isso
se for gato, faça aquilo
se for pássaro, faça outra coisa

Com polimorfismo, chamamos o mesmo método
e cada objeto sabe o que fazer.

-----------------------------------------------------------
EXEMPLO 3 - SEM POLIMORFISMO
-----------------------------------------------------------

Esse modelo funciona, mas é menos organizado.
"""

def emitir_som_sem_polimorfismo(animal):
    if animal == "cachorro":
        print("Au au!")
    elif animal == "gato":
        print("Miau!")
    elif animal == "passaro":
        print("Piu piu!")
    else:
        print("Animal desconhecido.")


emitir_som_sem_polimorfismo("cachorro")


"""
-----------------------------------------------------------
EXEMPLO 4 - COM POLIMORFISMO
-----------------------------------------------------------

Agora a responsabilidade fica dentro da classe.
"""

def fazer_animal_emitir_som(animal):
    animal.emitir_som()


fazer_animal_emitir_som(cachorro)
fazer_animal_emitir_som(gato)
fazer_animal_emitir_som(passaro)


"""
-----------------------------------------------------------
POLIMORFISMO COM HERANÇA
-----------------------------------------------------------

O polimorfismo normalmente aparece junto com herança.

A classe pai define um comportamento geral.
As classes filhas implementam esse comportamento
de formas diferentes.
"""

class Animal:
    def emitir_som(self):
        print("O animal emitiu um som.")


class CachorroHeranca(Animal):
    def emitir_som(self):
        print("O cachorro latiu usando herança.")


class GatoHeranca(Animal):
    def emitir_som(self):
        print("O gato miou usando herança.")


animal1 = CachorroHeranca()
animal2 = GatoHeranca()

lista_animais = [animal1, animal2]

for animal in lista_animais:
    animal.emitir_som()


"""
-----------------------------------------------------------
POLIMORFISMO COM SOBRESCRITA DE MÉTODOS
-----------------------------------------------------------

Sobrescrita ocorre quando uma classe filha cria um método
com o mesmo nome do método existente na classe pai.

O método da classe filha substitui o comportamento da classe pai.

Isso permite polimorfismo.
"""

class Funcionario:
    def calcular_pagamento(self):
        print("Calculando pagamento genérico.")


class Desenvolvedor(Funcionario):
    def calcular_pagamento(self):
        print("Pagamento do desenvolvedor calculado com bônus técnico.")


class Gerente(Funcionario):
    def calcular_pagamento(self):
        print("Pagamento do gerente calculado com bônus de liderança.")


class Estagiario(Funcionario):
    def calcular_pagamento(self):
        print("Pagamento do estagiário calculado com bolsa fixa.")


funcionarios = [
    Desenvolvedor(),
    Gerente(),
    Estagiario()
]

for funcionario in funcionarios:
    funcionario.calcular_pagamento()


"""
-----------------------------------------------------------
POLIMORFISMO COM ABSTRAÇÃO
-----------------------------------------------------------

A abstração ajuda muito o polimorfismo.

A classe abstrata define o método obrigatório.
As classes filhas implementam esse método
de acordo com sua própria regra.
"""

from abc import ABC, abstractmethod


class FormaPagamento(ABC):

    @abstractmethod
    def pagar(self, valor):
        pass


class PagamentoPix(FormaPagamento):
    def pagar(self, valor):
        print(f"Pagamento PIX realizado no valor de R$ {valor:.2f}")


class PagamentoCartao(FormaPagamento):
    def pagar(self, valor):
        print(f"Pagamento no cartão realizado no valor de R$ {valor:.2f}")


class PagamentoBoleto(FormaPagamento):
    def pagar(self, valor):
        print(f"Boleto gerado no valor de R$ {valor:.2f}")


pagamentos = [
    PagamentoPix(),
    PagamentoCartao(),
    PagamentoBoleto()
]

for pagamento in pagamentos:
    pagamento.pagar(150)


"""
-----------------------------------------------------------
O QUE ESSE EXEMPLO MOSTRA?
-----------------------------------------------------------

Todos os pagamentos usam o método pagar().

Mas cada classe executa o pagamento de uma forma diferente.

PIX:
confirma pagamento instantâneo.

Cartão:
processa pagamento no cartão.

Boleto:
gera boleto para pagamento.

O comando é o mesmo:
pagar()

Mas o comportamento muda.

Isso é polimorfismo aplicado a um caso real.

-----------------------------------------------------------
POLIMORFISMO COM FUNÇÕES
-----------------------------------------------------------

Uma função pode receber objetos diferentes,
desde que eles possuam o método esperado.
"""

def processar_pagamento(forma_pagamento, valor):
    forma_pagamento.pagar(valor)


processar_pagamento(PagamentoPix(), 100)
processar_pagamento(PagamentoCartao(), 200)
processar_pagamento(PagamentoBoleto(), 300)


"""
-----------------------------------------------------------
DUCK TYPING EM PYTHON
-----------------------------------------------------------

Python trabalha muito com uma ideia chamada Duck Typing.

A frase comum é:

"Se anda como pato e faz som de pato, então pode ser tratado como pato."

Na prática:
Python não se preocupa tanto com o tipo exato do objeto.
Ele se preocupa se o objeto possui o método necessário.

Exemplo:
Se um objeto tem o método pagar(),
ele pode ser usado na função processar_pagamento().
"""

class PagamentoCripto:
    def pagar(self, valor):
        print(f"Pagamento com criptomoeda no valor de R$ {valor:.2f}")


processar_pagamento(PagamentoCripto(), 500)


"""
-----------------------------------------------------------
POLIMORFISMO EM SISTEMAS REAIS
-----------------------------------------------------------

Esse conceito aparece em muitos cenários:

sistemas de pagamento
sistemas de notificações
sistemas de relatórios
sistemas de veículos
jogos digitais
APIs
frameworks
ORMs
microserviços

-----------------------------------------------------------
EXEMPLO PROFISSIONAL - SISTEMA DE NOTIFICAÇÕES
-----------------------------------------------------------

Imagine um sistema que envia notificações por:

email
SMS
WhatsApp
push notification

Todas as notificações precisam ser enviadas.
Mas cada uma usa uma lógica diferente.
"""

class Notificacao(ABC):

    @abstractmethod
    def enviar(self, mensagem):
        pass


class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando email: {mensagem}")


class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando SMS: {mensagem}")


class WhatsApp(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando WhatsApp: {mensagem}")


notificacoes = [
    Email(),
    SMS(),
    WhatsApp()
]

for notificacao in notificacoes:
    notificacao.enviar("Sua compra foi aprovada!")


"""
-----------------------------------------------------------
VANTAGENS DO POLIMORFISMO
-----------------------------------------------------------

✔ reduz repetição de código
✔ evita muitos if/else
✔ facilita manutenção
✔ facilita expansão do sistema
✔ melhora organização
✔ permite trabalhar com objetos diferentes de forma padronizada

-----------------------------------------------------------
EXEMPLO DE EXPANSÃO DO SISTEMA
-----------------------------------------------------------

Se amanhã precisarmos adicionar uma nova forma de notificação,
não precisamos alterar a lógica principal.

Basta criar uma nova classe com o mesmo método enviar().
"""

class PushNotification(Notificacao):
    def enviar(self, mensagem):
        print(f"Enviando push notification: {mensagem}")


notificacoes.append(PushNotification())

for notificacao in notificacoes:
    notificacao.enviar("Novo acesso detectado.")


"""
-----------------------------------------------------------
DIFERENÇA ENTRE HERANÇA, ABSTRAÇÃO E POLIMORFISMO
-----------------------------------------------------------

HERANÇA:
Uma classe reaproveita estrutura de outra.

ABSTRAÇÃO:
Uma classe define um padrão obrigatório.

POLIMORFISMO:
Objetos diferentes respondem ao mesmo método
de formas diferentes.

-----------------------------------------------------------
EXEMPLO RESUMIDO
-----------------------------------------------------------

Classe abstrata:
FormaPagamento

Método obrigatório:
pagar()

Classes concretas:
PagamentoPix
PagamentoCartao
PagamentoBoleto

Polimorfismo:
todas usam pagar(), mas cada uma paga de um jeito.

-----------------------------------------------------------
ERROS COMUNS DOS ALUNOS
-----------------------------------------------------------

1. Achar que polimorfismo é apenas herança.

2. Criar métodos com nomes diferentes para comportamentos parecidos.

3. Usar muitos if/else quando poderia usar polimorfismo.

4. Não entender que o mesmo método pode ter respostas diferentes.

5. Confundir sobrescrita com sobrecarga.

6. Achar que Python exige tipo fixo para aplicar polimorfismo.

-----------------------------------------------------------
SOBRESCRITA X SOBRECARGA
-----------------------------------------------------------

Sobrescrita:
A classe filha redefine um método da classe pai.

Sobrecarga:
Métodos com o mesmo nome, mas parâmetros diferentes.

Em Python, a sobrecarga tradicional não funciona como em Java.
Se você criar dois métodos com o mesmo nome,
o último sobrescreve o anterior.

-----------------------------------------------------------
EXEMPLO DE CUIDADO EM PYTHON
-----------------------------------------------------------
"""

class ExemploSobrecarga:
    def mostrar(self, nome):
        print(f"Nome: {nome}")

    def mostrar(self, nome, idade):
        print(f"Nome: {nome}, Idade: {idade}")


exemplo = ExemploSobrecarga()

# exemplo.mostrar("Ana")  # ERRO
exemplo.mostrar("Ana", 25)


"""
-----------------------------------------------------------
COMO SIMULAR SOBRECARGA EM PYTHON?
-----------------------------------------------------------

Podemos usar parâmetros opcionais.
"""

class Pessoa:
    def apresentar(self, nome, idade=None):
        if idade is None:
            print(f"Nome: {nome}")
        else:
            print(f"Nome: {nome}, Idade: {idade}")


pessoa = Pessoa()

pessoa.apresentar("Carlos")
pessoa.apresentar("Carlos", 30)


"""
-----------------------------------------------------------
RESUMO FINAL
-----------------------------------------------------------

Polimorfismo = muitas formas.

Na prática:
objetos diferentes podem usar o mesmo método
e responder de formas diferentes.

O mesmo comando pode gerar comportamentos diferentes
dependendo do objeto.

-----------------------------------------------------------
REGRA GERAL
-----------------------------------------------------------

Se vários objetos precisam executar a mesma ação,
mas cada um executa do seu jeito,
provavelmente existe polimorfismo.

Exemplo:

pagamento.pagar()
animal.emitir_som()
notificacao.enviar()
funcionario.calcular_pagamento()

O método é o mesmo.
A execução muda conforme o objeto.

Isso transforma código repetitivo
em código flexível, limpo e profissional.
"""
