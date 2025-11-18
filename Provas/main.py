import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas - Flet"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START


    task_input = ft.TextField(label="Nova tarefa", width=400, autofocus=True)
    tasks_column = ft.Column(spacing=8, expand=True)


    def add_task(e):
        value = task_input.value.strip()
        if not value:
            return

        task_row = ft.Row(
            controls=[
                ft.Checkbox(label=value, expand=True),
                ft.IconButton(
                    ft.icons.DELETE,
                    tooltip="Remover",
                    on_click=lambda ev, tr=task_row: remove_task(ev, tr)
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True
        )
        tasks_column.controls.append(task_row)
        task_input.value = ""
        page.update()


    def remove_task(e, task_row):
        if task_row in tasks_column.controls:
            tasks_column.controls.remove(task_row)
            page.update()


    add_button = ft.ElevatedButton(text="Adicionar", on_click=add_task)


    task_input.on_submit = add_task


    page.add(
        ft.Column(
            controls=[
                ft.Row(controls=[task_input, add_button], alignment=ft.MainAxisAlignment.START),
                ft.Divider(),
                ft.Text("Tarefas:", weight=ft.FontWeight.BOLD),
                ft.Container(content=tasks_column, padding=ft.EdgeInsets(all=8), bgcolor=ft.colors.WHITE, expand=True)
            ],
            spacing=12,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)