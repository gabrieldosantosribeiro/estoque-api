from fastapi import FastAPI

app = FastAPI(
    title="API de Estoque",
    description="API REST para controle de estoque de uma loja de roupas",
    version="0.1.0",
)


@app.get("/")
def raiz():
    return {"mensagem": "API de estoque funcionando"}