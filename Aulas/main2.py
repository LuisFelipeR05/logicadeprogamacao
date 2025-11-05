nome = "Luna"
cor = "beje"
caracteristicas = "pequena"
raca = "pincher"


class Cachorro:
    def __init__(self,nome,cor,caracteristicas,raca):
        self.nome = nome
        self.cor = cor
        self.caracteristicas = caracteristicas
        self.raca = raca

    # def __str__(self):
        # return f"{self.dog} - {self.nome} - {self.cor} - {self.caracteristicas} - {self.raca}"

dog = Cachorro(nome="Luna",cor="beje",caracteristicas="pequena",raca="pincher")
print(vars(dog))
