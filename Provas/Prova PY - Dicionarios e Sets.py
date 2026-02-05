usuarios = {

    "Luis": "12345",
    "ANA": "4321",
    "Clara": "54321"
}

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario in usuarios:

    if usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")
