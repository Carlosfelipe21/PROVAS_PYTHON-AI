# Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. 
# Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. 
# Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.

contato = {}

contato["nome"] = input("digite o nome do contato: ")
contato["E-mail"] = input("digite o E-mail do contato: ")
contato["Telefone"] = input("digite o telefone do contato: ")

print("\n Os valores do contatos foram inseridas.")

for chave, valor in contato.items():
    print(f"{chave.capitalize()}: {valor}")