import random

numero_aleatorio = random.randint(1,100)
palpite_jogador = int(input("Digite um numero_inteiro de 1 a 100: "))

numero_tentativas = 1

tentativas_passadas = []

while numero_aleatorio != palpite_jogador:

    tentativas_passadas.append(palpite_jogador)

    numero_tentativas += 1

    if palpite_jogador < numero_aleatorio:
        print('O número é maior')
    else:
        palpite_jogador > numero_aleatorio
        print('O número é menor')

        palpite_jogador = int(input("Digite um novo numero "))


print(f"acertou em {numero_tentativas} tentativas")
print(tentativas_passadas)