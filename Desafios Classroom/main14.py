def desconto(preco: float, percentual: float = 10.0) -> float:

    if preco < 0:
        raise ValueError("Preço não pode ser negativo")
    if percentual < 0:
        raise ValueError("Percentual não pode ser negativo")
    desconto_valor = preco * (percentual / 100.0)
    return preco - desconto_valor
print(desconto(100.0))          
print(desconto(200.0, 25))      
print(desconto(50.0, 0))        