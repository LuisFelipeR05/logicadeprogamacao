from typing import Iterable

def multiplicar_array(nums: Iterable[float]) -> float:

    produto = 1.0
    for n in nums:
        produto *= n
    return produto

print(multiplicar_array([2, 3, 4]))
print(multiplicar_array([1.5, 2]))    
print(multiplicar_array([]))