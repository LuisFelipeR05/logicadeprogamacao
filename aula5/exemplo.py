#resposabilidade da variavel ---> guradar valores
#resposabilidade do for ---> percorrer valores ---> retirar ---> ou interar valores
#round() arredonda o valor que esta dentro dele
#print(5%2)# pegar somente o resto da divisao
#print(5//2)# pegar somente a parte inteira

for i in range(10,1,-1):  
    print(i)
    fatorial = int(input('Digite um numero para calcular o fatorial: '))
    resultado = 1
    for numero in range(fatorial,1,-1):
        resultado *= numero
    print(f'O fatorial de {fatorial} é {resultado}')