
import sqlite3
from datetime import datetime

DB = "estoque_basico.db"

def criar_tabelas(conn):
    cur = conn.cursor()
    cur.executescript("""
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS Produtos (
        ProdutoID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Fornecedores (
        FornecedorID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Estoque (
        EstoqueID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProdutoID INTEGER NOT NULL,
        FornecedorID INTEGER NOT NULL,
        Quantidade INTEGER NOT NULL CHECK (Quantidade >= 0),
        DataEntrada TEXT NOT NULL,
        FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID) ON DELETE RESTRICT ON UPDATE CASCADE,
        FOREIGN KEY (FornecedorID) REFERENCES Fornecedores(FornecedorID) ON DELETE RESTRICT ON UPDATE CASCADE
    );
    """)
    conn.commit()

def inserir_dados_exemplo(conn):
    cur = conn.cursor()
    # Inserir produtos e fornecedores se não existirem
    cur.execute("SELECT COUNT(*) FROM Produtos")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO Produtos (Nome) VALUES (?)",
                        [("Parafuso M6",), ("Porca M6",)])
    cur.execute("SELECT COUNT(*) FROM Fornecedores")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO Fornecedores (Nome) VALUES (?)",
                        [("Fornecedor A",), ("Fornecedor B",)])
    conn.commit()

    # Obter ids
    cur.execute("SELECT ProdutoID FROM Produtos WHERE Nome = ?", ("Parafuso M6",))
    p1 = cur.fetchone()[0]
    cur.execute("SELECT ProdutoID FROM Produtos WHERE Nome = ?", ("Porca M6",))
    p2 = cur.fetchone()[0]
    cur.execute("SELECT FornecedorID FROM Fornecedores WHERE Nome = ?", ("Fornecedor A",))
    f1 = cur.fetchone()[0]
    cur.execute("SELECT FornecedorID FROM Fornecedores WHERE Nome = ?", ("Fornecedor B",))
    f2 = cur.fetchone()[0]

    # Inserir entradas de estoque se tabela vazia
    cur.execute("SELECT COUNT(*) FROM Estoque")
    if cur.fetchone()[0] == 0:
        entradas = [
            (p1, f1, 100, "2026-01-10 00:00:00"),
            (p1, f2, 50,  "2026-02-05 00:00:00"),
            (p2, f1, 200, "2026-01-20 00:00:00"),
        ]
        cur.executemany(
            "INSERT INTO Estoque (ProdutoID, FornecedorID, Quantidade, DataEntrada) VALUES (?, ?, ?, ?)",
            entradas
        )
        conn.commit()

def consultas(conn):
    cur = conn.cursor()

    print("\nEntradas de estoque (INNER JOIN):")
    for row in cur.execute("""
        SELECT e.EstoqueID, p.Nome AS Produto, f.Nome AS Fornecedor, e.Quantidade, e.DataEntrada
        FROM Estoque e
        JOIN Produtos p ON e.ProdutoID = p.ProdutoID
        JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID
        ORDER BY e.EstoqueID
    """):
        print(row)

    print("\nTotal por produto (GROUP BY):")
    for row in cur.execute("""
        SELECT e.ProdutoID, p.Nome, SUM(e.Quantidade) AS TotalQuantidade
        FROM Estoque e
        JOIN Produtos p ON e.ProdutoID = p.ProdutoID
        GROUP BY e.ProdutoID, p.Nome
        ORDER BY TotalQuantidade DESC
    """):
        print(row)

    print("\nEmulação de FULL OUTER JOIN (UNION de LEFT JOINs):")
    sql_full_outer = """
    SELECT p.ProdutoID, p.Nome as ProdutoNome, e.EstoqueID, e.Quantidade, f.FornecedorID, f.Nome as FornecedorNome
    FROM Produtos p
    LEFT JOIN Estoque e ON p.ProdutoID = e.ProdutoID
    LEFT JOIN Fornecedores f ON e.FornecedorID = f.FornecedorID

    UNION

    SELECT p.ProdutoID, p.Nome as ProdutoNome, e.EstoqueID, e.Quantidade, f.FornecedorID, f.Nome as FornecedorNome
    FROM Fornecedores f
    LEFT JOIN Estoque e ON f.FornecedorID = e.FornecedorID
    LEFT JOIN Produtos p ON e.ProdutoID = p.ProdutoID
    """
    for row in cur.execute(sql_full_outer):
        print(row)

def main():
    try:
        conn = sqlite3.connect(DB)
        conn.execute("PRAGMA foreign_keys = ON;")
        criar_tabelas(conn)
        inserir_dados_exemplo(conn)
        consultas(conn)
    except Exception as e:
        print("Erro:", e)
    finally:
        try:
            conn.close()
        except:
            pass

if __name__ == "__main__":
    main()
