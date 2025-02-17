# Crie uma função chamada lancar_dados que utilizará o módulo random para simular o lançamento de dois dados
#  Cada dado deve gerar um número aleatório entre 1 e 6.
# A função deve somar os resultados desses dois lançamentos e retornar o valor total.

import random

def lancar_dados():
    dados_1 = random.randint(1, 6)
    dados_2 = random.randint(1, 6)
    somar_dados = dados_1 + dados_2
    return somar_dados
resultado = lancar_dados
print(f"O resultado do laçamento de dados é: {resultado} ")