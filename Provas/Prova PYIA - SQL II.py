import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE Produtos (
  ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
  NomeProduto TEXT,
  Quantidade INTEGER,
  Preco REAL
);
""")

cur.executemany(
  "INSERT INTO Produtos (ProdutoID, NomeProduto, Quantidade, Preco) VALUES (?, ?, ?, ?);",
  [
    (1, "calculadora", 15, 249.90),
    (2, "Mouse", 30, 129.50),
    (3, "Teclado", 120, 9.75)
  ]
)

conn.commit()
for row in cur.execute("SELECT * FROM Produtos;"):
    print(row)

conn.close()
