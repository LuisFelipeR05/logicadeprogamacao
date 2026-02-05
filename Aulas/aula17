from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
from dataclasses import dataclass

# INPUT e OUTPUT
class UsuarioIn(BaseModel):
    nome:str 
    email:EmailStr
    telefone:str
    senha: str

class UsuarioOut(BaseModel):
    nome:str 
    email:str

app = FastAPI()

lista_usuarios = []
# Uniforme resource locator 
@app.get("/usuarios")
def listar_usuarios()-> list[UsuarioOut]:# como deve estar a resposta
    return lista_usuarios

@app.get("/usuario/{id}")
def pegar_usuario_por_id(id:int):
    return lista_usuarios[id]

# path param parâmetro de caminho
@app.post("/usuarios")
def cadastrar_novo_usuario(usuario:UsuarioIn):
    lista_usuarios.append(usuario)
    return "Cliente Cadastrado com sucesso!"


@app.delete("/usuarios/{id}")
def deletar_usuario(id:int):
    lista_usuarios.pop(id)
    return "Usuários exlcuido com sucesso!"

@app.put("/usuarios/{id}/{novo_nome}")
def atualizar_usuario(id:int,novo_nome:str):
    lista_usuarios[id] = novo_nome 
