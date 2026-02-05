from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class ProdutoIn(BaseModel):
    name: str
    price: float
    stock: int

class Produto(ProdutoIn):
    id: int

_store: List[dict] = []
_next_id = 1


@app.post("/produto", response_model=Produto, status_code=201)
def cadastrar_novo_produto(produto: ProdutoIn):
    global _next_id
    item = produto.dict()
    item["id"] = _next_id
    _next_id += 1
    _store.append(item)
    return item

@app.get("/produto/{id}", response_model=Produto)
def procurar_produto_por_id(id: int):
    for p in _store:
        if p["id"] == id:
            return p
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.put("/produto/{id}", response_model=Produto)
def atualizar_produto(id: int, novo: ProdutoIn):
    for idx, p in enumerate(_store):
        if p["id"] == id:
            updated = novo.dict()
            updated["id"] = id
            _store[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produto/{id}")
def deletar_produto(id: int):
    for idx, p in enumerate(_store):
        if p["id"] == id:
            _store.pop(idx)
            return {"detail": "Produto deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")