def soma_pares(*args: int) -> int:
    total = 0
    for x in args:
        if isinstance(x, int) and x % 2 == 0:
            total += x
    return total

print(soma_pares(1, 2, 3, 4, 5, 6))    
print(soma_pares(10, -2, 3.0, "8", 7)) 
print(soma_pares())                    
