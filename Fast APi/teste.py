from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# @app.get("/")
# def root():
#     return {"mensagem": "ola mundo"}


class Usuario(BaseModel):
    id: int
    nome: str
    senha: str


lista = [
    Usuario(id=1, nome="caio", senha="minhasenha1"),
    Usuario(id=2, nome="guilherme", senha="minhasenha2"),
    Usuario(id=3, nome="marcos", senha="minhasenha3"),
]

@app.post("/usuario")
def main(usuario: Usuario):
    lista.append(usuario)
    return "usuario cadastrado"
 


@app.get("/usuarioListar")
def main():
    return lista
 