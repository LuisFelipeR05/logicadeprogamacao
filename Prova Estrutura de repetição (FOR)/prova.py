salario = float(input("Informe o salário (R$): "))
dias_atraso = int(input("Informe o número de dias de atraso: "))

multa = 0.0
for dia in range(1, dias_atraso + 1):
    if dia > 5:
        multa += salario * 0.02

if multa > 0:
    print(f"Multa total por atraso: R$ {multa:.2f}")
else:
    print("Não há multa. Pagamento dentro do prazo permitido.")
