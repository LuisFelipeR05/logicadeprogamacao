def contagem_regressiva(n: int) -> None:

    for i in range(n, 0, -1):
        print(i)
def contagem_regressiva_rec(n: int) -> None:

    if n < 1:
        return
    print(n)
    contagem_regressiva_rec(n - 1)
contagem_regressiva(5)
contagem_regressiva_rec(3)
