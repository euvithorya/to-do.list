def add_task(task_list, task):
    """Adiciona uma nova tarefa à lista."""
    task_list.append({"tarefa": task, "concluida": False})

def list_tasks(task_list):
    """Lista todas as tarefas."""
    if not task_list:
        return "Nenhuma tarefa disponível."
    resultado = ""
    for i, task in enumerate(task_list):
        status = "✅" if task["concluida"] else "❌"
        resultado += f"{i + 1}. {task['tarefa']} - {status}\n"
    return resultado

def mark_task_as_done(task_list, index):
    """Marca uma tarefa como concluída."""
    if 0 <= index < len(task_list):
        task_list[index]["concluida"] = True
        return "Tarefa marcada como concluída!"
    return "Índice inválido!"

def delete_task(task_list, index):
    """Remove uma tarefa da lista."""
    if 0 <= index < len(task_list):
        task_list.pop(index)
        return "Tarefa removida com sucesso!"
    return "Índice inválido!"

#:V
