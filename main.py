from todo_list import add_task, list_tasks, mark_task_as_done, delete_task

def main():
    task_list = []
    
    while True:
        print("\n--- To-Do List ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            add_task(task_list, tarefa)
            print("Tarefa adicionada!")
        
        elif escolha == "2":
            print("\n--- Lista de Tarefas ---")
            print(list_tasks(task_list))
        
        elif escolha == "3":
            try:
                index = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
                print(mark_task_as_done(task_list, index))
            except ValueError:
                print("Por favor, digite um número válido!")
        
        elif escolha == "4":
            try:
                index = int(input("Digite o número da tarefa para remover: ")) - 1
                print(delete_task(task_list, index))
            except ValueError:
                print("Por favor, digite um número válido!")
        
        elif escolha == "5":
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

#:V
