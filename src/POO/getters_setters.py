# Introdução ao @Property
#

class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self._preco = preco

    @property
    def nome(self):
        # Aqui podemos controlar o retorno/consulta
        return self.__nome
    
    @property
    def preco(self):
        # Aqui podemos controlar o retorno/consulta
        return self._preco
    
produto1 = Produto(nome = str(input("Informe o nome do produto: ")),
    preco = float(input("Informe o valor do produto: ")))

print(produto1.nome)
print(produto1.preco)


# @setters - Controla as modificações
class ProdutoSeguro:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser maior que 0.")
        
        else:
            self.preco = valor
            return self.preco

produtoSeguro1 = ProdutoSeguro(nome = str(input("Informe o nome do produto: ")),
preco = float(input("Informe o preco do ProdutoSeguro: ")))

print(produtoSeguro1.preco)


class Usuario:
    def __init__(self, nome, age):
        self._nome = nome
        self.__age = age

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, cadastroNome):
        if not cadastroNome.strip():
            raise ValueError("Nome inválido...")
        
        self._nome = cadastroNome

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, cadastroAge):
        if not cadastroAge and cadastroAge <= 0:
            raise ValueError("Idade inválida...")
        
        self.__age = cadastroAge

    def presentation(self):
        print(f"Your name is {self._nome} and your age is {self.__age}.")

usuario1 = Usuario(nome = str(input("Informe o seu nome: ")),
                   age = int(input("Informe a sua idade: ")))

usuario1.presentation()

usuario1.nome = "Patrick"
usuario1.age = 100
usuario1.presentation()
