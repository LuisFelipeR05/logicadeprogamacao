import random

def lancar_dados():

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

resultado = lancar_dados()
print(f"Soma dos dados: {resultado}")