class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self._historico = [self.velocidade]

    def acelerar(self):
        self.velocidade += 8
        self._historico.append(self.velocidade)
        return self.velocidade

    def frear(self):
        self.velocidade -= 3
        if self.velocidade < 0:
            self.velocidade = 0
        self._historico.append(self.velocidade)
        return self.velocidade

    def velocidade_media(self):
        return sum(self._historico) / len(self._historico)

modelo = input("Digite o modelo: ")
ano = input("Digite o ano: ")
cor = input("Digite a cor: ")
car = Carro(modelo, ano, cor)

print("Velocidade inicial:", car.velocidade)
car.acelerar()
car.acelerar()
car.acelerar()
car.frear()
print("Velocidade final:", car.velocidade)
print("Velocidades registradas:", car._historico)
print("Velocidade média:", car.velocidade_media())