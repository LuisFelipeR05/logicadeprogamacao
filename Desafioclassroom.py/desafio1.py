import math

area_m2 = float(input("Informe a área a ser pintada (m²): "))


litros_necessarios = area_m2 / 6 * 1.10


quantidade_latas = math.ceil(litros_necessarios / 18)
preco_latas = quantidade_latas * 80


quantidade_galoes = math.ceil(litros_necessarios / 3.6)
preco_galoes = quantidade_galoes * 25


quantidade_latas_mix = int(litros_necessarios // 18)
resto_litros = litros_necessarios - quantidade_latas_mix * 18
quantidade_galoes_mix = math.ceil(resto_litros / 3.6)
preco_mix = quantidade_latas_mix * 80 + quantidade_galoes_mix * 25


print(f"\nOpção 1 – Só latas (18 L): {quantidade_latas} lata(s) → R$ {preco_latas:.2f}")
print(f"Opção 2 – Só galões (3,6 L): {quantidade_galoes} galão(ões) → R$ {preco_galoes:.2f}")
print(f"Opção 3 – Mistura: {quantidade_latas_mix} lata(s) e {quantidade_galoes_mix} galão(ões) → R$ {preco_mix:.2f}")