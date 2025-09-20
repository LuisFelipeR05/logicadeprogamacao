salario = float(input("Informe o salário mensal (R$): ").replace(",", "."))
meses = int(input("Informe o número de meses trabalhados (0–12): "))

if meses < 0 or meses > 12:
    print("Quantidade de meses inválida. Deve ser entre 0 e 12.")
else:
    ferias = (salario / 12) * meses
    print(f"Férias proporcionais de: R$ {ferias:.2f}")