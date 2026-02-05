from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./produtos.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ProdutoORM(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

class ProdutoIn(BaseModel):
    name: str
    price: float
    stock: int

class Produto(ProdutoIn):
    id: int

    class Config:
        orm_mode = True

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produto", response_model=Produto, status_code=201)
def cadastrar_novo_produto(produto: ProdutoIn, db: Session = Depends(get_db)):
    novo = ProdutoORM(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.get("/produto/{id}", response_model=Produto)
def procurar_produto_por_id(id: int, db: Session = Depends(get_db)):
    p = db.query(ProdutoORM).filter(ProdutoORM.id == id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p

@app.put("/produto/{id}", response_model=Produto)
def atualizar_produto(id: int, novo: ProdutoIn, db: Session = Depends(get_db)):
    p = db.query(ProdutoORM).filter(ProdutoORM.id == id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    p.name = novo.name
    p.price = novo.price
    p.stock = novo.stock
    db.commit()
    db.refresh(p)
    return p

@app.delete("/produto/{id}")
def deletar_produto(id: int, db: Session = Depends(get_db)):
    p = db.query(ProdutoORM).filter(ProdutoORM.id == id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(p)
    db.commit()
    return {"detail": "Produto deletado com sucesso!"}
