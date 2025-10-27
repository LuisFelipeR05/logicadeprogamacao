from typing import Iterable, Union

Number = Union[int, float]

def maior_numero(numeros: Iterable[Number]) -> Number:

    iterator = iter(numeros)
    try:
        maior = next(iterator)
    except StopIteration:
        raise ValueError("A lista não pode ser vazia")
    for x in iterator:
        if x > maior:
            maior = x
    return maior
print(maior_numero([3, 7, 2, 9, 5]))   
print(maior_numero([-4, -1, -10]))     
print(maior_numero([2.5, 3.75, 3.7])) 