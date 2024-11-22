# Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
# Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
# À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário 
# e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, 
# calcule o valor total da compra somando todos os preços armazenados no dicionário. 
# Por fim, exiba o valor total da compra.



produtos = {}

for a in range(5):
    nome_produto = input(f"Informe o nome do Produto {a+1}: ")
    preco_produto = float(input(f"Informe o Preço do produto {nome_produto}: "))
    produtos[nome_produto] = preco_produto

valor_total = sum(produtos.values())

print("Produtos Cadastrados:")

for nome_produto, preco_produto in produtos.items():
    print(f"{nome_produto}: R$ {preco_produto:.2f}")

print(f"valor total da Compra: R${valor_total:.2f}")