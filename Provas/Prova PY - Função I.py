from typing import Iterable, Tuple

def maior_e_menor(numeros: Iterable[float]) -> Tuple[float, float]:
    nums = list(numeros)
    if not nums:
        raise ValueError("A lista não pode ser vazia.")
    maior = menor = nums[0]
    for n in nums[1:]:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    return maior, menor

valores = [3.5, -2, 10, 7, 0]
print(maior_e_menor(valores))
