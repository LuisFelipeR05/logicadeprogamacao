from typing import Union

Number = Union[int, float]

def media(n1: Number, n2: Number, n3: Number) -> float:
    try:
        s = float(n1) + float(n2) + float(n3)
    except (TypeError, ValueError):
        raise ValueError("Todas as notas devem ser números")
    resultado = s / 3.0
    return round(resultado, 2)
print(media(7, 8, 9))        
print(media(6.5, 7.25, 8))   
print(media(10, 10, 9.5))    