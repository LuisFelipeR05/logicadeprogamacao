horas_trabalhadas = float(input("Digite o total de horas trabalhadas na semana: "))

jornada_padrao = 44
if horas_trabalhadas > jornada_padrao:
    horas_extras = horas_trabalhadas - jornada_padrao
    valor_hora = float(input("Digite o valor da hora normal (em R$): "))
    valor_hora_extra = valor_hora * 1.5
    total_horas_extras = horas_extras * valor_hora_extra
    print(f"{horas_extras:.0f} horas extras a R$ {valor_hora_extra:.2f} cada.")
    print(f"Total a receber pelas horas extras: R$ {total_horas_extras:.2f}")
else:
     print("Jornada cumprida corretamente. Não há horas extras a pagar.")