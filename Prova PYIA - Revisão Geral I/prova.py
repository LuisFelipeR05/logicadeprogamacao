produtos = {}

for i in range(1, 6):
    nome = input(f"Produto {i} - nome: ")
    preco = float(input(f"Produto {i} - preço (use ponto para decimais): R$ "))
    produtos[nome] = preco

total = sum(produtos.values())
print(f"\nValor total da compra: R$ {total:.2f}")