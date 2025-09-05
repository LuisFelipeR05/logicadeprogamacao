# Fazer um algoritimo em loop infinito

usuariso = []
while True:
    print("=*30")
    print("Bem vindo ao sistema de cadastro")
    print("=*30")
    print("1-faça seu cadastro de usuario:")
    print("2-digite seu nome:")
    print("3-concluir cadastro")
    print("4-atualizar cadastro")
    print("5-deletar cadastro")
    print("6-listar usuarios cadastrados")
    print("7-sair do sistema")

    opção = input("Digite a opção desejada: ")

    if opção == "1":
        nome = input("Digite seu nome: ")
        usuariso.append(nome)

        print("Usuario cadastrado com sucesso!")

    elif opção == "2":
        for i, nome in enumerate(usuariso):
            print(f"{i + 1}. {nome}")
        indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
        if 0 <= indice < len(usuariso):
            novo_nome = input("Digite o novo nome: ")
            usuariso[indice] = novo_nome
        
            print("Usuário atualizado com sucesso!")
        
        else:
            print("Índice inválido.")
    elif opção == "3":
        print("Cadastro concluído.")
        for i, nome in enumerate(usuariso):
            print(f"{i + 1}. {nome}")

    elif opção == "4":
        for i, nome in enumerate(usuariso):
            print(f"{i + 1}. {nome}")
        indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
        if 0 <= indice < len(usuariso):
            novo_nome = input("Digite o novo nome: ")
            usuariso[indice] = novo_nome
        
            print("Usuário atualizado com sucesso!")
        
        else:
            print("Índice inválido.")
    elif opção == "5":
        for i, nome in enumerate(usuariso):
            print(f"{i + 1}. {nome}")
        indice = int(input("Digite o número do usuário que deseja deletar: ")) - 1
        if 0 <= indice < len(usuariso):
            usuariso.pop(indice)
            print("Usuário deletado com sucesso!")
        else:
            print("Índice inválido.")

    elif opção == "6":
        print("Usuários cadastrados:")
        for i, nome in enumerate(usuariso):
            print(f"{i + 1}. {nome}")

    elif opção == "7":
        print("Saindo do sistema...")
        break

        
            