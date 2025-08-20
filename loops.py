#contador = 0
numero1 = int(input("Digite um inteiro"))
numero2 = int(input("Digite outro inteiro"))

while numero1 != numero2:

    if numero1 > numero2:
        numero1 = numero1 - numero2
    else:
        numero2 = numero2 - numero1


print(numero1)