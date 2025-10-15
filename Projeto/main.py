from fastapi import FastAPI
from tasks import (

    add_task, list_tasks,
    complete_task, list_by_priority,
    list_by_category
)

app = FastAPI()

@app.post("/tasks/")
def create_task(name: str, description: str, priority: str, category: str):
    add_task(name, description, priority, category)
    return {"message": "Task added successfully"}

@app.get("/tasks/")
def read_tasks(show_completed: bool = True):
    return list_tasks(show_completed=show_completed)

@app.put("/tasks/{task_id}/complete")
def finish_task(task_id: int):
    complete_task(task_id)
    return {"message": "Task marked as complete"}

@app.get("/tasks/priority/{priority}")
def read_tasks_by_priority(priority: str):
    return list_by_priority(priority)

@app.get("/tasks/category/{category}")
def read_tasks_by_category(category: str):
    return list_by_category(category)

def print_menu():
    print("""
1) Adicionar tarefa
2) Listar todas as tarefas
3) Listar tarefas pendentes
4) Marcar tarefa como concluída
5) Listar por prioridade
6) Listar por categoria
0) Sair
""")

def main():
    while True:
        print_menu()
        choice = input("Escolha uma opção: ").strip()
        if choice == "1":
            name = input("Nome: ")
            desc = input("Descrição: ")
            prio = input("Prioridade (Baixa/Média/Alta): ")
            cat = input("Categoria: ")
            add_task(name, desc, prio, cat)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks(show_completed=False)
        elif choice == "4":
            tid = int(input("ID da tarefa: "))
            complete_task(tid)
        elif choice == "5":
            prio = input("Prioridade (Baixa/Média/Alta): ")
            list_by_priority(prio)
        elif choice == "6":
            cat = input("Categoria: ")
            list_by_category(cat)
        elif choice == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()