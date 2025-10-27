def calcular_imc(peso: float = 70.0, altura: float = 1.75) -> float:
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero")
    imc = peso / (altura * altura)
    return round(imc, 2)
print(calcular_imc())            
print(calcular_imc(80, 1.8))    
print(calcular_imc(peso=60))     