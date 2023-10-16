import requests


retorno = requests.post(
    "http://127.0.0.1:8000/usuario",
    params={"id": 5, "nome": "ze", "senha": "minhasenha5"},
)


print(retorno.json())
