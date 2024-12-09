# Definição de Dados:

# Defina estruturas de dados para representar tarefas. Cada tarefa pode incluir

# informações como nome, descrição, prioridade e categoria. Você pode usar
# dicionários para representar as tarefas.

# Funções:
# Crie funções para adicionar tarefas, listar tarefas, marcar tarefas
# como concluídas, exibir tarefas por prioridade ou categoria, e outras
# funcionalidades que desejar.

# Menu de Comandos:
# Crie um menu de comandos de linha de comando que permita ao
# usuário interagir com o programa.


lista_de_tarefas = []

def adicionar_tarefa():
    nome = input("Informe o nome da Tarefa: ")
    prioridade = input("Informe a prioridade da Tarefa: ")
    categoria = input("Informe a categoria da Tarefa: ")
    status = input("Informe o status da Tarefa: ")

    tarefa = {
        "nome": nome,
        "prioridade": prioridade,
        "categoria": categoria,
        "status": status
    }

    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")


def visualizar_tarefas():
    if lista_de_tarefas:
        for i in range(len(lista_de_tarefas)):
            print(f"Tarefa: {i+1}: ")
            print(f"Nome: {lista_de_tarefas[i]["nome"]}")
            print(f"Prioridade: {lista_de_tarefas[i]["prioridade"]}")
            print(f"Categoria: {lista_de_tarefas[i]["categoria"]}")
            print(f"Status: {lista_de_tarefas[i]["status"]}")
    else:
        print("Nenhuma Tarefa Encontrada.")



def remover_tarefa():
    nome = input("Informe o nome da tarefa que deseja remover: ")
    for tarefa in lista_de_tarefas:
        if tarefa["nome"] == nome:
            lista_de_tarefas.remove(tarefa)
            print("Tarefa removida com sucesso.")
            break
    else:
        print("Tarefa não encontrada.")


while True:
    menu = """
        1- Adicionar Tarefa
        2- Visualizar Tarefa
        3- Remover Tarefa
        4- Sair
    """
    print(menu)
    opcao = int(input("Informe a opção desejada: "))
    
    match opcao:
        case 1:
            adicionar_tarefa()
        case 2:
            visualizar_tarefas()
        case 3:
            remover_tarefa()
        case 4:
            print("Saindo do programa")
            break
        case _:
            print("Opção invalida")