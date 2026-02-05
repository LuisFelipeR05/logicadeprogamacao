from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass

class ProdutoIn(BaseModel):
    name:str
    price:float
    stock:int

app = FastAPI()

lista_produto = []

@app.post("/produto")
def cadastrar_novo_produto(produto:ProdutoIn):
    listar_produtos.append(produto)
    return "Produto cadastrado com sucesso!"

@app.get("/produto")
def procurar_produto_por_id(id:int | None = None,nome: str|None = None ):
    return lista_produto(id)

@app.put("/produtos/{id/{novo_nome}")
def atualizar_produto(id:int,novo_nome:str):
    listar_produtos[id] = novo_nome

@app.get("/produtos")
def listar_produtos():
    return listar_produtos

@app.delete("/produtos/{id}")
def deletar_produto(id:int):
    listar_produtos.pop(id)
    return "Produto deletado com sucesso!"
