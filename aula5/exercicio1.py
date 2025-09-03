numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for numero in numeros:
    if numero % 2 == 0:
        soma += numero
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
print(f'soma dos pares é {soma}')
