class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

class Bike:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 2

carro1 = Carro()
print(carro1.velocidade)
carro1.acelerar()
print(carro1.velocidade)

bike1 = Bike()
print(bike1.velocidade)
bike1.acelerar()
print(bike1.velocidade)


