def contar_vogais(texto: str) -> int:

    vogais = set("aeiouAEIOUáàãâéèêíïóôõúùüÁÀÃÂÉÈÊÍÏÓÔÕÚÙÜ")
    contador = 0
    for ch in texto:
        if ch in vogais:
            contador += 1
    return contador

print(contar_vogais("Olá, mundo"))      
print(contar_vogais("Exemplo: ABC"))
print(contar_vogais(""))        
print(contar_vogais("PYTHON"))        