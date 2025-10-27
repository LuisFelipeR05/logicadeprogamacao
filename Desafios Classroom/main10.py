def par_ou_impar(n: int) -> str:
    if not isinstance(n, int):
        raise ValueError("Entrada deve ser um número inteiro")
    return "par" if n % 2 == 0 else "ímpar"
print(par_ou_impar(4))   
print(par_ou_impar(7))   
print(par_ou_impar(0))   