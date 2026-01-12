class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def dirigindo(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def acelerando(self):
        print("Moto está acelerando.")

Veiculo = Veiculo()
Carro = Carro()
Moto = Moto()

Veiculo.movimentar()
Carro.dirigindo()
Moto.acelerando()