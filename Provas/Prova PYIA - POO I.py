class Animal:
    def som(self):
        print("Este animal faz um som genérico.")


class Cachorro:
    def latir(self):
        print("O cachorro está latindo.")


class Gato:
    def miar(self):
        print("O gato está miando.")

animal = Animal()
cachorro = Cachorro()
gato = Gato()

animal.som()
cachorro.latir()
gato.miar()

