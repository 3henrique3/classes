"""
Dicionários são estruturas de dados para armazenar informações em formato de chave-valor
"""

loja = [
    {
        'fruta_id' : 1,
        'nome' : 'maracujá',
        'cor' : 'amarelo',
    },
    {
        'fruta_id' : 2,
        'nome' : 'laranja',
        'cor' : 'laranja',
    },
    {
        'fruta_id' : 3,
        'nome' : 'amora',
        'cor' : 'roxo'
    }
]

print("O nome da primeira fruta é: ", loja[0]["nome"])
print("\nO nome da primeira fruta é: ", loja[1]["nome"])
print("\nO nome da primeira fruta é: ", loja[2]["nome"])

# Alterando um atributo de um dicionário da lista

loja[2]["cor"] = "azul"

print("\nA cor da terceira fruta foi alterada para: ", loja[2]["cor"])

