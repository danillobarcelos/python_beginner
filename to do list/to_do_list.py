lista_tarefas = []

def add_to_list(tarefa="Nova Tarefa", desc="Descrição", status=False):
    task = {'tarefa': tarefa, "descricao": desc, "finalizada" : status}

    lista_tarefas.append(task)
    return f"A nova tarefa \"{task['tarefa']}\" foi criada!"

def remove_from_list(tarefa):
    for task in lista_tarefas:
        if task["tarefa"] == tarefa:
            lista_tarefas.remove(task)
            print(f"A tarefa \"{tarefa}\" foi removida com sucesso!")
            return
    
    print(f"A tarefa \"{tarefa}\"  não foi encontrada!!")

print(add_to_list("Lavar louça", "Lavar louça do almoço"))
remove_from_list("Lavar louça")
