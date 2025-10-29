import flet as ft
def main2(pagina:ft.Page):
    def cadastrar_produto(e): 
        produto = {
        "nome":nome_produto.vaule,
        "preco":preco_produto.vaule,
        "quantidade":quantidade_produto.vaule
    }
        estoque.append(produto)
        print(estoque)
        carregar_produtos()
        pagina.update()

    def carregar_produtos():
        linha.controls.append(ft.Text(produto))

    titulo = ft.Text("Gerenciamento de Estoque",size=50)
    nome_produto = ft.TextField(hint_text="Digite o nome do produto")
    preco = ft.TextField(hint_text="Digite o preco:")
    quantidade = ft.TextField(hint_text="Digite a quantidade:")
    linha = ft.Row(controls=[])
    botao = ft.ElevatedButton("Cadastrar",on_click=cadastrar_produto)
    pagina.add(titulo,nome_produto,preco,quantidade,botao,linha)


ft.app(target=main2)

