from typing import List

def fibonacci_ate(n: int) -> List[int]:
    if not isinstance(n, int):
        raise ValueError("n deve ser um inteiro")
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq
print(fibonacci_ate(0))  
print(fibonacci_ate(1))  
print(fibonacci_ate(2))  
print(fibonacci_ate(6)) 