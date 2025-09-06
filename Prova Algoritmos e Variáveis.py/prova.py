def calcula_multa_rescisoria(tempo_servico_anos: float, valor_fgts: float) -> float:

    if tempo_servico_anos > 1:
        return valor_fgts * 0.4
    return 0.0

tempo = 2
fgts = 10000  
multa = calcula_multa_rescisoria(tempo, fgts)

if multa > 0:
    print(f"A multa será de R$ {multa:,.2f}")
else:
    print("Não há multa rescisória")
    meses = 18
    anos = meses / 12
    print(f"{meses} meses equivalem a {anos} anos")