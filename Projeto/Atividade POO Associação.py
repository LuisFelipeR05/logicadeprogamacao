class Cliente:
    def __init__(self, nome: str):
        self.nome = nome.strip()
        self.gasto_total = 0.0

    def registrar_gasto(self, valor: float):
        self.gasto_total += valor


class Produto:
    def __init__(self, nome: str, quantidade: int, preco_unitario: float):
        self.nome = nome.strip()
        self.quantidade = int(quantidade)
        self.preco_unitario = float(preco_unitario)
        self.vendido_quantidade = 0
        self.vendido_valor = 0.0

    @property
    def total_produto_estoque(self):
        return self.quantidade * self.preco_unitario

    def vender(self, qtd: int):
        qtd = int(qtd)
        if qtd <= 0 or qtd > self.quantidade:
            raise ValueError("Quantidade inválida ou insuficiente.")
        valor = qtd * self.preco_unitario
        self.quantidade -= qtd
        self.vendido_quantidade += qtd
        self.vendido_valor += valor
        return valor


class Estoque:
    def __init__(self):
        self.clientes = {}      
        self.produtos = {}      
        self.total_faturado = 0.0
        self.total_itens_vendidos = 0

    def cadastrar_cliente(self, cliente: Cliente):
        key = cliente.nome.lower()
        if key in self.clientes:
            return False
        self.clientes[key] = cliente
        return True

    def cadastrar_produto(self, produto: Produto):
        key = produto.nome.lower()
        if key in self.produtos:
            return False
        self.produtos[key] = produto
        return True

    def vender_produto(self, nome_cliente: str, nome_produto: str, qtd: int):
        ck = nome_cliente.strip().lower()
        pk = nome_produto.strip().lower()
        if ck not in self.clientes:
            return "Cliente não cadastrado."
        if pk not in self.produtos:
            return "Produto não cadastrado."
        produto = self.produtos[pk]
        cliente = self.clientes[ck]
        if produto.quantidade == 0:
            return "Produto sem estoque."
        try:
            valor = produto.vender(qtd)
        except ValueError as e:
            return str(e)
        cliente.registrar_gasto(valor)
        self.total_faturado += valor
        self.total_itens_vendidos += qtd
        return f"Venda: {qtd} x {produto.nome} = R$ {valor:.2f}"

    def gerar_estatisticas(self):
        gasto_por_cliente = {c.nome: c.gasto_total for c in self.clientes.values()}
        faturamento_por_produto = {p.nome: p.vendido_valor for p in self.produtos.values()}
        mais_vendidos = sorted(self.produtos.values(), key=lambda x: x.vendido_quantidade, reverse=True)
        menos_vendidos = sorted(self.produtos.values(), key=lambda x: x.vendido_quantidade)
        return {
            "total_faturado": self.total_faturado,
            "total_itens_vendidos": self.total_itens_vendidos,
            "gasto_por_cliente": gasto_por_cliente,
            "faturamento_por_produto": faturamento_por_produto,
            "mais_vendidos": [(p.nome, p.vendido_quantidade) for p in mais_vendidos],
            "menos_vendidos": [(p.nome, p.vendido_quantidade) for p in menos_vendidos],
        }


def menu():
    estoque = Estoque()
    while True:
        print("\n1 Cadastrar Cliente | 2 Cadastrar Produto | 3 Vender Produto | 4 Estatísticas | 0 Sair")
        op = input("Opção: ").strip()
        if op == "1":
            nome = input("Nome do cliente: ").strip()
            if nome and estoque.cadastrar_cliente(Cliente(nome)):
                print("Cliente cadastrado.")
            else:
                print("Cliente já existe ou nome inválido.")
        elif op == "2":
            nome = input("Nome do produto: ").strip()
            try:
                qtd = int(input("Quantidade: ").strip())
                preco = float(input("Preço unitário: ").strip())
            except ValueError:
                print("Quantidade ou preço inválido.")
                continue
            if estoque.cadastrar_produto(Produto(nome, qtd, preco)):
                print("Produto cadastrado.")
            else:
                print("Produto já existe.")
        elif op == "3":
            cliente = input("Nome do cliente: ").strip()
            produto = input("Nome do produto: ").strip()
            try:
                qtd = int(input("Quantidade a vender: ").strip())
            except ValueError:
                print("Quantidade inválida.")
                continue
            print(estoque.vender_produto(cliente, produto, qtd))
        elif op == "4":
            s = estoque.gerar_estatisticas()
            print(f"Total faturado: R$ {s['total_faturado']:.2f}")
            print(f"Total itens vendidos: {s['total_itens_vendidos']}")
            print("Gasto por cliente:", s['gasto_por_cliente'])
            print("Faturamento por produto:", s['faturamento_por_produto'])
            print("Mais vendidos:", s['mais_vendidos'])
            print("Menos vendidos:", s['menos_vendidos'])
        elif op == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
