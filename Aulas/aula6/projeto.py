# Desafio em dupla

# - Doceria, você foi contratado para desenvolver um sistema para uma doceria
# - O programa deverá rodar em looping pedindo informações do tipo, nome, telefone e email.
# - O programa deverá quebrar o looping de repetição se o nome digitado for "sair"
# - No final do programa o algoritmo irá sortear um cliente aleatoriamente para receber um brinde de dia das Crianças

# Critério de Avaliação 
# - Os nomes terão que ser armazenados e organizados de maneira clara e legível
# - O código não pode quebrar
# - tente deixar visualmente bonito (capricha ai )

print("Bem vindo ao cadastro")
print("Digite seu nome, email, telefone para finalizar o cadastro")
usuarios = []
while True:
    nome = input("digite seu nome")
    email = input("digite seu email")
    telefone = input("digite seu telefone")

    