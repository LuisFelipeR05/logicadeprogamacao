import random

print("Bem vindo ao jogo de adivinhação")
print("Tente adivinhar o numero entre 1 e 100")

numero_aleatorio = random.randint(0,100)
palpite_jogador = int(input("Digite um numero_inteiro de 1 a 100: "))
numero_tentativas = 1

while numero_aleatorio != palpite_jogador:
    numero_tentativas += 1

    if palpite_jogador < numero_aleatorio:
        print("O número é maior")
    elif palpite_jogador > numero_aleatorio:   
        print("O número é menor")

        palpite_jogador = int(input("Digite um novo numero "))

    print(f"Parabéns você acertou o número {numero_aleatorio} em {numero_tentativas} tentativas")

    print("Fim do jogo")
    print("Obrigado por jogar!")