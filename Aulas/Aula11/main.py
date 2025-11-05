# int
# str
# float
# bool

idade = 23 # int
nome = "Luis" # str
altura = 1.83 # float
estudante = True # bool

# 1 Abstração
# reduzir para o que eu preciso 
class Pessoa:
    def __init__(self,nome,altura,idade,peso):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

# objeto da classe Pessoa

p1 = Pessoa(nome="Luis",altura=1.83,idade=23,peso=90)
nome = "Luis"
print(vars(p1))
# class é o tipo do dado
