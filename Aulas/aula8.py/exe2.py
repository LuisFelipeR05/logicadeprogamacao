from random import randint

numero_aleatorio = randint(1,10)
numero_tentativas = 1
tentativas_passadas = []

while True:
    palpite_jogador = int(input('Digite um numero_inteiro de 1 a 10: '))
    if numero_aleatorio == palpite_jogador:
    
        if palpite_jogador in tentativas_passadas:
            print('Errado tente novamente!')
        else: 
            tentativas_passadas.append(palpite_jogador)
            numero_tentativas += 1

            if palpite_jogador > numero_aleatorio:
                print('Errado! O número é maior')
            else:
                print('Errado! O número é menor')

    

    print(f"Prabens! voce acertou em {numero_tentativas} tentativas")
    print(tentativas_passadas)
    print('Voce acertou!')
    break