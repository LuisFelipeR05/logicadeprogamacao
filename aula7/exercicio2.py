numeros = [1,2,3]
dobro = map(lambda x:x * 2, numeros)

numeros = [2,3,4]
suscessor = map(lambda x:x + 1, numeros)

numeros = [1,2,3]
antecessor = map(lambda x:x - 1, numeros)

numeros = [1,2,3]
suscessor_quintuplo = map(lambda x: x *5 + 1, numeros)

print(list(dobro))
print(list(suscessor))
print(list(antecessor))
print(list(suscessor_quintuplo))