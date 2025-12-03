
class Cliente:
    def cliente(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone
        self.gasto_total = 0
nome = input(" digite seu nome" )
email = input(" digite seu email" )
telefone = input(" digite seu telefone" )

class Produto:
    def produto(self,nome,quantidade,preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total_produto_estoque = self.quantidade * self.preco_unitario
nome = input("digite o nome do produto")
quantidade = input("digite a quantidade do produto")



class Estoque:
    def vender_produto(self,produto:Produto, cliente:Cliente):
        self.clientes = []
        self.produtos = []


def cadastrar_cliente(self,cliente:Cliente):
    self.cliente.append(cliente)
    print("cliente cadastrado!")



def cadastrar_produto(self,produto:Produto):
    self.produto.append(produto)
    print("Produto cadastrado com sucesso!")


def vender_produto(self,produto:Produto, cliente:Cliente):
    if not (produto in self.produtos):
        print("Produto não indisponivel no estoque!")
    else:
        quantidade_vendida = int(input("Digite a quantidade que deseja comprar"))
    print(f"Produto vendido com sucesso! Agora restam {produto.quantidade}quantidades.")
    total_venda = produto1.preco_unitario * quantidade_vendida
    cliente.gasto_total += total_venda

    print(f"Total venda:")



if __name__ == "__main__":

    estoque = Estoque()
    produto1 = Produto(nome)
    print("produto1")
    cliente1 = Cliente(nome)
    print("clinte1")