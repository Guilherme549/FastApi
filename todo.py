from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()


class Todo(BaseModel):
    tarefas: str
    realizada: bool
    prazo: Optional[date]


lista = []


@app.post("/inserir")
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return {"status": "sucesso"}
    except:
        return {"status": "erro"}


@app.post("/listar")
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))


@app.get("/listagemUnica/{id}")
def listar(id: int):
    try:
        return lista[id]
    except:
        return {"status": "erro"}


@app.post("/alteraStatus")
def alteraStatus(id: int):
    try:
        lista[id].realizada = not lista[id].realizada
        return {"status": "sucesso"}
    except:
        return {"status": "erro"}


