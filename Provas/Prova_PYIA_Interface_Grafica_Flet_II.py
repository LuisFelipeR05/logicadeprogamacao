import flet
from flet import Page, TextField, ElevatedButton, Column, Row, Text, SnackBar, AlertDialog, ElevatedButtonStyle

def main(page: Page):
    page.title = "Formulário de Contato"
    page.padding = 20
    page.vertical_alignment = "start"


    nome = TextField(label="Nome", width=400)
    email = TextField(label="Email", width=400)
    mensagem = TextField(label="Mensagem", multiline=True, min_lines=4, width=400)


    snackbar = SnackBar(content=Text(""), open=False)
    page.snack_bar = snackbar

    def enviar_click(e):
        n = nome.value.strip()
        em = email.value.strip()
        msg = mensagem.value.strip()


        if not n:
            page.snack_bar.content = Text("Por favor, informe o nome.")
            page.snack_bar.open = True
            page.update()
            return
        if not em or "@" not in em:
            page.snack_bar.content = Text("Por favor, informe um email válido.")
            page.snack_bar.open = True
            page.update()
            return
        if not msg:
            page.snack_bar.content = Text("Por favor, escreva uma mensagem.")
            page.snack_bar.open = True
            page.update()
            return


        dados = {
            "nome": n,
            "email": em,
            "mensagem": msg
        }
        print("Formulário recebido:", dados) 

     
        nome.value = ""
        email.value = ""
        mensagem.value = ""
        page.update()

    
        dialog = AlertDialog(
            title=Text("Formulário enviado"),
            content=Text("Obrigado! Sua mensagem foi enviada com sucesso."),
            actions=[ElevatedButton("Fechar", on_click=lambda e: page.dialog.close())],
            actions_align="end"
        )
        page.dialog = dialog
        page.dialog.open = True
        page.update()

    botao_enviar = ElevatedButton(text="Enviar", on_click=enviar_click)


    page.add(
        Column(
            [
                Text("Preencha o formulário de contato", size=20),
                nome,
                email,
                mensagem,
                Row([botao_enviar], alignment="center")
            ],
            spacing=15
        )
    )

if __name__ == "__main__":
    flet.app(target=main, view=flet.WEB_BROWSER)
