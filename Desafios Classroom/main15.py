def fatorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("n deve ser um inteiro")
    if n < 0:
        raise ValueError("fatorial não é definido para números negativos")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def fatorial_rec(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("n deve ser um inteiro")
    if n < 0:
        raise ValueError("fatorial não é definido para números negativos")
    if n == 0:
        return 1
    return n * fatorial_rec(n - 1)
print(fatorial(0))   
print(fatorial(5))   
print(fatorial_rec(6)) 