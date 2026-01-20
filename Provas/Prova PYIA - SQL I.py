import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()


cursor.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", 
               ("Luis Silva", 37, "Barreiro"))
cursor.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", 
               ("Gabriel Carlos", 52, "Sabara"))
cursor.execute("INSERT INTO Clientes (Nome, Idade, Cidade) VALUES (?, ?, ?)", 
               ("Ana Clara", 30, "Belo Horizonte"))

conexao.commit()

cursor.execute("SELECT * FROM Clientes")
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)

conexao.close()
