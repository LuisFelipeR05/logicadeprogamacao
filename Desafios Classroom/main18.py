import time
import itertools

PINS_COMUNS = [
    "1234","0000","1111","1212","7777","1004","2000","4444",
    "2222","6969","9999","3333","5555","6666","1122","1313"
]

def descobrir_pin_interativo():
    pin_alvo = input("Digite uma senha de números (4 dígitos): ").strip()
    if not (pin_alvo.isdigit() and len(pin_alvo) == 4):
        print("Erro: informe exatamente 4 dígitos numéricos.")
        return

    tentativas = 0
    inicio = time.time()


    for pin in PINS_COMUNS:
        tentativas += 1
        if pin == pin_alvo:
            dur = time.time() - inicio
            print(pin)
            print(f"consegui advinhar a senha com {tentativas} tentativas.")
            print(f"Tempo: {dur:.2f}s")
            return

    for i in range(10000):
        pin = f"{i:04d}"
        if pin in PINS_COMUNS:
            continue
        tentativas += 1
        if pin == pin_alvo:
            dur = time.time() - inicio
            print(pin)
            print(f"consegui advinhar a senha com {tentativas} tentativas.")
            print(f"Tempo: {dur:.2f}s")
            return

    dur = time.time() - inicio
    print("Não foi possível encontrar a senha.")
    print(f"Tentativas realizadas: {tentativas}. Tempo: {dur:.2f}s")

if __name__ == "__main__":
    print("Atenção: use este script apenas em dispositivos ou contas que você possui.")
    descobrir_pin_interativo()