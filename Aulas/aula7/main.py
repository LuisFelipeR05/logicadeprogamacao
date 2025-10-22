import string
import random
def gerar_senha(tamamnho):
    # caracteres =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    letras = string.ascii_letters
    especiais = "!@#$%¨&*()_-=?"
    numeros = "0123456789"


    senha_gerada = ""
    for i in range(tamamnho):
        senha_gerada += random.choice(letras + especiais + numeros)

    return senha_gerada

# print(gerar_senha(15))

def descobridor_de_senhas(senha):
    contador = 0
    while True:
        senha_gerada = ""
        for i in range(4):
            senha_gerada += str(random.randint(0,9))
        contador += 1
        print(senha_gerada)
        print(senha)
        
        if senha_gerada == senha:
            print(f"Senha encontrada: {senha_gerada}")
            print(f"Total de tentativas: {contador}")
            break

        # print(random.randint(0,9), end="")




descobridor_de_senhas("1234")
