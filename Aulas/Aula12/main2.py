
class Livro:
    def __init__(self,titulo,ano_publi,autor):
        self.titulo = titulo
        self.anoPubli = ano_publi
        self.autor = autor
        self.emprestado = False

class Membro:
    def __init__(self,numero_membro,nome,ano_nasce):
        self.numero_membro = numero_membro
        self.nome = nome
        self.ano_nasce = ano_nasce
        self.historico_livros_emprestados = []


class Biblioteca:
    def __init__(self):
        self.catalogos = []
        self.membros = []

def adicionar_livro_catalogo(self,livro:Livro):
    self.catalogo.append(livro)
    print("livro Adicionado ao catálogo!")

def cadastrar_membro(self,membro:Membro):
    self.membro.append(membro)
    print("Membro cadastrado!")

def emprestar_livro(self,livro:Livro,membro:Membro):
    print(livro in self.catalogo)
    if livro in self.catalogo and livro.emprestado == False and membro in self.membros:
        livro.emprestado = True
        membro.historico_livros_emprestados.append(livro)

def devolver_livro(self,livro:Livro):
    if livro.emprestado == False:
        print("Livro ja está disponível!")
    livro.emprestado = False

def listar_livros_disponiveis(self):
    for livro in self.catalogo:
        print(livro.titulo,livro.autor)

b1 = Biblioteca()

l1 = Livro("Morte e vida severina","1987", "Joao cabral de melo neto")
l2 = Livro("Dom casmurro","1987","Machado de Assis")
m1 = Membro("010203","Joao severino",2004)
b1.adicionar_livro_catalogo(l1)
b1.emprestar_livro(l1,m1)
b1.adicionar_membros(m1)
print(b1.catalogo)
