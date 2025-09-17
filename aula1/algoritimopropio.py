primeiro_numero = input("Digite um numero inteiro: ")
primeiro_numero = int(primeiro_numero)

segundo_numero = input("Digite outro numero inteiro: ")
segundo_numero = int(segundo_numero)

if primeiro_numero > segundo_numero:
    primeiro_numero = primeiro_numero - segundo_numero
elif segundo_numero > primeiro_numero:
    segundo_numero = segundo_numero - primeiro_numero
else:
    print("numeros sao iguais")

    print(primeiro_numero , segundo_numero)