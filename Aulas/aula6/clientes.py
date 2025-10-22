clientes = []
cliente = {}

# cliente["nome"] = input("digite o seu nome complteto: ")
# cliente["telefone"] = input("digite seu telefone:  ")
# cliente["profissão"] = input("digite sua profissão: ")
# cliente["email"] = input("digite o seu email: ")
# clientes.append(cliente)

print(clientes)

for i in range(3):
    cliente["nome"] = input("digite o seu nome complteto: ")
    cliente["telefone"] = input("digite seu telefone:  ")
    cliente["profissão"] = input("digite sua profissão: ")
    cliente["email"] = input("digite o seu email: ")

    clientes.append(cliente.copy())

for cliente in clientes:
    print(cliente)