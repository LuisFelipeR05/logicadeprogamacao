notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor_a_receber = float(input('qual o valor a receber?'))
# 1700

valor_recebido = float(input('qual o valo recebido?'))
# 2000

diferenca = valor_recebido - valor_a_receber
# 300

for valor in notas_e_moedas: # 200
    quantidade_de_itens = 0
    while valor <= diferenca: # 200 < 300
        quantidade_de_itens += 1
        diferenca -= valor
    if quantidade_de_itens > 0:
        print(f'{quantidade_de_itens} itens de {valor}')