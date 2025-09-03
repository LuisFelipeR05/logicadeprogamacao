# Fazer um algoritimo em loop infinito

usuariso = []
while True:
    print("=*30")
    print("Bem vindo ao sistema de cadastro")
    print("=*30")
    print("1-faça seu cadastro de usuario:")
    print("2-digite seu nome:")
    print("3-concluir cadastro")
    print("4-usuario cadastrado com sucesso")
    print("5-atualizar cadastro")
    print("6-deletar cadastro")
    print("7-listar usuarios cadastrados")
    print("8-sair do sistema")

opção = input("Digite a opção desejada: ")
if opção == "1":
    nome = input("Digite seu nome: ")
    usuariso.append(nome)
    print("Usuario cadastrado com sucesso!")
elif opção == "2":
    for i, nome in enumerate(usuariso):
        print(f"{i + 1}. {nome}")
indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
novo_nome = input("Digite o novo nome: ")

elif opção == "3":
    for i, nome in enumerate(usuariso):
        print(f"{i + 1}. {usuario}")
    indice = int(input("Digite o número do usuário que deseja deletar: ")) - 1
    usuariso.pop(indice)
    print("Usuário deletado com sucesso!")
elif opção == "4":
    for i, nome in enumerate(usuariso):
        print(f"{i + 1}. {nome}")
elif opção == "5":
    print("Saindo do sistema...")
    break
else:
    print("Opção inválida. Tente novamente.")
    usuariso[indice] = novo_nome
    print("Usuário atualizado com sucesso!")