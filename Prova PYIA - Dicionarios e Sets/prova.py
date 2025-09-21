contato = {}

print(contato)

contato["nome"] = input("digite o seu nome de contato: ")
contato["telefone"] = input("digite o seu telefone: ")
contato["email"] = input("digite o seu email: ")

print("usuario cadastrado com sucesso!")
for chave, valor in contato.items():
    print(f"{chave}: {valor}")
