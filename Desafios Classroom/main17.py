import string
import secrets

def gerar_senha(tamanho: int = 6) -> str:
    if not isinstance(tamanho, int):
        raise ValueError("tamanho deve ser um inteiro")
    if tamanho < 1:
        raise ValueError("tamanho deve ser pelo menos 1")

    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))
print(gerar_senha())       
print(gerar_senha(12))    