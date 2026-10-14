from pydantic import BaseModel


class ProdutoCreate(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int