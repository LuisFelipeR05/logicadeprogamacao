class Carro:
    def __init__(self,modelo,ano,cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.frear = 0

    def acelerar(self):
        self.velocidade += 8
        return self.velocidade
    
    def frear(self):
        self.velocidade -= 3
        return self.velocidade


modelo = input("Digite o modelo")
ano = input("Digite o ano")
cor = input("Digite o cor")
car = Carro(modelo,ano,cor)

print(car.velocidade)
car.acelerar()
car.frear()
print(car.velocidade)

