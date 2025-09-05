# Gerenciador de Tarefas no Python

tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("✅ Tarefa adicionada com sucesso!")


def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\n📋 Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")


def remover_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"❌ Tarefa removida: {removida}")
        else:
            print("Número inválido!")


def menu():
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---")
        print("1 - Adicionar Tarefa")
        print("2 - Listar Tarefas")
        print("3 - Remover Tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            remover_tarefa()
        elif opcao == "4":
            print("👋 Saindo do programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
