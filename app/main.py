from fastapi import FastAPI, HTTPException

from app.schemas import ProdutoCreate
from app.storage import produtos

app = FastAPI(
    title="API de Estoque",
    description="API REST para controle de estoque de uma loja de roupas",
    version="0.1.0",
)


@app.get("/")
def raiz():
    return {"mensagem": "API de estoque funcionando"}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{produto_id}")
def buscar_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")


@app.post("/produtos", status_code=201)
def criar_protudo(produto:ProdutoCreate):
    novo_id = max((p["id"] for p in produtos), default=0) + 1
    novo_produto = {"id": novo_id, **produto.model_dump()}
    produtos.append(novo_produto)
    return novo_produto

@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, dados: ProdutoCreate):
    for produto in produtos:
        if produto["id"] == produto_id:
            produto.update(dados.model_dump())
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.put("produtos/{produto_id}", status_code=204)
def remover_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            produtos.remove(produto)
            return
    raise HTTPException(status_code=404, detail="Produto não encontrado")