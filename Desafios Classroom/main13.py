def eh_palindromo(texto: str) -> bool:

    if not isinstance(texto, str):
        raise ValueError("Entrada deve ser uma string")
    filtrado = ''.join(ch.lower() for ch in texto if ch.isalnum())
    return filtrado == filtrado[::-1]
print(eh_palindromo("NATAN"))            
print(eh_palindromo("A man, a plan, a canal: Panama")) 
print(eh_palindromo("Olá"))              
print(eh_palindromo(""))                 