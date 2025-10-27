from typing import Union

Number = Union[int, float]

def calculadora(a: Number, b: Number, operacao: str) -> float:

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Os dois primeiros parâmetros devem ser números")
    op = operacao.strip().lower()
    if op in ("soma", "+", "add", "adição", "adicao"):
        return float(a + b)
    if op in ("subtração", "subtracao", "-", "sub", "menos"):
        return float(a - b)
    if op in ("multiplicação", "multiplicacao", "*", "mul", "vezes"):
        return float(a * b)
    if op in ("divisão", "divisao", "/", "div", "÷"):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return float(a / b)
    raise ValueError(f"Operação desconhecida: {operacao}")
print(calculadora(4, 2, "soma"))           
print(calculadora(4, 2, "subtração"))      
print(calculadora(4, 2, "multiplicação"))  
print(calculadora(4, 2, "divisão"))        
#print(calculadora(5, 0, "/"))    # ValueError: Divisão por zero não é permitida
print(calculadora(3, 7, "vezes"))          